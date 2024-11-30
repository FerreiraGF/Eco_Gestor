from tkinter import *

def exibir_termos():
    termos_window = Tk()
    termos_window.title("Termos de Uso")
    termos_window.geometry("1000x800")
    termos_window.configure(bg="#EAF7EC")

    termos_text = """
    Data de Vigência: 23 de setembro de 2024
    Bem-vindo ao Eco Gestor! Ao acessar e utilizar nossa plataforma, você concorda com os seguintes termos e condições. Se não concordar com algum deles,
    pedimos que não utilize nossos serviços.

    1. Aceitação dos Termos
    Ao utilizar o Eco Gestor, você concorda em respeitar todos os termos e condições estabelecidos.

    2. Uso da Plataforma
    Você se compromete a utilizar o Eco Gestor apenas para fins lícitos e em conformidade com a legislação vigente. É proibido:
    - Utilizar a plataforma para atividades fraudulentas ou ilegais.
    - Compartilhar informações falsas ou enganosas.
    - Interferir na segurança da plataforma ou comprometê-la de qualquer forma.

    3. Cadastro e Responsabilidades
    Para acessar determinados serviços, pode ser necessário criar uma conta. Você é responsável por:
    - Manter a confidencialidade das informações da sua conta.
    - Notificar imediatamente o Eco Gestor sobre qualquer uso não autorizado da sua conta.
    - Garantir que as informações fornecidas durante o cadastro sejam precisas e atualizadas.

    4. Propriedade Intelectual
    Todo o conteúdo disponível no Eco Gestor, incluindo textos, imagens, logotipos e design, é protegido por direitos autorais e outras leis de propriedade
    intelectual. A reprodução ou distribuição não autorizada de qualquer parte da plataforma é proibida.

    5. Limitação de Responsabilidade
    O Eco Gestor não se responsabiliza por danos diretos, indiretos, incidentais ou consequenciais resultantes do uso ou da incapacidade de uso da plataforma.

    6. Modificações nos Termos
    O Eco Gestor reserva-se o direito de modificar estes Termos de Uso a qualquer momento. As alterações serão publicadas na plataforma, e o uso contínuo do
    serviço implica na aceitação das novas condições.

    7. Cancelamento de Conta
    O Eco Gestor pode, a seu exclusivo critério, suspender ou cancelar sua conta a qualquer momento, sem aviso prévio, em caso de violação destes termos.

    8. Disposições Finais
    Estes Termos de Uso são regidos pelas leis do Brasil. Qualquer disputa relacionada a estes termos será resolvida nos tribunais competentes em território
    brasileiro.
    """

    termos_label = Label(termos_window, text=termos_text, font=("Arial", 12), bg="#EAF7EC", justify="left", anchor="nw")
    termos_label.pack(padx=20, pady=20, fill="both", expand=True)

    ok_button = Button(termos_window, text="OK", font=("Arial", 14), command=termos_window.destroy, bg="#2A5729", fg="white", relief="flat")
    ok_button.pack(pady=20)

    termos_window.mainloop()

# Exibir a janela de Termos de Uso diretamente
exibir_termos()