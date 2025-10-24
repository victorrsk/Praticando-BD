import re

def validar_nome(nome):
    nome_pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    if len(nome) > 150:
        print('Nome muito extenso')
        return False
    
    elif re.fullmatch(nome_pattern, nome):
            return True
    
    print('Nome inválido')
    return False

def validar_email(email):
    email_pattern = r'[a-zA-Z0-9]{5,}((@gmail.com){1}$)'
    
    if len(email) > 150:
        print('email muito extenso')
        return False
    
    elif re.fullmatch(email_pattern, email):
        return True
    
    print('email inválido')
    return False

def validar_cpf(cpf):
    cpf_pattern = r'^[0-9]{3}.{1}[0-9]{3}.{1}[0-9]{3}-{1}[0-9]{2}'
    if re.fullmatch(cpf_pattern, cpf):
        return True
    
    print('CPF inválido')
    return False

def validar_dados(nome, email, cpf):
    nome_valido = validar_nome(nome)
    email_valido = validar_email(email)
    cpf_valido = validar_cpf(cpf)
    
    if nome_valido and email_valido and cpf_valido:
        return True
    
    return False

