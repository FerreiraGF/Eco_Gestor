import re

class Usuario:
    def __init__(self, nome_empresa, cnpj, cep, email, telefone, senha):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.cep = cep
        self.email = email
        self.telefone = telefone
        self.senha = senha

    @staticmethod
    def formatar_cnpj(cnpj):
        if not re.fullmatch(r'\d{14}', cnpj):
            raise ValueError("CNPJ deve conter 14 números")
        cnpj_formatado = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', cnpj)
        return cnpj_formatado

    @staticmethod
    def formatar_cep(cep):
        if not re.fullmatch(r'\d{8}', cep):
            raise ValueError("CEP deve conter 8 números")
        cep_formatado = re.sub(r'(\d{5})(\d{3})', r'\1-\2', cep)
        return cep_formatado

    @staticmethod
    def formatar_email(email):
        if not re.search(r'[@]', email) or not re.search(r'[.]', email):
            raise ValueError("Email inválido")
        return email

    @staticmethod
    def formatar_telefone(telefone):
        telefone = re.sub(r'\D', '', telefone)
        if not re.fullmatch(r'\d{10,11}', telefone):
            raise ValueError("Telefone deve conter 10 números para telefones fixos ou 11 números para telefones celulares")
        if len(telefone) == 11:
            telefone_formatado = re.sub(r'(\d{2})(\d{5})(\d{4})', r'(\1) \2-\3', telefone)
        elif len(telefone) == 10:
            telefone_formatado = re.sub(r'(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', telefone)
        return telefone_formatado

    @staticmethod
    def formatar_senha(senha):
        if len(senha) < 6 or not re.search(r'[A-Za-z]', senha) or not re.search(r'[0-9]', senha) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            raise ValueError("Senha deve ter no mínimo 6 caracteres, conter pelo menos uma letra, um número e um caractere especial")
        return senha

    def dicionario(self):
        return {
            'Nome da Empresa': self.nome_empresa,
            'CNPJ': self.cnpj,
            'CEP': self.cep,
            'Email': self.email,
            'Telefone': self.telefone,
            'Senha': self.senha
        }