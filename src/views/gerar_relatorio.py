import pandas as pd
import os

# Configurar caminhos para entrada e saída
entrada = 'Base_Dados.xlsx'  # Substitua pelo nome do arquivo fornecido pela empresa
saida = 'relatorio_residuos.xlsx'  # Nome do arquivo gerado com os relatórios

# Verificar se o arquivo de entrada existe
if not os.path.exists(entrada):
    print(f"Erro: O arquivo '{entrada}' não foi encontrado.")
    exit()

# Carregar a planilha em um DataFrame
try:
    df = pd.read_excel(entrada)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    exit()

# Garantir que as colunas necessárias estejam presentes
colunas_necessarias = ['Data', 'Tipo de Resíduo', 'Peso (kg)']
for coluna in colunas_necessarias:
    if coluna not in df.columns:
        print(f"Erro: A coluna '{coluna}' não foi encontrada no arquivo.")
        exit()

# Converter coluna 'Data' para datetime
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

# Verificar se houve erros na conversão de datas
if df['Data'].isnull().any():
    print("Aviso: Algumas datas foram convertidas para 'NaT'. Verifique os dados de entrada.")

# Extrair ano e mês (como número de dois dígitos)
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month.astype(str).str.zfill(2)  # Extrair o mês como número de dois dígitos (01, 02, ..., 12)

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
        relatorio_anual.to_excel(writer, sheet_name=f'{ano}', index=False)
    
    # Relatório mensal por ano
    for ano in anos:
        for mes in sorted(df[df['Ano'] == ano]['Mes'].unique()):
            df_mes = df[(df['Ano'] == ano) & (df['Mes'] == mes)]
            
            # Verificar se há dados para o mês
            if not df_mes.empty:
                nome_aba = f'{mes}/{ano}'  # Nome da aba no formato "MM/AAAA"
                
                # Agrupar os dados por tipo de resíduo
                relatorio_mes = (
                    df_mes.groupby('Tipo de Resíduo')
                    .agg(
                        Peso_Total=('Peso (kg)', 'sum'),
                        Quantidade=('Tipo de Resíduo', 'count')
                    )
                    .reset_index()
                )
                
                # Calcular a frequência
                relatorio_mes['Frequencia'] = relatorio_mes['Quantidade'] / relatorio_mes['Quantidade'].sum()
                
                # Escrever na aba correspondente
                relatorio_mes.to_excel(writer, sheet_name=nome_aba, index=False)

print(f"Relatórios gerados com sucesso no arquivo: {saida}")
