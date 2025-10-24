import sqlite3
from pathlib import Path

# caminho do diretório atual
ROOT_PATH = Path(__file__).parent

# conectando ao BD
conn = sqlite3.connect(ROOT_PATH / 'praticando.db')
# criando o cursor
cursor = conn.cursor()

nome = input('Seu nome: ')
email = input('Seu email: ')
cpf = input('Seu CPF: ')

data = (nome, email, cpf)

cursor.execute('INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)', data)