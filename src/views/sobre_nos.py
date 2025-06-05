from tkinter import *
from tkinter import font

def sobre_nos():
    # Criar a janela principal com o título e a geometria
    janela = Tk()
    janela.title("Sobre Nós - Eco Gestor")
    janela.geometry("1000x400")  

    # Definir a fonte para o título e o texto, agora usando Arial
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_texto = font.Font(family="Arial", size=12)

    # Criar o título da página
    titulo = Label(janela, text="Sobre Nós", font=fonte_titulo)
    titulo.pack(pady=10)

    # Criar o texto da seção "Sobre Nós"
    sobre_nos_texto = (
        "O Eco Gestor, desde 2024, oferece às grandes empresas, centros empresariais e instituições de ensino uma\n"
        "solução inteligente para o descarte de resíduos eletrônicos, utilizando análise de dados para otimizar o processo\n"
        "e garantir a conformidade ambiental.\n\n"
        
        "Nossa parceria com a ABREE assegura que o descarte seja feito de forma correta e responsável, fortalecendo a\n"
        "imagem da empresa como uma organização comprometida com a sustentabilidade. As empresas que adotam nossas práticas\n"
        "recebem o Selo de Certificação Responsabilidade Ambiental, valorizando sua reputação e destacando seu compromisso com\n"
        "um futuro mais sustentável."
    )

    # Criar o rótulo para o texto da seção "Sobre Nós"
    texto_sobre_nos = Label(janela, text=sobre_nos_texto, font=fonte_texto, justify="left", padx=10, pady=10)
    texto_sobre_nos.pack()

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

# Chamar a função para criar a página "Sobre Nós"
sobre_nos()
