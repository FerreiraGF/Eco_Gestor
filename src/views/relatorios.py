import tkinter as tk
import webbrowser
from tkinter import font

# Função para criar a interface
def pagina_relatorios():
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Relatórios em Andamento - Eco Gestor")
    janela.geometry("1000x600")  # Definir tamanho da janela

    # Definir a fonte para o título e os textos
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_opcao = font.Font(family="Arial", size=12)
    fonte_botoes = font.Font(family="Arial", size=12)

    # Título "Relatórios em Andamento" centralizado
    titulo = tk.Label(janela, text="Relatórios em Andamento", font=fonte_titulo, anchor="center")
    titulo.pack(pady=20, fill="x", anchor="center")

    # Frame para os relatórios
    relatorios_frame = tk.Frame(janela)
    relatorios_frame.pack(pady=30, anchor="w", padx=20)

    # Função para abrir o link do PDF no navegador
    def abrir_relatorio(url):
        webbrowser.open(url)

    # Títulos e Botões dos relatórios (em negrito e mais largos)
    relatorio1_titulo = tk.Label(relatorios_frame, text="Relatório do dia 23/11", font=("Arial", 12, "bold"), anchor="w")
    relatorio1_titulo.grid(row=0, column=0, pady=5, sticky="w")
    relatorio1_btn1 = tk.Button(relatorios_frame, text="Visualizar Relatório", font=fonte_opcao, bg="#2A5729", fg="white", 
                               width=110, command=lambda: abrir_relatorio("https://drive.google.com/uc?id=186-HgIweo0m4R2xdegSR5fWklIedua9J"))
    relatorio1_btn1.grid(row=1, column=0, pady=10, sticky="ew")

    # Rodapé
    footer_frame = tk.Frame(janela, bg="#2A5729", height=120)
    footer_frame.pack(side="bottom", fill="x")

    # Texto à esquerda do rodapé
    left_text = tk.Label(
        footer_frame,
        text="O Eco Gestor oferece uma solução inteligente para o descarte de resíduos eletrônicos, otimizando processos e garantindo a conformidade ambiental. Faça parte dessa luta ambiental conosco e ajude a mudar o planeta.",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="left",
        padx=20,
        wraplength=300,  # Quebra automática de texto
        anchor="w"
    )
    left_text.pack(side="left", anchor="w", padx=10)

    # Texto à direita do rodapé
    right_text = tk.Label(
        footer_frame,
        text="Envie seu feedback para nós! Sua opinião nos ajuda a melhorar e transformar o planeta em um lugar melhor!\n eg_ouvidoria@ecogestor.com.br",
        font=("Arial", 9),
        fg="white",
        bg="#2A5729",
        justify="right",
        padx=20,
        wraplength=300,  # Quebra automática de texto
        anchor="e"
    )
    right_text.pack(side="right", anchor="e", padx=10)

    # Exibir a janela
    janela.mainloop()

# Chamar a função para criar a página
pagina_relatorios()
