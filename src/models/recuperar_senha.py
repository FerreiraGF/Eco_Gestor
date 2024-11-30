import pandas as pd
from tkinter import *
from tkinter import messagebox

# Função para carregar a planilha de usuários cadastrados
def carregar_planilha():
    return pd.read_excel('Usuarios_Cadastrados.xlsx')

# Função para salvar a planilha de usuários cadastrados
def salvar_planilha(pl_cadastrados):
    pl_cadastrados.to_excel('Usuarios_Cadastrados.xlsx', index=False)

# Função para exibir a tela de alteração de senha
def exibir_tela_alteracao_senha(email):
    def alterar_senha():
        nova_senha = nova_senha_entry.get()
        pl_cadastrados = carregar_planilha()
        pl_cadastrados.loc[pl_cadastrados['E-mail'] == email, 'Senha'] = nova_senha
        salvar_planilha(pl_cadastrados)
        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        janela_alteracao_senha.destroy()

    janela_alteracao_senha = Toplevel()
    janela_alteracao_senha.title("Alteração de Senha")
    janela_alteracao_senha.geometry("400x200")
    janela_alteracao_senha.configure(bg="#EAF7EC")

    Label(janela_alteracao_senha, text="Alteração de Senha", font=("Arial", 16, "bold"), bg="#EAF7EC").pack(pady=20)
    Label(janela_alteracao_senha, text="Digite sua nova senha:", font=("Arial", 12), bg="#EAF7EC").pack(pady=5)
    nova_senha_entry = Entry(janela_alteracao_senha, show="*", width=30)
    nova_senha_entry.pack(pady=5)
    Button(janela_alteracao_senha, text="Alterar Senha", font=("Arial", 12), bg="#2A5729", fg="white", command=alterar_senha).pack(pady=20)

# Função para recuperar a senha
def recuperar_senha():
    def enviar_link():
        email = email_entry.get()
        pl_cadastrados = carregar_planilha()
        if email in pl_cadastrados['E-mail'].values:
            messagebox.showinfo("Link Enviado", "Um link de alteração de senha foi enviado para o seu e-mail.")
            janela_recuperacao.destroy()
            exibir_tela_alteracao_senha(email)
        else:
            messagebox.showerror("Erro", "E-mail não encontrado!")

    # Criar a janela de recuperação de senha
    janela_recuperacao = Toplevel()
    janela_recuperacao.title("Recuperação de Senha")
    janela_recuperacao.geometry("400x200")
    janela_recuperacao.configure(bg="#EAF7EC")

    Label(janela_recuperacao, text="Recuperação de Senha", font=("Arial", 16, "bold"), bg="#EAF7EC").pack(pady=20)
    Label(janela_recuperacao, text="Digite seu e-mail:", font=("Arial", 12), bg="#EAF7EC").pack(pady=5)
    email_entry = Entry(janela_recuperacao, width=30)
    email_entry.pack(pady=5)
    Button(janela_recuperacao, text="Enviar", font=("Arial", 12), bg="#2A5729", fg="white", command=enviar_link).pack(pady=20)

# Testar a função de recuperação de senha
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    recuperar_senha()
    root.mainloop()