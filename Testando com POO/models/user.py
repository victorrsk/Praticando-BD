from database import DataBase


class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.db = DataBase()

    def create_user(self):
        try:
            with self.db.connect() as conn:
                conn.execute(
                    'INSERT INTO users (name, email) VALUES (?, ?)', (self.name, self.email))
                conn.commit()
            print('Usuário criado')
        except Exception as exc:
            print(f'err: {exc}')
            conn.rollback()

    def select_user(self, id):
        with self.db.connect() as conn:
            try:
                response = conn.execute(
                    'SELECT name, email FROM users WHERE id=?', (id,))
                return response.fetchone()

            except Exception as exc:
                print(f'err: {exc}')
                conn.rollback()

    def select_users(self):
        with self.db.connect() as conn:
            try:
                response = conn.execute(
                    'SELECT name, email FROM users')
                return response.fetchall()

            except Exception as exc:
                print(f'err: {exc}')

    def update_user(self, data, id):
        if data.lower() == 'email':
            self.__update_email(id=id)
            return True
        elif data.lower() == 'name':
            self.__update_name(id=id)
            return True
        else:
            print('Dado inválido')
            return False

    def __update_email(self, id):
        new_value = input('Novo email: ')
        with self.db.connect() as conn:
            try:
                conn.execute(
                    'UPDATE users SET email=? WHERE id=?', (new_value, id))
                conn.commit()
                print('Email atualizado')
                return True
            except Exception as exc:
                print(f'err: {exc}')
                conn.rollback()

    def __update_name(self, id):
        new_value = input('Novo nome: ')
        with self.db.connect() as conn:
            try:
                conn.execute(
                    'UPDATE users SET name=? WHERE id=?', (new_value, id))
                conn.commit()
                print('Nome atualizado')
                return True
            except Exception as exc:
                print(f'err: {exc}')
                conn.rollback()

    def delete_user(self, id):
        with self.db.connect() as conn:
            try:
                conn.execute('DELETE FROM users WHERE id=?', (id,))
                conn.commit()
                print('Registro apagado')
                return True
            except Exception as exc:
                print(f'err: {exc}')
                conn.rollback()