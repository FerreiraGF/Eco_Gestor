from tkinter import *
import pandas as pd
from tkinter import messagebox
from openpyxl import load_workbook

# Função para criar ou adicionar à planilha com o CEP, nome da empresa, produto e empresa selecionada
def criar_planilha(cep, empresa, produto):
    # Dados a serem registrados
    dados = {
        'CEP': [cep],
        'Empresa': [empresa],
        'Produto': [produto]
    }
    df = pd.DataFrame(dados)
    
    try:
        # Tentar carregar o arquivo Excel existente
        wb = load_workbook('enderecos_empresas.xlsx')
        ws = wb.active
        # Adicionar os dados na próxima linha disponível
        for i, row in df.iterrows():
            ws.append(row.values.tolist())
        wb.save('enderecos_empresas.xlsx')
    except FileNotFoundError:
        # Se o arquivo não existir, crie um novo arquivo
        df.to_excel('enderecos_empresas.xlsx', index=False)

# Função para exibir as empresas e botões de seleção
def procurar_empresas():
    # Obter o CEP digitado
    cep = cep_entry.get()

    # Verificando se o CEP foi digitado
    if cep:
        # Exibindo as empresas e botões de seleção
        empresa_label1.config(text="Amorim Eco - Avenida Gomes, 1902\nFonseca, Salvador\n1km de distância - Aberto agora")
        empresa_label2.config(text="SustentabilIgor - Rua Tirony, 245\nParalela, Salvador\n2km de distância - Aberto agora")

        # Tornando os botões visíveis para selecionar uma empresa
        botao_selecionar1.grid(row=6, column=3, pady=10)  # Posiciona à direita da tela, ao lado do primeiro endereço
        botao_selecionar2.grid(row=7, column=3, pady=10)  # Posiciona à direita da tela, ao lado do segundo endereço

    else:
        # Caso o CEP não tenha sido preenchido, mostrar um aviso
        mensagem_label.config(text="Por favor, digite o CEP.")

# Função para selecionar a empresa
def selecionar_empresa(empresa):
    global empresa_selecionada
    empresa_selecionada = empresa
    mensagem_label.config(text=f"Você selecionou: {empresa}")

    # Tornar o botão "Agendar Coleta" visível após a seleção da empresa
    agendar_button.grid(row=9, column=0, columnspan=2, pady=40)  # Aumentei o pady para dar mais espaço

# Função para agendar a coleta e salvar na planilha
def agendar_coleta():
    cep = cep_entry.get()
    produto = produto_entry.get()

    # Verificando se o CEP, produto e a empresa foram selecionados
    if cep and produto and empresa_selecionada:
        criar_planilha(cep, empresa_selecionada, produto)
        # Exibir pop-up com a mensagem de confirmação
        messagebox.showinfo("Agendamento", "A empresa entrará em contato em breve!")
        mensagem_label.config(text=f"Coleta agendada com {empresa_selecionada}!\nProduto: {produto}\nCEP: {cep}")
    else:
        mensagem_label.config(text="Por favor, preencha todos os campos e selecione uma empresa.")

# Função para exibir a lista de produtos descartáveis
def mostrar_lista_descartaveis():
    lista = [
        "Antenas", "Baterias", "Calculadoras eletrônicas", "Cabos e fios", "Câmeras de segurança", "Discos rígidos",
        "Eletrodomésticos", "Equipamentos de áudio", "Equipamentos de medição eletrônica", "Equipamentos médicos eletrônicos",
        "Equipamentos de rede", "Impressoras", "Jogos eletrônicos", "Leitores de DVD/Blu-ray", "Monitores", "Projetores",
        "Rádios", "Roteadores", "Sistemas de segurança eletrônicos", "Tablets", "Teclados e mouses", "Telefones celulares",
        "Televisores", "Videogames"
    ]
    
    # Exibe a lista em um novo pop-up
    lista_str = "\n".join(lista)
    messagebox.showinfo("O que pode ser descartado", lista_str)

