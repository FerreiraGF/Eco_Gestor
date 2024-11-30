from tkinter import *
from tkinter import messagebox

def cadastrar():
    if senha.get() != confirmar_senha.get():
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return
    if not termos_var.get():
        messagebox.showerror("Erro", "Você deve concordar com os termos de uso e políticas de privacidade!")
        return
    # adicionar o código para salvar os dados do cadastro
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

root = Tk()
root.title("Cadastro")

frame = Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

Label(frame, text="Nome da Empresa:").grid(row=0, column=0, sticky="w")
nome_empresa = Entry(frame, width=50)
nome_empresa.grid(row=0, column=1, pady=5)

Label(frame, text="CNPJ:").grid(row=1, column=0, sticky="w")
cnpj = Entry(frame, width=50)
cnpj.grid(row=1, column=1, pady=5)

Label(frame, text="CEP:").grid(row=1, column=2, sticky="w")
cep = Entry(frame, width=50)
cep.grid(row=1, column=3, pady=5)

Label(frame, text="E-mail para Contato:").grid(row=2, column=0, sticky="w")
email = Entry(frame, width=50)
email.grid(row=2, column=1, pady=5)

Label(frame, text="Telefone para Contato:").grid(row=3, column=0, sticky="w")
telefone = Entry(frame, width=50)
telefone.grid(row=3, column=1, pady=5)

Label(frame, text="Senha para Login:").grid(row=4, column=0, sticky="w")
senha = Entry(frame, show="*", width=25)
senha.grid(row=4, column=1, pady=5)

Label(frame, text="Digite a Senha Novamente:").grid(row=4, column=2, sticky="w")
confirmar_senha = Entry(frame, show="*", width=25)
confirmar_senha.grid(row=4, column=3, pady=5)

mensagem = Label(frame, text="Senha deve conter: de 6 a 30 caracteres pelo menos uma letra e um número", font=("Arial", 10, "bold"))
mensagem.grid(row=5, column=0, columnspan=4, pady=5)

termos_var = BooleanVar()
termos = Checkbutton(frame, text="Eu li e concordo com os termos de uso e políticas de privacidade", variable=termos_var)
termos.grid(row=7, column=0, columnspan=4, pady=5)

botao_cadastrar = Button(frame, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(row=8, column=0, columnspan=4, pady=10)

root.mainloop()