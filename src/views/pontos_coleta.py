from tkinter import *
import pandas as pd
from tkinter import messagebox
from openpyxl import load_workbook


def criar_planilha(cep, empresa, produto):
    
    dados = {
        'CEP': [cep],
        'Empresa': [empresa],
        'Produto': [produto]
    }
    df = pd.DataFrame(dados)
    
    try:
      
        wb = load_workbook('enderecos_empresas.xlsx')
        ws = wb.active
        for i, row in df.iterrows():
            ws.append(row.values.tolist())
        wb.save('enderecos_empresas.xlsx')
    except FileNotFoundError:
        df.to_excel('enderecos_empresas.xlsx', index=False)


def procurar_empresas():
    cep = cep_entry.get()

    if cep:
        empresa_label1.config(text="Amorim Eco - Avenida Gomes, 1902\nFonseca, Salvador\n1km de distância - Aberto agora")
        empresa_label2.config(text="SustentabilIgor - Rua Tirony, 245\nParalela, Salvador\n2km de distância - Aberto agora")

        botao_selecionar1.grid(row=6, column=3, pady=10)  
        botao_selecionar2.grid(row=7, column=3, pady=10)  

    else:
        mensagem_label.config(text="Por favor, digite o CEP.")


def selecionar_empresa(empresa):
    global empresa_selecionada
    empresa_selecionada = empresa
    mensagem_label.config(text=f"Você selecionou: {empresa}")

    agendar_button.grid(row=9, column=0, columnspan=2, pady=40) 

def agendar_coleta():
    cep = cep_entry.get()
    produto = produto_entry.get()

    if cep and produto and empresa_selecionada:
        criar_planilha(cep, empresa_selecionada, produto)
      
        messagebox.showinfo("Agendamento", "A empresa entrará em contato em breve!")
        mensagem_label.config(text=f"Coleta agendada com {empresa_selecionada}!\nProduto: {produto}\nCEP: {cep}")
    else:
        mensagem_label.config(text="Por favor, preencha todos os campos e selecione uma empresa.")


def mostrar_lista_descartaveis():
    lista = [
        "Antenas", "Baterias", "Calculadoras eletrônicas", "Cabos e fios", "Câmeras de segurança", "Discos rígidos",
        "Equipamentos de áudio","Impressoras", "Jogos eletrônicos", "Leitores de DVD/Blu-ray", "Monitores", "Projetores",
        "Rádios", "Roteadores", "Sistemas de segurança eletrônicos", "Tablets", "Teclados e mouses", "Telefones celulares",
        "Televisores", "Videogames"
    ]
    
    lista_str = "\n".join(lista)
    messagebox.showinfo("O que pode ser descartado", lista_str)

def agendamento_coleta():
    global cep_entry, produto_entry, empresa_selecionada, empresa_label1, empresa_label2, botao_selecionar1, botao_selecionar2, mensagem_label, agendar_button

    empresa_selecionada = None  

    janela = Tk()
    janela.title("Agendamento de Coleta")
    janela.geometry("900x850") 
    janela.configure(bg="#EAF7EC")

    titulo = Label(janela, text="Agendamento de Coleta", font=("Arial", 16, "bold"), bg="#EAF7EC")
    titulo.pack(pady=20)

    form_frame = Frame(janela, bg="#EAF7EC")
    form_frame.pack(padx=20, pady=20, fill="both", expand=True)

    Label(form_frame, text="CEP:", font=("Arial", 12), bg="#EAF7EC").grid(row=1, column=0, sticky="w", pady=5)
    cep_entry = Entry(form_frame, width=50)
    cep_entry.grid(row=1, column=1, pady=5, sticky="ew")

    Label(form_frame, text="Produto a ser Descartado:", font=("Arial", 12), bg="#EAF7EC").grid(row=2, column=0, sticky="w", pady=5)
    produto_entry = Entry(form_frame, width=50)
    produto_entry.grid(row=2, column=1, pady=5, sticky="ew")

    Label(form_frame, text="Distância de Preferência (km):", font=("Arial", 12), bg="#EAF7EC").grid(row=3, column=0, sticky="w", pady=5)
    distancia_entry = Entry(form_frame, width=50)
    distancia_entry.grid(row=3, column=1, pady=5, sticky="ew")

    descartado_button = Button(
        form_frame,
        text="O que pode ser descartado",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=mostrar_lista_descartaveis  
    )
    descartado_button.grid(row=4, column=0, columnspan=2, pady=10)

    procurar_button = Button(
        form_frame,
        text="Procurar Empresas",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=procurar_empresas  
    )
    procurar_button.grid(row=5, column=0, columnspan=2, pady=20)

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

    botao_selecionar1 = Button(
        form_frame,
        text="Selecionar",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=lambda: selecionar_empresa("Amorim Eco") 
    )
    botao_selecionar1.grid(row=6, column=3, pady=10, padx=10)
    botao_selecionar1.grid_forget() 

    botao_selecionar2 = Button(
        form_frame,
        text="Selecionar",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=lambda: selecionar_empresa("Green Solutions")  
    )
    botao_selecionar2.grid(row=7, column=3, pady=10, padx=10)
    botao_selecionar2.grid_forget()  

   
    mensagem_label = Label(form_frame, text="", font=("Arial", 12), bg="#EAF7EC", fg="#333333")
    mensagem_label.grid(row=8, column=0, columnspan=2, pady=10)

    agendar_button = Button(
        form_frame,
        text="Agendar Coleta",
        font=("Arial", 12),
        bg="#2A5729",
        fg="white",
        command=agendar_coleta  
    )
    agendar_button.grid(row=9, column=0, columnspan=2, pady=40)  
    agendar_button.grid_forget()  

    # Rodapé
    footer_frame = Frame(janela, bg="#2A5729", height=120)
    footer_frame.pack(side="bottom", fill="x")
    footer_frame.pack_propagate(False)

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