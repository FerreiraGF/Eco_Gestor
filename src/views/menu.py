from tkinter import *
import subprocess
from pontos_coleta import agendamento_coleta 

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Lateral")
        self.root.geometry("150x500")

        # Cria o frame da aba lateral
        self.sidebar = Frame(self.root, width=200, bg="#EAF7EC", height=500, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        # Adiciona os botões na aba lateral
        self.add_sidebar_button("Meu Perfil", self.exibir_meu_perfil)
        self.add_sidebar_button("Enviar Relatório", self.exibir_insercao_dados)
        self.add_sidebar_button("Agendar Coleta", self.exibir_pontos_coleta)
        self.add_sidebar_button("Relatórios", self.exibir_relatorio)
        self.add_sidebar_button("Certificado e Selo EcoGestor", self.exibir_certificado)
        self.add_sidebar_button("Sobre Nós", self.exibir_sobre_nos)
        self.add_sidebar_button("Contato", self.exibir_contato)
        self.add_sidebar_button("Política de Privacidade", self.exibir_politica)
        self.add_sidebar_button("FAQ", self.exibir_faq)

    def add_sidebar_button(self, text, command=None):
        button = Button(self.sidebar, text=text, bg="#EAF7EC", fg='black', relief='flat', command=command)
        button.pack(fill='x')

    def exibir_politica(self):
        subprocess.run(["python", "src/views/politicaPrivacidade.py"])

    def exibir_faq(self):
        subprocess.run(["python", "src/views/FAQ.py"])

    def exibir_certificado(self):
        subprocess.run(["python", "src/views/certificado_selo.py"])
        
    def exibir_sobre_nos(self):
        subprocess.run(["python", "src/views/sobre_nos.py"])
    
    def exibir_contato(self):
        subprocess.run(["python", "src/views/contato.py"])
        
    def exibir_relatorio(self):
        subprocess.run(["python", "src/views/relatorios.py"])
    
    def exibir_insercao_dados(self):
        subprocess.run(["python", "src/views/insercao_dados.py"])
        
    def exibir_pontos_coleta(self):
        agendamento_coleta()  # Chamar a função de agendamento de coleta
    
    def exibir_meu_perfil(self):
        subprocess.run(["python", "src/views/meuperfil.py"])