def agendamento_coleta():
    global cep_entry, produto_entry, empresa_selecionada, empresa_label1, empresa_label2, botao_selecionar1, botao_selecionar2, mensagem_label, agendar_button

    empresa_selecionada = None  # Inicializa a variável da empresa selecionada

    # Criar a janela principal
    janela = Tk()
    janela.title("Agendamento de Coleta")
    janela.geometry("900x700") 
    janela.configure(bg="#EAF7EC")

    # Título da página
    titulo = Label(janela, text="Agendamento de Coleta", font=("Arial", 16, "bold"), bg="#EAF7EC")
    titulo.pack(pady=20)

    # Frame principal
    form_frame = Frame(janela, bg="#EAF7EC")
    form_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Campo para o CEP
    Label(form_frame, text="CEP:", font=("Arial", 12), bg="#EAF7EC").grid(row=1, column=0, sticky="w", pady=5)
    cep_entry = Entry(form_frame, width=50)
    cep_entry.grid(row=1, column=1, pady=5, sticky="ew")

    # Campo para o Produto a ser Descartado
    Label(form_frame, text="Produto a ser Descartado:", font=("Arial", 12), bg="#EAF7EC").grid(row=2, column=0, sticky="w", pady=5)
    produto_entry = Entry(form_frame, width=50)
    produto_entry.grid(row=2, column=1, pady=5, sticky="ew")

    # Campo para a Distância de Preferência
    Label(form_frame, text="Distância de Preferência (km):", font=("Arial", 12), bg="#EAF7EC").grid(row=3, column=0, sticky="w", pady=5)
    distancia_entry = Entry(form_frame, width=50)
    distancia_entry.grid(row=3, column=1, pady=5, sticky="ew")

    # Botão "O que pode ser descartado" - posicionado acima do botão "Procurar Empresas"
    descartado_button = Button(
        form_frame,
        text="O que pode ser descartado",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=mostrar_lista_descartaveis  # Chama a função que exibe a lista
    )
    descartado_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para procurar as empresas
    procurar_button = Button(
        form_frame,
        text="Procurar Empresas",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=procurar_empresas  # Associa a função ao botão
    )
    procurar_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Labels para exibir as empresas (esses labels inicialmente ficam invisíveis)
    empresa_label1 = Label(
        form_frame,
        text="",
        font=("Arial", 12),
        bg="#EAF7EC",
        fg="#333333",
        anchor="w",
        justify="left"
    )
    empresa_label1.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")

    empresa_label2 = Label(
        form_frame,
        text="",
        font=("Arial", 12),
        bg="#EAF7EC",
        fg="#333333",
        anchor="w",
        justify="left"
    )
    empresa_label2.grid(row=7, column=0, columnspan=2, pady=10, sticky="w")

    # Botões para selecionar as empresas - agora com o alinhamento correto
    botao_selecionar1 = Button(
        form_frame,
        text="Selecionar",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=lambda: selecionar_empresa("Amorim Eco")  # Seleciona a primeira empresa
    )
    botao_selecionar1.grid(row=6, column=3, pady=10, padx=10)
    botao_selecionar1.grid_forget()  # Esconde inicialmente

    botao_selecionar2 = Button(
        form_frame,
        text="Selecionar",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=lambda: selecionar_empresa("Green Solutions")  # Seleciona a segunda empresa
    )
    botao_selecionar2.grid(row=7, column=3, pady=10, padx=10)
    botao_selecionar2.grid_forget()  # Esconde inicialmente

    # Label para mensagens
    mensagem_label = Label(form_frame, text="", font=("Arial", 12), bg="#EAF7EC", fg="#333333")
    mensagem_label.grid(row=8, column=0, columnspan=2, pady=10)

    # Botão "Agendar Coleta" - inicialmente invisível
    agendar_button = Button(
        form_frame,
        text="Agendar Coleta",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=agendar_coleta  # Chama a função para agendar a coleta
    )
    agendar_button.grid(row=9, column=0, columnspan=2, pady=40)  # Aumentei o pady para dar mais espaço
    agendar_button.grid_forget()  # Esconde inicialmente

    # Rodapé
    footer_frame = Frame(janela, bg="#2A5729", height=120)
    footer_frame.pack(side="bottom", fill="x")

    left_text = Label(
        footer_frame,
        text="O Eco Gestor oferece uma solução inteligente para o descarte de resíduos eletrônicos, otimizando processos e garantindo a conformidade ambiental. Faça parte dessa luta ambiental conosco e ajude a mudar o planeta.",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="left",
        padx=20,
        wraplength=350,
        anchor="w"
    )
    left_text.pack(side="left", anchor="w", padx=10)

    right_text = Label(
        footer_frame,
        text="Envie seu feedback para nós! Sua opinião nos ajuda a melhorar e transformar o planeta em um lugar melhor!\n eg_ouvidoria@ecogestor.com.br",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="right",
        padx=20,
        wraplength=350,
        anchor="e"
    )
    right_text.pack(side="right", anchor="e", padx=10)

    janela.mainloop()

# Chamar a função para criar a interface
agendamento_coleta()
