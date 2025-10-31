import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

class DataBase:
    
    def __init__(self, db_name='testando.db'):
        self.db_name = db_name
    
    def connect(self):
        return sqlite3.connect(ROOT_PATH / self.db_name)
    
    def create_table(self):
        with self.connect() as conn:
            conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(155), email VARCHAR(100) UNIQUE)')

if __name__ == '__main__':
    teste = DataBase()
    teste.connect()
