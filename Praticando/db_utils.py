import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# conecta o BD
conn = sqlite3.connect(ROOT_PATH / 'praticando.db')

def criar_cursor():
    return conn.cursor()

def inserir_registro(cursor, dados):
    try:
        cursor.execute('INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)', dados)
        conn.commit()
        print('Usuário inserido com sucesso!')
    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')
        conn.rollback()




