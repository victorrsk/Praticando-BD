import sqlite3
from pathlib import Path
from utils import validar_cpf, validar_dados, validar_email

ROOT_PATH = Path(__file__).parent

# conecta o BD
conn = sqlite3.connect(ROOT_PATH / 'praticando.db')
# cria o cursor
cursor = conn.cursor()
# para listar os registros melhor
cursor.row_factory = sqlite3.Row


def inserir_registro(dados):
    try:
        cursor.execute(
            'INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)', dados)
        conn.commit()
        print('Usuário inserido com sucesso!')
    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')
        conn.rollback()


def inserir_registros(lista_dados):
    try:
        cursor.executemany(
            'INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)', lista_dados)
        conn.commit()
    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')
        cursor.rollback()


def atualizar_registro(id, atributo):
    try:
        if atributo.upper() == 'NOME':
            novo = input('Novo nome: ')
            cursor.execute('UPDATE usuarios SET nome=? WHERE id=?', (novo, id))

        elif atributo.upper() == 'EMAIL':
            novo = input('Novo email: ')
            cursor.execute(
                'UPDATE usuarios SET email=? WHERE id=?', (novo, id))

        else:
            print('Atributo inexistente ou não pode ser alterado')
            return False
        conn.commit()
        print(f'{atributo} atualizado com sucesso!')

    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')
        conn.rollback()


def excluir_registro(id):
    try:
        cursor.execute('DELETE FROM usuarios WHERE id=?', (id,))
        conn.commit()
        print('Registro excluido com sucesso!')
    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')
        conn.rollback()

def listar_registros():
    try:
        cursor.execute('SELECT * FROM usuarios')
        registros = cursor.fetchall()
        for usuario in registros:
            print(f'NOME: {usuario['nome']}\tEMAIL: {usuario['email']}')
    except Exception as exc:
        print(f'Ocorreu algum erro: {exc}')

