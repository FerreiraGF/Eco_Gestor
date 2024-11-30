from tkinter import *

def exibir_faq():
    janela = Tk()
    janela.title("Perguntas Frequentes (FAQ)")
    janela.geometry("1450x600")
    janela.configure(bg="#EAF7EC")

    faq_text = """
    Perguntas Frequentes (FAQ)

    1. O que é o Eco Gestor?
    O Eco Gestor é uma plataforma que oferece soluções inteligentes para o descarte de resíduos eletrônicos, utilizando análise de dados para otimizar o processo e garantir a conformidade ambiental.

    2. Como posso me cadastrar no Eco Gestor?
    Você pode se cadastrar no Eco Gestor acessando a página de cadastro e preenchendo as informações necessárias, como nome da empresa, CNPJ, CEP, e-mail para contato e senha.

    3. Quais tipos de resíduos eletrônicos posso descartar?
    Você pode descartar diversos tipos de resíduos eletrônicos, como baterias, computadores, celulares, monitores, impressoras, teclados, mouses, cabos, câmeras e controles.

    4. Como o Eco Gestor garante a segurança dos meus dados?
    O Eco Gestor implementa medidas de segurança para proteger seus dados contra acesso não autorizado, uso ou divulgação. Seus dados são armazenados em servidores seguros.

    5. Como posso entrar em contato com o suporte do Eco Gestor?
    Você pode entrar em contato com o suporte do Eco Gestor pelo e-mail: ecogestor@org.com.br.
    """

    # Frame para o conteúdo principal
    content_frame = Frame(janela, bg="#EAF7EC")
    content_frame.pack(padx=20, pady=20, fill="both", expand=True)

    faq_label = Label(content_frame, text=faq_text, font=("Arial", 12), bg="#EAF7EC", justify="left", anchor="nw")
    faq_label.pack(fill="both", expand=True)

    ok_button = Button(content_frame, text="OK", font=("Arial", 14), command=janela.destroy, bg="#2A5729", fg="white", relief="flat")
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

# Exibir a janela de FAQ diretamente
exibir_faq()