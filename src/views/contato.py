from tkinter import *
import webbrowser
from tkinter import font

# Função para criar a interface de Contato
def criar_pagina_contato():
    # Criar a janela principal
    janela = Tk()
    janela.title("Contato - Eco Gestor")
    janela.geometry("1000x600") 

    # Definir a fonte para o título e os textos
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_opcao = font.Font(family="Arial", size=12)

    titulo = Label(janela, text="Entre em Contato", font=fonte_titulo, anchor="center")
    titulo.pack(pady=20, fill="x", anchor="center")

    # Frame para as informações de contato
    contato_frame = Frame(janela)
    contato_frame.pack(pady=30, anchor="w", padx=20)

    # Títulos e Links clicáveis 
    
    # Instagram
    contato1 = Label(contato_frame, text="Instagram: EcoGestorOrg", font=("Arial", 12, "bold"), anchor="w", fg="blue", cursor="hand2")
    contato1.grid(row=0, column=0, pady=5, sticky="w")
    contato1.bind("<Button-1>", lambda e: webbrowser.open("https://www.instagram.com/EcoGestorOrg"))

    # LinkedIn
    contato2 = Label(contato_frame, text="LinkedIn: EcoGestor", font=("Arial", 12, "bold"), anchor="w", fg="blue", cursor="hand2")
    contato2.grid(row=2, column=0, pady=5, sticky="w")
    contato2.bind("<Button-1>", lambda e: webbrowser.open("https://www.linkedin.com/company/EcoGestor"))

    # E-mail
    contato3 = Label(contato_frame, text="E-mail: ecogestor@org.com.br", font=("Arial", 12, "bold"), anchor="w", fg="blue", cursor="hand2")
    contato3.grid(row=4, column=0, pady=5, sticky="w")
    contato3.bind("<Button-1>", lambda e: webbrowser.open("mailto:ecogestor@org.com.br"))

    # Telefone
    contato4 = Label(contato_frame, text="Telefone: (71) XXXXX-XXXX", font=("Arial", 12, "bold"), anchor="w", fg="blue", cursor="hand2")
    contato4.grid(row=6, column=0, pady=5, sticky="w")
    contato4.bind("<Button-1>", lambda e: webbrowser.open("tel:(71) XXXXX-XXXX"))

    # Endereço
    contato5 = Label(contato_frame, text="Endereço: Av. Luís Viana Filho, 6775 - Paralela, Salvador - BA", font=("Arial", 12, "bold"), anchor="w", fg="blue", cursor="hand2")
    contato5.grid(row=8, column=0, pady=5, sticky="w")
    contato5.bind("<Button-1>", lambda e: webbrowser.open("https://www.google.com/maps/place/Av.+Lu%C3%ADs+Viana+Filho,+6775+-+Paralela,+Salvador+-+BA"))

    # Rodapé
    footer_frame = Frame(janela, bg="#2A5729", height=120)
    footer_frame.pack(side="bottom", fill="x")

    # Texto à esquerda do rodapé
    left_text = Label(
        footer_frame,
        text="O Eco Gestor oferece uma solução inteligente para o descarte de resíduos eletrônicos, otimizando processos e garantindo a conformidade ambiental. Faça parte dessa luta ambiental conosco e ajude a mudar o planeta.",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="left",
        padx=20,
        wraplength=350,  # Quebra automática de texto
        anchor="w"
    )
    left_text.pack(side="left", anchor="w", padx=10)

    # Texto à direita do rodapé
    right_text = Label(
        footer_frame,
        text="Envie seu feedback para nós! Sua opinião nos ajuda a melhorar e transformar o planeta em um lugar melhor!\n eg_ouvidoria@ecogestor.com.br",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="right",
        padx=20,
        wraplength=350,  # Quebra automática de texto
        anchor="e"
    )
    right_text.pack(side="right", anchor="e", padx=10)

    # Exibir a janela
    janela.mainloop()

# Chamar a função para criar a página
criar_pagina_contato()
