from database import conectar, desconectar
from utils import listar, listar_especial, atualizar, deletar
from utils import cadastrar_usuario, cadastrar_cartao, cadastrar_onibus, cadastrar_motorista

# Fazendo a conexão com o banco de dados
conn = conectar()

while True:
    print("########################* Sistema de cadastro CADUni *#########################")

    print('\n\t(1) - Cadastrar dados\n'
          '\t(2) - Listar dados\n'
          '\t(3) - Atualizar dados\n'
          '\t(4) - Deletar dados\n'
          '\t(5) - Finalizar o programa\n')

    opcao = input('\n\tIndique uma opção: ')
    print('\n')

    if opcao.isdigit():
        opcao = int(opcao)
    else:
        input('opção inválida. continuar ...')
        continue

    if opcao == 1:
        print('\n################ * Cadastrar dados * ##############\n')

        print('\n\t(1) - Cadastrar Usuários\n'
              '\t(2) - Cadastrar Motoristas\n'
              '\t(3) - Cadastrar Cartões\n'
              '\t(4) - Cadastrar Ônibus\n'
              '\t(5) - Retornar\n')

        opcao = input('\n\tIndique uma opção desejada: ')

        print('\n')

        if opcao.isdigit():
            opcao = int(opcao)
        else:
            input('opção inválida. continuar ...')
            continue

        if opcao == 1:
            print('\n################ * Cadastrar Usuário * ##############\n')
            cadastrar_usuario(conn)
            input("\nPressione Enter para continuar ...")

        elif opcao == 2:
            print('\n################ * Cadastrar Motorista * ##############\n')
            cadastrar_motorista(conn)
            input("\nPressione Enter para continuar ...")
        elif opcao == 3:
            print('\n################ * Cadastrar Cartão * ##############\n')
            cadastrar_cartao(conn)
            input("\nPressione Enter para continuar ...")
        elif opcao == 4:
            print('\n################ * Cadastrar Ônibus * ##############\n')
            cadastrar_onibus(conn)
            input("\nPressione Enter para continuar ...")
        elif opcao == 5:
            continue



    elif opcao == 2:
        print('\n################ * listar dados * ##############\n')

        print('\n\t(1) - Listar Usuários\n'
              '\t(2) - Listar Motoristas\n'
              '\t(3) - Listar Cartões\n'
              '\t(4) - Listar Ônibus\n'
              '\t(5) - Listar usuários e cartões\n'
              '\t(6) - listar Motoristas e ônibus\n'
              '\t(7) - Retornar\n')

        opcao = input('\n\tIndique a opção desejada: ')

        print('\n')

        if opcao.isdigit():
            opcao = int(opcao)
        else:
            input('opção inválida. continuar ...')
            continue

        if opcao == 1:
            print('\n################################## * Listando Usuários * #################################\n')
            listar(conn, 'usuarios')
            input("Pressione Enter para continuar ...")
        elif opcao == 2:
            print('\n################################## * Listando Motoristas * ##################################\n')
            listar(conn, 'motoristas')
            input("\nPressione Enter para continuar ...")
        elif opcao == 3:
            print('\n################################## * Listando Cartões * ##################################\n')
            listar(conn, 'cartoes')
            input("\nPressione Enter para continuar ...")
        elif opcao == 4:
            print('\n################################## * Listando Ônibus * ##################################\n')
            listar(conn, 'onibus')
            input("\nPressione Enter para continuar ...")

        elif opcao == 5:
            print('\n################################## * Listando Usuários e cartões * ##################################\n')
            listar_especial(conn, 1)
            input("\nPressione Enter para continuar ...")
        elif opcao == 6:
            print('\n################################## * Listando Motoristas e ônibus * ##################################\n')
            listar_especial(conn, 2)
            input("\nPressione Enter para continuar ...")

        elif opcao == 7:
            continue

    elif opcao == 3:
        print('\n################ * Atualizar dados * ##############\n')

        print('\n\t(1) - Atualizar Usuário\n'
              '\t(2) - Atualizar Motorista\n'
              '\t(3) - Atualizar Cartão\n'
              '\t(4) - Atualizar Ônibus\n'
              '\t(5) - Retornar\n')

        opcao = input('\n\tIndique a opção desejada: ')

        print('\n')

        if opcao.isdigit():
            opcao = int(opcao)
        else:
            input('opção inválida. continuar ...')
            continue

        if opcao == 1:
            print('\n################ * Atualizando Usuário * ##############\n')
            atualizar(conn, 'usuarios')
            input("Pressione Enter para continuar ...")
        elif opcao == 2:
            print('\n################ * Atualizando Motorista * ##############\n')
            atualizar(conn, 'motoristas')
            input("\nPressione Enter para continuar ...")
        elif opcao == 3:
            print('\n################ * Atualizando Cartão * ##############\n')
            atualizar(conn, 'cartoes')
            input("\nPressione Enter para continuar ...")
        elif opcao == 4:
            print('\n################ * Atualizando Ônibus * ##############\n')
            atualizar(conn, 'onibus')
            input("\nPressione Enter para continuar ...")
        elif opcao == 5:
            continue

    elif opcao == 4:
        print('\n################ * Deletar dados * ##############\n')

        print('\n\t(1) - Deletar Usuário\n'
              '\t(2) - Deletar Motorista\n'
              '\t(3) - Deletar Cartão\n'
              '\t(4) - Deletar Ônibus\n'
              '\t(5) - Retornar\n')

        opcao = input('\n\tIndique a opção desejada: ')

        print('\n')

        if opcao.isdigit():
            opcao = int(opcao)
        else:
            input('opção inválida. continuar ...')
            continue

        if opcao == 1:
            print('\n################################### * Deletando Usuário * ##############################\n')
            deletar(conn, 'usuarios')
            input("Pressione Enter para continuar ...")
        elif opcao == 2:
            print('\n################ * Deletando Motorista * ##############\n')
            deletar(conn, 'motoristas')
            input("\nPressione Enter para continuar ...")
        elif opcao == 3:
            print('\n################ * Deletando Cartão * ##############\n')
            deletar(conn, 'cartoes')
            input("\nPressione Enter para continuar ...")
        elif opcao == 4:
            print('\n################ * Deletando Ônibus * ##############\n')
            deletar(conn, 'onibus')
            input("\nPressione Enter para continuar ...")
        elif opcao == 5:
            continue

    elif opcao == 5:
        print('Programa finalizado')
        desconectar(conn)
        break
