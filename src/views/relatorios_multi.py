import tkinter as tk
from tkinter import font, messagebox
import os

# Configuração da janela principal
janela = tk.Tk()
janela.title("Relatórios Multi")
janela.geometry("1100x600")
janela.configure(bg="#EAF7EC")  # Fundo verde claro

# Definir a fonte para o título e os textos
fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
fonte_opcao = font.Font(family="Arial", size=12)

# Título "Relatório do dia 23/11" centralizado
titulo = tk.Label(janela, text="Relatório do dia 23/11", font=fonte_titulo, bg="#EAF7EC", fg="#2A5729")
titulo.pack(pady=20, fill="x", anchor="center")

# função para abrir a Base de dados
def abrir_base_dados():
    caminho_base_dados = os.path.join(os.getcwd(), "Base_Dados.xlsx")
    if os.path.exists(caminho_base_dados):
        os.startfile(caminho_base_dados)
    else:
        messagebox.showerror("Erro", "O arquivo base_dados.xlsx não foi encontrado.")
# Função para abrir o relatório
def abrir_relatorio():
    caminho_relatorio = os.path.join(os.getcwd(), "relatorio.xlsx")
    if os.path.exists(caminho_relatorio):
        os.startfile(caminho_relatorio)
    else:
        messagebox.showerror("Erro", "O arquivo relatorio.xlsx não foi concluído.")

# Primeira frase à esquerda para visualizar o relatório
visualizar_label = tk.Label(
    janela, 
    text="Visualizar o relatório enviado por você:",
    font=fonte_opcao,
    anchor="w",
    bg="#EAF7EC",
    fg="#2A5729"
)
visualizar_label.pack(padx=20, anchor="w", pady=10)

# Botão para visualizar o relatório
visualizar_btn = tk.Button(
    janela, 
    text="Clique aqui para visualizar", 
    font=fonte_opcao, 
    bg="#2A5729", 
    fg="white", 
    command=abrir_base_dados
)
visualizar_btn.pack(padx=20, pady=10, anchor="w", fill="x")

# Segunda frase com o status e link para baixar o arquivo
status_label = tk.Label(
    janela, 
    text="Status:",
    font=fonte_opcao,
    anchor="w",
    bg="#EAF7EC",
    fg="#2A5729"
)
status_label.pack(padx=20, anchor="w", pady=10)

# Botão para baixar o arquivo
baixar_btn = tk.Button(
    janela, 
    text="Clique aqui para baixar", 
    font=fonte_opcao, 
    bg="#2A5729", 
    fg="white", 
    command=abrir_relatorio 
)
baixar_btn.pack(padx=20, pady=10, anchor="w", fill="x")

# Criar o rodapé
footer_frame = tk.Frame(janela, bg="#2A5729", height=120)
footer_frame.pack(side="bottom", fill="x")

# Texto à esquerda do rodapé
left_text = tk.Label(
    footer_frame,
    text="O Eco Gestor oferece uma solução inteligente para o\n"
         "descarte de resíduos eletrônicos, otimizando processos\n"
         "e garantindo a conformidade ambiental. Faça parte dessa\n"
         "luta ambiental conosco e ajude a mudar o planeta.",
    font=("Arial", 9),
    fg="white",
    bg="#2A5729",
    justify="left",
    padx=20,
    wraplength=350,
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
    wraplength=350,
    anchor="e"
)
right_text.pack(side="right", anchor="e", padx=10)

# Exibir a janela
janela.mainloop()