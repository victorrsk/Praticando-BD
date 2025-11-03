import sqlite3
import requests
import json
from pathlib import Path

ROOT_PATH = Path(__file__).parent

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url)

# conectando e criando cursor
conn = sqlite3.connect(ROOT_PATH / 'api_db.db')
conn.execute("PRAGMA foreign_keys = ON")  # ativando chaves estrangeiras
cur = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------

# criando tabela (poucas informações só pra praticar)
# cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name VARCHAR(150), username VARCHAR(150), email VARCHAR(150) UNIQUE)')

# criando tabela de posts
# cur.execute('CREATE TABLE posts (user_id INTEGER REFERENCES users(id), id INTEGER PRIMARY KEY, title VARCHAR(300), body VARCHAR(1000))')

# ---------------------------------------------------------------------------------------------------------------

# inserindo os dados de cada usuário em users_data
# os dados passados pra essa função são os de /users
def post_user(id, name, username, email):
    # dados a serem inseridos
    payload = (id, name, username, email)
    try:
        cur.execute(
            'INSERT INTO users (id, name, username, email) VALUES (?, ?, ?, ?)', payload)
        conn.commit()
    except Exception as exc:
        print(f'err {exc}')
        conn.rollback()

# os dados passados pra essa função são os de /posts
def post_post(user_id, id, title, body):
    payload = (user_id, id, title, body)
    try:
        cur.execute(
            'INSERT INTO posts (user_id, id, title, body) VALUES (?, ?, ?, ?)', payload)
        conn.commit()
    except Exception as exc:
        print(f'err {exc}')
        conn.rollback()


# inserção dos dados no BD


'''posts = response.json()

for post in posts:
    post_post(
            post['userId'],
            post['id'],
            post['title'],
            post['body']
            )'''


'''users_data = response.json()

for user_data in users_data:
    post_user(
            user_data['id'],
            user_data['name'],
            user_data['username'],
            user_data['email']
            )'''
