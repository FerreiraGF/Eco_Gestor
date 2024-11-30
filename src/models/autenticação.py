import pandas as pd

# Carregar os usuários cadastrados
pl_cadastrados = pd.read_excel('Usuarios_Cadastrados.xlsx')

def verificar_login(email, senha):
    # Verificando se o email e senha estão corretos
    for index, usuario in pl_cadastrados.iterrows():
        if usuario['E-mail'] == email and usuario['Senha'] == senha:
            return True
    return False