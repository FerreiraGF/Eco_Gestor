from tkinter import *
from tkinter import messagebox
from tkinter import font

# Função para criar a interface de perfil
def criar_pagina_perfil():
    # Criar a janela principal
    janela = Tk()
    janela.title("Meu Perfil - EcoGestor")
    janela.geometry("1000x600")  # Definir tamanho da janela

    # Definir a fonte para o título e os textos
    fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
    fonte_opcao = font.Font(family="Arial", size=12)

    # Título "Meu Perfil" centralizado
    titulo = Label(janela, text="Meu Perfil", font=fonte_titulo, anchor="center")
    titulo.pack(pady=20, fill="x", anchor="center")

    # Informações de perfil
    info_frame = Frame(janela)
    info_frame.pack(pady=20)

    # Exibir as informações centralizadas
    nome_empresa = Label(info_frame, text="Empresa: Caio", font=("Arial", 12, "bold"))
    nome_empresa.pack(pady=5, anchor="center")  # Centralizando a informação

    # Colocar CEP e CNPJ lado a lado, ambos centralizados
    cep = Label(info_frame, text="CEP: 2222222", font=("Arial", 12, "bold"))
    cep.pack(pady=5, anchor="center")  # Centralizando a informação
    
    cnpj = Label(info_frame, text="CNPJ: 1111111111", font=("Arial", 12, "bold"))
    cnpj.pack(pady=5, anchor="center")  # Centralizando a informação

    # Informações adicionais
    email = Label(info_frame, text="Email: unijorge@gmail.com", font=("Arial", 12, "bold"))
    email.pack(pady=5, anchor="center")  # Centralizando a informação

    usuario_desde = Label(info_frame, text="Usuário desde: 19/02/2024", font=("Arial", 12, "bold"))
    usuario_desde.pack(pady=5, anchor="center")  # Centralizando a informação

    # Botões de ações
    botoes_frame = Frame(janela)
    botoes_frame.pack(pady=20)

    # Botão "Alterar Senha" e "Excluir Conta"
    alterar_senha_button = Button(botoes_frame, text="Alterar Senha", font=fonte_opcao, bg="#2A5729", fg="white", width=20, command=alterar_senha)
    alterar_senha_button.grid(row=0, column=0, padx=20)

    excluir_conta_button = Button(botoes_frame, text="Excluir Conta", font=fonte_opcao, bg="#2A5729", fg="white", width=20, command=excluir_conta)
    excluir_conta_button.grid(row=0, column=1, padx=20)

    # Botão "Log Out"
    logout_button = Button(janela, text="Log Out", font=fonte_opcao, bg="#2A5729", fg="white", width=20, command=logout)
    logout_button.pack(pady=20)

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

# Função de Logout
def logout():
    resposta = messagebox.showinfo("Log Out", "Logout realizado!")
    janela.quit()

# Função de Excluir Conta com confirmação
def excluir_conta():
    confirmacao = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir sua conta?")
    
    if confirmacao:
        # Se o usuário confirmar, exibe a mensagem de despedida
        messagebox.showinfo("Exclusão", "Uma pena te ver ir embora. Se isso for um erro, favor contatar nosso suporte.\n\nA equipe EcoGestor agradece sua parceria.")
        janela.quit()
    else:
        # Se o usuário cancelar a exclusão, retorna para o perfil
        messagebox.showinfo("Cancelado", "Você não excluiu sua conta. Retornando para o seu perfil...")
        janela.quit()

# Função de Alterar Senha
def alterar_senha():
    # Exibir a mensagem de confirmação simulando o envio do email
    messagebox.showinfo("Alteração de Senha", "Enviamos um email para você com as instruções de recuperação de senha.")

# Chamar a função para criar a página de perfil
criar_pagina_perfil()
