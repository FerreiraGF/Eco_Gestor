import tkinter as tk
import webbrowser
from tkinter import font

# Função para criar a interface da nova página
def pagina_novo_relatorio():
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Relatório - Eco Gestor")
    janela.geometry("1000x600")  # Definir tamanho da janela

    # Definir a fonte para o título e os textos
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_opcao = font.Font(family="Arial", size=12)

    # Título "Relatório do dia 23/11" centralizado
    titulo = tk.Label(janela, text="Relatório do dia 23/11", font=fonte_titulo)
    titulo.pack(pady=20, fill="x", anchor="center")

    # Função para abrir o link no navegador
    def abrir_relatorio(url):
        webbrowser.open(url)

    # Primeira frase à esquerda para visualizar o relatório
    visualizar_label = tk.Label(
        janela, 
        text="Visualizar o relatório enviado por você:",
        font=fonte_opcao,
        anchor="w"
    )
    visualizar_label.pack(padx=20, anchor="w", pady=10)

    # Botão para visualizar o relatório
    visualizar_btn = tk.Button(
        janela, 
        text="Clique aqui para visualizar", 
        font=fonte_opcao, 
        bg="#2A5729", 
        fg="white", 
        command=lambda: abrir_relatorio("https://drive.google.com/uc?id=186-HgIweo0m4R2xdegSR5fWklIedua9J")
    )
    visualizar_btn.pack(padx=20, pady=10, anchor="w", fill="x")

    # Segunda frase com o status e link para baixar o arquivo
    status_label = tk.Label(
        janela, 
        text="Status:",
        font=fonte_opcao,
        anchor="w"
    )
    status_label.pack(padx=20, anchor="w", pady=20)

    # Botão para baixar o arquivo
    baixar_btn = tk.Button(
        janela, 
        text="Concluído - Clique aqui para baixar o relatório", 
        font=fonte_opcao, 
        bg="#2A5729", 
        fg="white", 
        command=lambda: abrir_relatorio("https://drive.google.com/uc?id=186-HgIweo0m4R2xdegSR5fWklIedua9J")
    )
    baixar_btn.pack(padx=20, pady=10, anchor="w", fill="x")

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

# Chamar a função para criar a nova página
pagina_novo_relatorio()
