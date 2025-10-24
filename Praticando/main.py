from db_utils import inserir_registro, inserir_registros, atualizar_registro, excluir_registro, listar_registros
from utils import validar_dados
from interface import menu
from time import sleep

lista_dados = []

while True:
    menu()
    escolha = input('Sua escolha: ')

    if escolha == '1':
        nome = input('Seu nome: ')
        email = input('Seu email: ')
        cpf = input('Seu CPF: ')
        if validar_dados(nome, email, cpf):
            dados = (nome, email, cpf)
            inserir_registro(dados)

    elif escolha == '2':
        while True:
            nome = input('Seu nome: ')
            email = input('Seu email: ')
            cpf = input('Seu CPF: ')
            if validar_dados(nome, email, cpf):
                lista_dados.append((nome, email, cpf))
                print('Usuário cadastrado')
            continuar = input('Continuar? [S/N]').upper().strip()
            if continuar == 'N':
                inserir_registros(lista_dados)
                break
            elif continuar != 'S':
                print('Nenhuma resposta foi dada, continuando...')

    elif escolha == '3':
        # o sqlite nao da erro com a busca por id's que não existam
        id = input('id do registro que deseja atualizar: ')
        atributo = input('Atributo que quer atualizar [nome/email]: ')
        atualizar_registro(id, atributo)
    elif escolha == 'q':
        print('Finalizando...')
        sleep(3)
        print('Execução finalizada')
        break
    
    elif escolha == '4':
        id = input('id do registro que deseja excluir: ')
        excluir_registro(id)
    
    elif escolha == '5':
        listar_registros()

    else:
        print('Opção inválida')