import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from models.auten import verificar_login 
from models.recuperar_senha import recuperar_senha

def login(parent):
    # Criar a janela de login
    janela = Toplevel(parent)
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

    # Função de verificação de login
    def verificar():
        email = cnpj_entry.get()
        senha = senha_entry.get()
        if verificar_login(email, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos!")

    # Mensagem "Esqueceu sua senha?"
    esqueceu_senha = Label(janela, text="Esqueceu sua senha?", font=("Arial", 10, "underline"), fg="black", bg="#EAF7EC", cursor="hand2")
    esqueceu_senha.pack(pady=5)
    esqueceu_senha.bind("<Button-1>", lambda e: recuperar_senha())

    # Botão de login
    login_button = Button(janela, text="Login", font=("Arial", 12), bg="#2A5729", fg="white", command=verificar)
    login_button.pack(pady=20)

# Exibir a janela
if __name__ == "__main__":
    root = Tk()
    login(root)
    root.mainloop()