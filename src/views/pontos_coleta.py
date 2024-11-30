from tkinter import *
from tkinter import ttk

def agendamento_coleta():
    # Criar a janela principal
    janela = Tk()
    janela.title("Agendamento de Coleta")
    janela.geometry("1000x600")
    janela.configure(bg="#EAF7EC")

    # Título da página
    titulo = Label(janela, text="Agendamento de Coleta", font=("Arial", 16, "bold"), bg="#EAF7EC")
    titulo.pack(pady=20)

    # Frame para os campos de entrada
    frame = Frame(janela, bg="#EAF7EC")
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Campo para o CEP
    Label(frame, text="CEP:", font=("Arial", 12), bg="#EAF7EC").grid(row=0, column=0, sticky="w", pady=5)
    cep_entry = Entry(frame, width=30)
    cep_entry.grid(row=0, column=1, pady=5)

    # Campo para a distância de preferência
    Label(frame, text="Distância de Preferência (km):", font=("Arial", 12), bg="#EAF7EC").grid(row=1, column=0, sticky="w", pady=5)
    distancia_entry = Entry(frame, width=30)
    distancia_entry.grid(row=1, column=1, pady=5)

    # Campo para o produto a ser descartado
    Label(frame, text="Produto a ser Descartado:", font=("Arial", 12), bg="#EAF7EC").grid(row=2, column=0, sticky="w", pady=5)
    produto_entry = Entry(frame, width=30)
    produto_entry.grid(row=2, column=1, pady=5)

    # Botão para agendar a coleta
    agendar_button = Button(frame, text="Agendar Coleta", font=("Arial", 12), bg="#2A5729", fg="white")
    agendar_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Criar o rodapé
    footer_frame = Frame(janela, bg="#2A5729", height=120)
    footer_frame.pack(side="bottom", fill="x")

    # Configurar o grid no footer_frame
    footer_frame.grid_columnconfigure(0, weight=1)
    footer_frame.grid_columnconfigure(1, weight=1)

    # Texto à esquerda do rodapé
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
    left_text.grid(row=0, column=0, sticky="w", padx=10)

    # Texto à direita do rodapé
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
    right_text.grid(row=0, column=1, sticky="e", padx=10)

    # Exibir a janela
    janela.mainloop()

# Chamar a função para criar a interface
agendamento_coleta()