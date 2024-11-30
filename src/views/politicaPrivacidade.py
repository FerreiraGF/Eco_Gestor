from tkinter import *

def exibir_politica():
    janela = Tk()
    janela.title("Política de Privacidade")
    janela.geometry("1300x900")
    janela.configure(bg="#EAF7EC")

    politica_text = """
    Data de Vigência: 23 de setembro de 2024.
    Sua privacidade é importante para nós. Esta Política de Privacidade explica como coletamos, usamos, armazenamos e protegemos suas informações ao utilizar nossa
    plataforma.

    1. Coleta de Informações
    Coletamos informações que você fornece diretamente, incluindo, mas não se limitando a:
    - Dados pessoais (nome, e-mail, telefone) ao criar uma conta.
    - Informações sobre suas atividades na plataforma.

    2. Uso das Informações
    Utilizamos suas informações para:
    - Fornecer e gerenciar nossos serviços.
    - Comunicar atualizações e novidades sobre a plataforma.
    - Melhorar a experiência do usuário.

    3. Compartilhamento de Informações
    Não vendemos, trocamos ou alugamos suas informações pessoais a terceiros. Podemos compartilhar suas informações nas seguintes circunstâncias:
    - Com prestadores de serviços que nos ajudam a operar a plataforma.
    - Para cumprir obrigações legais ou proteger nossos direitos.

    4. Armazenamento de Dados
    Suas informações são armazenadas em servidores seguros. Implementamos medidas de segurança para proteger seus dados contra acesso não autorizado, uso ou divulgação.

    5. Seus Direitos
    Você tem o direito de:
    - Acessar, corrigir ou excluir suas informações pessoais.
    - Solicitar a limitação do uso de suas informações.
    - Revogar seu consentimento para o tratamento de dados.

    6. Cookies
    Utilizamos cookies para melhorar a experiência do usuário. Você pode optar por não aceitar cookies, mas isso pode limitar a funcionalidade da plataforma.

    7. Alterações na Política de Privacidade
    Reservamo-nos o direito de modificar esta Política de Privacidade a qualquer momento. As alterações serão publicadas na plataforma, e seu uso contínuo implicará na
    aceitação da nova política.

    8. Contato
    Se você tiver dúvidas ou preocupações sobre nossa Política de Privacidade, entre em contato conosco pelo e-mail: ecogestor@org.com.br.
    """

    politica_label = Label(janela, text=politica_text, font=("Arial", 12), bg="#EAF7EC", justify="left", anchor="nw")
    politica_label.pack(padx=20, pady=20, fill="both", expand=True)

    ok_button = Button(janela, text="OK", font=("Arial", 14), command=janela.destroy, bg="#2A5729", fg="white", relief="flat")
    ok_button.pack(pady=20)
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