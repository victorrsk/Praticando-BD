from db_utils import criar_cursor, inserir_registro
from utils import validar_dados

cursor = criar_cursor()

# dados para inserir no BD
nome = input('Seu nome: ')
email = input('Seu email: ')
cpf = input('Seu CPF: ')

# validação dos dados com regex simples
dados_validos = validar_dados(nome, email, cpf)

if dados_validos:
    dados_registro = (nome, email, cpf)
    inserir_registro(cursor, dados_registro)