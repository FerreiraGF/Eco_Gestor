from tkinter import *
from tkinter import font
from tkinter import filedialog
import os
import shutil

def insercao_dados():
    def selecionar_arquivo():
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo",
            filetypes=[("Arquivos Excel", "*.xlsx *.xls"), ("Todos os arquivos", "*.*")]
        )
        if arquivo:
            destino = os.path.join(os.getcwd(), os.path.basename(arquivo))
            shutil.copy(arquivo, destino)  # Copia o arquivo selecionado para a pasta atual
            print(f"Arquivo selecionado: {arquivo}")
            print(f"Arquivo salvo em: {destino}")
            arquivo_label.config(text=f"Arquivo salvo: {os.path.basename(arquivo)}")

    janela = Tk()
    janela.title("Inserção de Dados - Eco Gestor")
    janela.geometry("1000x600")  
    
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_opcao = font.Font(family="Arial", size=12)
    fonte_botoes = font.Font(family="Arial", size=12)

    titulo = Label(janela, text="Inserção de Dados", font=fonte_titulo, anchor="w", padx=20)
    titulo.pack(pady=20, fill="x")

    funcao_label = Label(janela, text="Selecione a opção que melhor representa sua função:", font=fonte_opcao, anchor="w", padx=20)
    funcao_label.pack(anchor="w", padx=20)

    funcao_var = StringVar()
    gerar_lixo_btn = Radiobutton(janela, text="Estou gerando o lixo", variable=funcao_var, value="gerando", font=fonte_opcao)
    recolher_lixo_btn = Radiobutton(janela, text="Vou recolher o lixo", variable=funcao_var, value="recolhendo", font=fonte_opcao)
    gerar_lixo_btn.pack(anchor="w", padx=40)
    recolher_lixo_btn.pack(anchor="w", padx=40)

    relatorio_label = Label(janela, text="Selecionar o tipo de documento:", font=fonte_opcao, anchor="w", padx=20)
    relatorio_label.pack(anchor="w", padx=20)

    relatorio_var = StringVar()
    csv_btn = Radiobutton(janela, text="CSV", variable=relatorio_var, value="csv", font=fonte_opcao)
    xlsx_btn = Radiobutton(janela, text="XLSX", variable=relatorio_var, value="xlsx", font=fonte_opcao)
    csv_btn.pack(anchor="w", padx=40)
    xlsx_btn.pack(anchor="w", padx=40)

    arquivo_label = Label(janela, text="Clique aqui para selecionar o arquivo no seu computador", font=fonte_opcao, anchor="w", padx=20)
    arquivo_label.pack(pady=10, anchor="w", padx=20)

    selecionar_arquivo_btn = Button(
        janela, 
        text="Selecionar Arquivo", 
        font=fonte_botoes, 
        command=selecionar_arquivo, 
        bg="#2A5729", 
        fg="white", 
        width=20
    )
    selecionar_arquivo_btn.pack(pady=10)

    enviar_btn = Button(janela, text="ENVIAR", font=fonte_botoes, bg="#2A5729", fg="white", width=20)
    enviar_btn.pack(pady=20)

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

insercao_dados()
