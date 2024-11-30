from tkinter import *
from tkinter import messagebox
import subprocess

def exibir_termos():
    subprocess.Popen(['python', 'TermosUso.py'])

def exibir_politica():
    subprocess.Popen(['python', 'politicaPrivacidade.py'])

def cadastrar():
    if senha.get() != confirmar_senha.get():
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return
    if not termos_var.get():
        messagebox.showerror("Erro", "Você deve concordar com os termos de uso e políticas de privacidade!")
        return
    # ################adicionar o código para salvar os dados do cadastro
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

janela = Tk()
janela.title("Cadastro")

frame = Frame(janela, padx=10, pady=10)
frame.pack(padx=10, pady=10)

Label(frame, text="Nome da Empresa:").grid(row=0, column=0, sticky="w")
nome_empresa = Entry(frame, width=50)
nome_empresa.grid(row=0, column=1, pady=5)

Label(frame, text="CNPJ:").grid(row=1, column=0, sticky="w")
cnpj = Entry(frame, width=50)
cnpj.grid(row=1, column=1, pady=5)

Label(frame, text="CEP:").grid(row=2, column=0, sticky="w")
cep = Entry(frame, width=50)
cep.grid(row=2, column=1, pady=5)

Label(frame, text="E-mail para Contato:").grid(row=3, column=0, sticky="w")
email = Entry(frame, width=50)
email.grid(row=3, column=1, pady=5)

Label(frame, text="Senha:").grid(row=4, column=0, sticky="w")
senha = Entry(frame, show="*", width=50)
senha.grid(row=4, column=1, pady=5)

Label(frame, text="Confirmar Senha:").grid(row=5, column=0, sticky="w")
confirmar_senha = Entry(frame, show="*", width=50)
confirmar_senha.grid(row=5, column=1, pady=5)

termos_var = BooleanVar()
termos_check = Checkbutton(frame, text="Eu concordo com os Termos de Uso e Políticas de Privacidade", variable=termos_var)
termos_check.grid(row=6, column=0, columnspan=2, pady=5)

# Botões para exibir os Termos de Uso e Política de Privacidade
buttons_frame = Frame(frame)
buttons_frame.grid(row=7, column=0, columnspan=2, pady=5)

termos_button = Button(buttons_frame, text="Termos de Uso", command=exibir_termos)
termos_button.pack(side=LEFT, padx=10)

politica_button = Button(buttons_frame, text="Política de Privacidade", command=exibir_politica)
politica_button.pack(side=LEFT, padx=10)

Button(frame, text="Cadastrar", command=cadastrar).grid(row=8, column=0, columnspan=2, pady=10)
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