import tkinter as tk
from tkinter import font
import subprocess


janela = tk.Tk()
janela.title("Relatórios")
janela.geometry("1045x600")

fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
fonte_opcao = font.Font(family="Arial", size=12)

titulo = tk.Label(janela, text="Relatórios em Andamento", font=fonte_titulo, anchor="center")
titulo.pack(pady=20, fill="x", anchor="center")

relatorios_frame = tk.Frame(janela)
relatorios_frame.pack(pady=30, anchor="w", padx=20)

def abrir_relatorio():
    subprocess.run(["python", "src/views/relatorios_multi.py"])

relatorio1_titulo = tk.Label(relatorios_frame, text="Relatório do dia 23/11", font=("Arial", 12, "bold"), anchor="w")
relatorio1_titulo.grid(row=0, column=0, pady=5, sticky="w")
relatorio1_btn1 = tk.Button(relatorios_frame, text="Status: Concluído - Clique aqui para saber mais", font=fonte_opcao, bg="#2A5729", fg="white", 
                            width=110, command=lambda: abrir_relatorio())
relatorio1_btn1.grid(row=1, column=0, pady=10, sticky="ew")

# Rodapé
footer_frame = tk.Frame(janela, bg="#2A5729", height=120)
footer_frame.pack(side="bottom", fill="x")

left_text = tk.Label(
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

janela.mainloop()