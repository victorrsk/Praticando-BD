from db_utils import inserir_registro, inserir_registros, atualizar_registro
from utils import validar_dados

# dados para inserir no BD
'''nome = input('Seu nome: ')
email = input('Seu email: ')
cpf = input('Seu CPF: ')'''

# validação dos dados com regex simples
# dados_validos = validar_dados(nome, email, cpf)

# if dados_validos:
# dados_registro = (nome, email, cpf)
# inserir_registro(dados_registro)

registros = []

'''while (resp := input('Resposta: ') != 'q'):
    nome = input('Seu nome: ')
    email = input('Seu email: ')
    cpf = input('Seu CPF: ')
    if validar_dados(nome, email, cpf):
        registros.append((nome, email, cpf))'''

print(registros)
inserir_registros(registros)
