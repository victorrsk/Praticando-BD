import re

def validar_nome(nome):
    nome_pattern = r'[a-zA-Z]{3,}\s*'
    if len(nome) > 150:
        print('Nome muito extenso')
        return False
    
    elif re.fullmatch(nome_pattern, nome):
            return True
    
    print('Nome inválido')
    return False

def validar_email(email):
    email_pattern = r'[a-zA-Z]{2,}[0-9]{3,}((@gmail.com){1}$)'
    
    if len(email) > 150:
        print('email muito extenso')
        return False
    
    elif re.fullmatch(email_pattern, email):
        return True
    
    print('email inválido')
    return False

def validar_cpf(cpf):