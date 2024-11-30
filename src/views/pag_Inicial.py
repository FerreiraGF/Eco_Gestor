from tkinter import *
from menu import MenuApp
import subprocess

def open_menu():
    menu_window = Toplevel(janela)
    menu_window.title("Menu Lateral")
    menu_window.geometry("300x600")
    app = MenuApp(menu_window)

def abrir_cadastramento():
    subprocess.run(["python", "src/views/cadastro.py"])

# Configuração da janela principal
janela = Tk()
janela.title("Eco Gestor")
janela.geometry("800x600")
janela.configure(bg="#EAF7EC")  # Fundo verde claro

# Botão de menu
menu_button = Button(janela, text="≡", font=("Arial", 18), command=open_menu, bg="#2A5729", fg="white", relief="flat")
menu_button.place(x=10, y=10)

# Cabeçalho
header_frame = Frame(janela, bg="#EAF7EC")
header_frame.pack(pady=20)

logo_label = Label(header_frame, text="Eco Gestor", font=("Inter", 36, "bold"), fg="#2A5729", bg="#EAF7EC")
logo_label.pack()

subtitle_label = Label(
    header_frame,
    text="O Eco Gestor oferece às grandes empresas, centros empresariais e instituições de ensino\n"
         "uma solução inteligente para o descarte de resíduos eletrônicos, utilizando análise de dados\n"
         "para otimizar o processo e garantir a conformidade ambiental.",
    font=("Arial", 12),
    fg="#2A5729",
    bg="#EAF7EC",
    justify="center"
)
subtitle_label.pack()

# Botão "Quero fazer parte"
join_button = Button(janela, text="Quero fazer parte", font=("Arial", 18), command=abrir_cadastramento, bg="#2A5729", fg="white", relief="flat")
join_button.pack(pady=20)



# Área de reviews
review_label = Label(janela, text="Review de nossos clientes", font=("Arial", 20, "bold"), fg="#2A5729", bg="#EAF7EC")
review_label.pack(pady=20)

review_frame = Frame(janela, bg="#EAF7EC")
review_frame.pack(pady=10)

# Clientes
def create_review(parent, name, stars, comment):
    frame = Frame(parent, bg="white", relief="solid", bd=1)
    frame.pack(side="left", padx=10, pady=5)

    name_label = Label(frame, text=name, font=("Arial", 10, "bold"), fg="#2A5729", bg="white")
    name_label.pack(pady=5)

    stars_label = Label(frame, text="★" * stars, font=("Arial", 10), fg="#FFD700", bg="white")
    stars_label.pack()

    comment_label = Label(frame, text=comment, font=("Arial", 10), fg="black", bg="white", wraplength=150, justify="center")
    comment_label.pack(pady=5)

create_review(review_frame, "Sheila Tirony", 5, "Adorei o site! Agora não tem mais desculpa para não reciclar.")
create_review(review_frame, "Celso Barreto", 5, "Amei a iniciativa. Já indiquei a todos que conheço.")
create_review(review_frame, "Igor Gonzalez", 5, "Ótimo serviço e atendimento ao cliente. Sou cliente fiel.")

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

janela.mainloop()
