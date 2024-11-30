from tkinter import *
from menu import MenuApp
import subprocess

def open_menu():
    menu_window = Toplevel(root)
    menu_window.title("Menu Lateral")
    menu_window.geometry("300x600")
    app = MenuApp(menu_window)

def abrir_cadastramento():
    subprocess.run(["python", "src/views/cadastro.py"])

# Configuração da janela principal
root = Tk()
root.title("Eco Gestor")
root.geometry("800x600")
root.configure(bg="#EAF7EC")  # Fundo verde claro

# Botão de menu
menu_button = Button(root, text="≡", font=("Arial", 18), command=open_menu, bg="#2A5729", fg="white", relief="flat")
menu_button.place(x=10, y=10)

# Cabeçalho
header_frame = Frame(root, bg="#EAF7EC")
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
join_button = Button(root, text="Quero fazer parte", font=("Arial", 18), command=abrir_cadastramento, bg="#2A5729", fg="white", relief="flat")
join_button.pack(pady=20)



# Área de reviews
review_label = Label(root, text="Review de nossos clientes", font=("Arial", 20, "bold"), fg="#2A5729", bg="#EAF7EC")
review_label.pack(pady=20)

review_frame = Frame(root, bg="#EAF7EC")
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

create_review(review_frame, "Sheila Tirony", 5, "Adorei conhecer vocês! Agora não tem mais desculpa de não saber onde reciclar.")
create_review(review_frame, "Celso Barreto", 5, "Amei a iniciativa. Já indiquei a todos que conheço.")
create_review(review_frame, "Igor Gonzalez", 5, "Ótimo serviço e atendimento ao cliente. Sou cliente fiel.")

# Rodapé
footer_frame = Frame(root, bg="#2A5729")
footer_frame.pack(fill="x", pady=20)

footer_label = Label(
    footer_frame,
    text="O Eco Gestor oferece uma solução inteligente para o descarte de resíduos eletrônicos, otimizando processos\n"
         "e garantindo a conformidade ambiental. Faça parte dessa luta ambiental conosco e ajude a mudar o planeta.",
    font=("Arial", 10),
    fg="white",
    bg="#2A5729",
    justify="center",
    wraplength=700
)
footer_label.pack(pady=10)

contact_label = Label(footer_frame, text="eg_ouvidoria@ecogestor.com.br", font=("Arial", 10, "bold"), fg="white", bg="#2A5729")
contact_label.pack(pady=5)

root.mainloop()
