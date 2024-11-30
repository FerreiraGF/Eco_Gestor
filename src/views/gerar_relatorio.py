import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.chart import PieChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows

# Caminho do arquivo de entrada e saída
arquivo = 'Base_Dados.xlsx'  # Substitua pelo caminho completo do arquivo se necessário
saida = 'relatorio.xlsx'

# Verificar se o arquivo existe
if not os.path.exists(arquivo):
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    exit()

# Carregar a planilha
try:
    df = pd.read_excel(arquivo)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    exit()

# Garantir que a coluna 'Data' esteja no formato datetime
try:
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    if df['Data'].isnull().any():
        print("Aviso: Algumas datas foram convertidas para 'NaT'. Verifique os dados de entrada.")
except KeyError:
    print("Erro: A coluna 'Data' não foi encontrada no arquivo.")
    exit()

# Extrair ano e mês (como número de dois dígitos)
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month.astype(str).str.zfill(2)  # Extrair o mês como número de dois dígitos (01, 02, ..., 12)

# Função para sanitizar nomes de abas
def sanitize_sheet_name(sheet_name):
    invalid_chars = ['\\', '/', '*', '[', ']', ':', '?']
    for char in invalid_chars:
        sheet_name = sheet_name.replace(char, '_')
    return sheet_name

# Criar um escritor para Excel
with pd.ExcelWriter(saida, engine='openpyxl') as writer:
    # Relatório por ano
    anos = sorted(df['Ano'].dropna().unique())
    
    # Criar relatório anual
    for ano in anos:
        df_ano = df[df['Ano'] == ano]
        relatorio_anual = (
            df_ano.groupby('Tipo de Resíduo')
            .agg(
                Peso_Total=('Peso (kg)', 'sum'),
                Quantidade=('Tipo de Resíduo', 'count')
            )
            .reset_index()
        )
        relatorio_anual['Frequencia'] = relatorio_anual['Quantidade'] / relatorio_anual['Quantidade'].sum()
        
        # Adicionar uma aba para o ano
        nome_aba = sanitize_sheet_name(f'{ano}')
        relatorio_anual.to_excel(writer, sheet_name=nome_aba, index=False)
    
    # Consolidar relatórios mensais em uma única planilha por ano
    for ano in anos:
        df_ano_mes = df[df['Ano'] == ano].groupby(['Mes', 'Tipo de Resíduo']).agg(
            Peso_Total=('Peso (kg)', 'sum'),
            Quantidade=('Tipo de Resíduo', 'count')
        ).reset_index()
        
        # Adicionar uma aba para os relatórios mensais consolidados
        nome_aba_mensal = sanitize_sheet_name(f'relatorios_mensais_{ano}')
        df_ano_mes.to_excel(writer, sheet_name=nome_aba_mensal, index=False)

# Adicionar gráficos para os anos de 2022 e 2023
wb = load_workbook(saida)

for ano in [2022, 2023]:
    if str(ano) in wb.sheetnames:
        ws = wb[str(ano)]
        
        # Gráfico de Porcentagem de Tipos de Resíduos
        df_tipo_residuo = df[df['Ano'] == ano].groupby('Tipo de Resíduo').agg(Quantidade=('Tipo de Resíduo', 'count')).reset_index()
        df_tipo_residuo['Porcentagem'] = df_tipo_residuo['Quantidade'] / df_tipo_residuo['Quantidade'].sum()
        
        # Criar uma nova planilha para o gráfico de tipos de resíduos
        ws_tipos_residuos = wb.create_sheet(title=f'Tipos_Residuos_{ano}')
        for r in dataframe_to_rows(df_tipo_residuo, index=False, header=True):
            ws_tipos_residuos.append(r)
        
        pie_chart = PieChart()
        labels = Reference(ws_tipos_residuos, min_col=1, min_row=2, max_row=len(df_tipo_residuo) + 1)
        data = Reference(ws_tipos_residuos, min_col=3, min_row=1, max_row=len(df_tipo_residuo) + 1)
        pie_chart.add_data(data, titles_from_data=True)
        pie_chart.set_categories(labels)
        pie_chart.title = f'Porcentagem de Tipos de Resíduos - {ano}'
        pie_chart.style = 10  # Estilo do gráfico
        pie_chart.width = 20  # Largura do gráfico
        pie_chart.height = 10  # Altura do gráfico
        ws_tipos_residuos.add_chart(pie_chart, 'E5')
        
        # Consolidar relatórios mensais em uma única planilha
        df_ano_mes = df[df['Ano'] == ano].groupby(['Mes', 'Tipo de Resíduo']).agg(
            Peso_Total=('Peso (kg)', 'sum'),
            Quantidade=('Tipo de Resíduo', 'count')
        ).reset_index()
        
        # Criar uma nova planilha para os relatórios mensais consolidados
        ws_mensal_consolidado = wb.create_sheet(title=f'Relatorios_Mensais_{ano}')
        current_row = 1
        for mes in sorted(df[df['Ano'] == ano]['Mes'].unique()):
            df_mes = df_ano_mes[df_ano_mes['Mes'] == mes]
            ws_mensal_consolidado.append([f'Mês: {mes}'])
            for r in dataframe_to_rows(df_mes, index=False, header=True):
                ws_mensal_consolidado.append(r)
            current_row += len(df_mes) + 2  # Adicionar espaço entre as tabelas
        
        # Gráfico de Peso por Mês
        df_peso_mes = df[df['Ano'] == ano].groupby('Mes').agg(Peso_Total=('Peso (kg)', 'sum')).reset_index()
        ws_peso_mensal = wb.create_sheet(title=f'Peso_Mensal_{ano}')
        for r in dataframe_to_rows(df_peso_mes, index=False, header=True):
            ws_peso_mensal.append(r)
        
        pie_chart_peso = PieChart()
        labels_peso = Reference(ws_peso_mensal, min_col=1, min_row=2, max_row=len(df_peso_mes) + 1)
        data_peso = Reference(ws_peso_mensal, min_col=2, min_row=1, max_row=len(df_peso_mes) + 1)
        pie_chart_peso.add_data(data_peso, titles_from_data=True)
        pie_chart_peso.set_categories(labels_peso)
        pie_chart_peso.title = f'Peso por Mês - {ano}'
        pie_chart_peso.style = 10  # Estilo do gráfico
        pie_chart_peso.width = 20  # Largura do gráfico
        pie_chart_peso.height = 10  # Altura do gráfico
        ws_peso_mensal.add_chart(pie_chart_peso, 'E5')

wb.save(saida)

print("Relatório gerado com sucesso!")