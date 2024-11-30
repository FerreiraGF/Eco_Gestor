import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from models.autenticação import verificar_login  # Importar a função de verificação de login

def recuperar_senha():
    # Função para exibir a tela de recuperação de senha
    janela_recuperacao = Toplevel()
    janela_recuperacao.title("Recuperação de Senha")
    janela_recuperacao.geometry("400x200")
    janela_recuperacao.configure(bg="#EAF7EC")

    Label(janela_recuperacao, text="Recuperação de Senha", font=("Arial", 16, "bold"), bg="#EAF7EC").pack(pady=20)
    Label(janela_recuperacao, text="Digite seu e-mail para recuperar a senha:", font=("Arial", 12), bg="#EAF7EC").pack(pady=5)
    email_entry = Entry(janela_recuperacao, width=30)
    email_entry.pack(pady=5)
    Button(janela_recuperacao, text="Enviar", font=("Arial", 12), bg="#2A5729", fg="white").pack(pady=20)

def login():
    # verificação de dados do login
    email = cnpj_entry.get()
    senha = senha_entry.get()
    if verificar_login(email, senha):
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos!")

# Criar a janela principal
janela = Tk()
janela.title("Login")
janela.geometry("400x300")
janela.configure(bg="#EAF7EC")

# Título da página
titulo = Label(janela, text="Login", font=("Arial", 16, "bold"), bg="#EAF7EC")
titulo.pack(pady=20)

# Campo para o E-mail
Label(janela, text="E-mail:", font=("Arial", 12), bg="#EAF7EC").pack(pady=5)
cnpj_entry = Entry(janela, width=30)
cnpj_entry.pack(pady=5)

# Campo para a senha
Label(janela, text="Senha:", font=("Arial", 12), bg="#EAF7EC").pack(pady=5)
senha_entry = Entry(janela, show="*", width=30)
senha_entry.pack(pady=5)

# Mensagem "Esqueceu sua senha?"
esqueceu_senha = Label(janela, text="Esqueceu sua senha?", font=("Arial", 10, "underline"), fg="black", bg="#EAF7EC", cursor="hand2")
esqueceu_senha.pack(pady=5)
esqueceu_senha.bind("<Button-1>", lambda e: recuperar_senha())

# Botão de login
login_button = Button(janela, text="Login", font=("Arial", 12), bg="#2A5729", fg="white", command=login)
login_button.pack(pady=20)

# Exibir a janela
janela.mainloop()