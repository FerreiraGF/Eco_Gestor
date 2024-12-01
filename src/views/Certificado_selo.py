from tkinter import *


janela = Tk()
janela.title("Certificado e Selo de Responsabilidade Ambiental")
janela.geometry("1000x600")
janela.configure(bg="#EAF7EC")

certificado_texto = (
    "O Eco Gestor oferece um certificado e selo de responsabilidade ambiental para empresas que realizam o descarte de resíduos eletrônicos de forma "
    "confiável e responsável. Para ser elegível ao selo basta usar nossos serviços frequentemente há mais de um semestre e fazer descarte/coleta responsável "
    "do e-lixo, depois é só renovar o certificado anualmente para garantir responsabilidade com o meio-ambiente."
)
texto_certificado = Label(janela, text=certificado_texto, font=("Arial", 12), justify="left", padx=10, pady=10, bg="#EAF7EC", wraplength=750)
texto_certificado.pack(pady=10)

botao_aplicar_certificado = Button(janela, text="Quero aplicar para o certificado", font=("Arial", 12), width=30, bg="#2A5729", fg="white")
botao_aplicar_certificado.pack(pady=10)

botao_acessar_certificado = Button(janela, text="Acessar certificado", font=("Arial", 12), width=30, bg="#2A5729", fg="white")
botao_acessar_certificado.pack(pady=10)

# Rodapé
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