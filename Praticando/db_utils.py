import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

def conectar_db(conexao):
    conn = sqlite3.connect(ROOT_PATH / conexao)
    if conn:
        print('Banco conectado')
        return True
