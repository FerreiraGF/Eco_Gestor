from tkinter import *

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Lateral")

        # Cria o frame da aba lateral
        self.sidebar = Frame(self.root, width=200, bg="#EAF7EC", height=500, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        # Adiciona os botões na aba lateral
        self.add_sidebar_button("Meu Perfil")
        self.add_sidebar_button("Enviar Relatório")
        self.add_sidebar_button("Pontos de Coleta")
        self.add_sidebar_button("Certificado e Selo EcoGestor")
        self.add_sidebar_button("Sobre Nós")
        self.add_sidebar_button("Contato")
        self.add_sidebar_button("Política de Privacidade")
        self.add_sidebar_button("FAQ")

        # Cria o frame do conteúdo principal
        self.main_content = Frame(self.root, bg='#fff', width=500, height=500)
        self.main_content.pack(expand=True, fill='both', side='right')

    def add_sidebar_button(self, text):
        button = Button(self.sidebar, text=text, bg="#EAF7EC", fg='black', relief='flat')
        button.pack(fill='x')

if __name__ == "__main__":
    root = Tk()
    app = MenuApp(root)
    root.mainloop()