from models.user import User

teste = User('lucas', 'lucasteste@gmail.com')

# teste de consulta geral
usuarios = teste.select_users()
print(usuarios)

# teste de consulta única
usuario = teste.select_user(3)
print(usuario)

# teste de upd nome
teste.update_user('name', 2)

# teste de upd email
teste.update_user('email', 3)

# teste de delete
teste.delete_user(2)
