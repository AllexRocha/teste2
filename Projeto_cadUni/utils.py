"""funções úteis"""
import datetime
import pandas as pd
from classes import Usuario, Motorista, Onibus, Cartao
from database import buscar, delete, update


def formatar_data(data, opcao):
    if opcao == 0:  # para enviar ao banco de dados
        try:
            return datetime.datetime.strptime(data, "%d/%m/%Y").date()
        except:
            print("O formato de data não está correto")

    if opcao == 1:  # para formatar a data recebida do banco de dados
        try:
            return datetime.datetime.strptime(data, "%Y-%m-%d").date().strftime('%d/%m/%Y')
        except:
            print("Erro ao converter a data")


def cadastrar_usuario(conexao):
    nome = input("Insira o nome do usuário: ")
    sobrenome = input("Insira o sobrenome do usuário: ")
    email = input("Insira o e-mail do usuário: ")
    bairro = input("Insira o bairro do usuário: ")
    data = input("Informe a data de nascimento no formato dd/mm/yyyy: ")
    data_nascimento = formatar_data(data, 0)

    usuario = Usuario(nome, sobrenome, data_nascimento, email, bairro)
    usuario.inserirUsuario(conexao)


def cadastrar_motorista(conn):
    nome = input("Insira o nome do motorista: ")
    sobrenome = input("Insira o sobrenome do motorista: ")
    numero_cnh = input("Insira a cnh do motorista: ")
    data = input("Informe a data de nascimento no formato dd/mm/yyyy: ")
    data_nascimento = formatar_data(data, 0)

    motorista = Motorista(nome, sobrenome, data_nascimento, numero_cnh)
    motorista.inserirMotorista(conn)


def cadastrar_onibus(conn):
    numero_placa = int(input("Informe o número da placa do veículo: "))
    numero_linha = int(input("Informe o número da linha do veículo: "))
    modelo_do_onibus = input("Informe o modelo do ônibus: ")
    data = input("Informe o ano de fabricação do ônibus: ")
    ano_de_fabricacao = formatar_data('01/01/' + data, 0)
    Motorista.listar_motoristas(conn)
    num_cnh = int(input("\nInforme o número da cnh do motorista do ônibus: "))
    id_motorista = buscar(conn, 'motoristas', '', 'numero_cnh', num_cnh, 1)

    if id_motorista:
        onibus = Onibus(numero_placa, numero_linha, modelo_do_onibus, ano_de_fabricacao, id_motorista[0][0])
        onibus.inserir_onibus(conn)
    else:
        print(f"O motorista com o númedo da cnh:{num_cnh} não foi encontrado")


def cadastrar_cartao(conn):
    global id_usuario
    cartao_existe = False
    qtd_creditos = float(input("Insira a quantidade de créditos disponível: "))
    while True:
        print('\n\t(1) - Comum\n'
              '\t(2) - Estudante\n'
              '\t(3) - Vale-Transporte\n'
              '\t(4) - Idoso\n')
        opcao = input("Selecione o tipo do cartão: ")
        if opcao.isdigit():
            opcao = int(opcao)

        if opcao == 1:
            tipo = 'Comum'
            break
        elif opcao == 2:
            tipo = 'Estudante'
            break
        elif opcao == 3:
            tipo = 'Vale-Tranporte'
            break
        elif opcao == 4:
            tipo = 'Idoso'
            break
        else:
            print('Opção inválida')

    data_emissao = datetime.datetime.now().date()
    listar(conn, 'usuarios')
    id = input("\nInforme o ID do usuário ao qual o cartão irá pertencer: ")

    if id.isdigit():
        id = int(id)
        usuarios = buscar(conn, 'usuarios', '', 'id', f"{id}", 1)

        if not (usuarios):
            print("Não existe usuário cadastrado com o id informado")
        else:
            id_usuario = usuarios[0][0]
            cartao = Cartao(id_usuario, qtd_creditos, tipo, data_emissao)
            cartao.inserir_cartao(conn)

    else:
        print('ID inválido')





def atualizar(conn, tabela):
    listar(conn, tabela)

    id = input("\n\nInforme o ID do dado a ser atualizado: ")

    if id.isdigit() and len(id) == 1:
        id = int(id)

        dado = buscar(conn, tabela, '', 'id', id, 1)
        if dado:
            if tabela == 'usuarios':
                usuario = Usuario(dado[0][1], dado[0][2], dado[0][3], dado[0][4], dado[0][5])
                usuario.atualizar(conn, tabela, id)

            elif tabela == 'cartoes':
                cartao = Cartao(dado[0][0], dado[0][1], dado[0][2], dado[0][3])
                cartao.atualizar(conn, tabela, id)
            elif tabela == 'motoristas':
                motorista = Motorista(dado[0][0], dado[0][1], dado[0][2], dado[0][3])
                motorista.atualizar(conn, tabela, id)
            elif tabela == 'onibus':
                onibus = Onibus(dado[0][0], dado[0][1], dado[0][2], dado[0][3], dado[0][4])
                onibus.atualizar(conn, tabela, id)

        else:
            print("Dado inexistente")

    else:
        print("entrada inválida")


def deletar(conn, tabela):
    global motorista, att
    listar(conn, tabela)

    id = input("\n\nInforme o ID do dado a ser deletado: ")

    if id.isdigit() and len(id) == 1:
        id = int(id)

        if buscar(conn, tabela, '', 'id', id, 1):
            print("O registro será excluído junto com todos os registros relacionados. Deseja continuar ?")
            while True:
                opcao = input("Digite S(sim)/N(não): ").upper()

                if opcao == 'S' or opcao == 'N':
                    if opcao == 'S':
                        if tabela == 'usuarios':
                            dados = buscar(conn, 'cartoes', '', 'id_usuario', id, 1)
                            if dados:
                                delete(conn, 'cartoes', dados[0][0])
                            if delete(conn, tabela, id):
                                print('Dados deletados')
                            else:
                                print('Não foi possível deletar')
                            break

                        elif tabela == 'motoristas':
                            dados = buscar(conn, 'onibus', '', 'id_motorista', id, 1)
                            if dados:
                                print("Há um ou mais ônibus vinculados a este motorista,"
                                      " por favor selecione um novo motorista para vincular ou altere manualmente \n")

                                while True:
                                    Motorista.listar_motoristas(conn)
                                    id_motorista = input(
                                        f"\nInforme o id do novo motorista para vincular ao ônibus"
                                        f"ou digite (sair): ")
                                    if id_motorista.isdigit():
                                        motorista = buscar(conn, 'motoristas', '', 'id', id_motorista, 1)

                                        if motorista:
                                            motorista = motorista[0]

                                            if motorista[0] == id:
                                                print("O id não pode ser o mesmo do motorista a ser deletado !")
                                                continue
                                            else:
                                                att = update(conn, 'onibus', f"id_motorista = {motorista[0]}",
                                                             f"id_motorista = {id}")
                                                break
                                        else:
                                            print('Não foram encontrados dados do motorista indicado')
                                            continue

                                    elif id_motorista == 'sair':
                                        att = False
                                        break
                                if att:
                                    delete(conn, tabela, id)
                                    print('Dados deletados')
                                    break
                                else:
                                    print("Não foi possível deletar")
                                    break



                            else:
                                if delete(conn, tabela, id):
                                    print('Dados deletados')
                                else:
                                    print('Não foi possível deletar')
                                break


                        elif tabela == 'cartoes':
                            if delete(conn, tabela, id):
                                print('Dados deletados')
                            else:
                                print('Não foi possível deletar')
                            break


                        elif tabela == 'onibus':
                            if delete(conn, tabela, id):
                                print('Dados deletados')
                            else:
                                print('Não foi possível deletar')
                            break


                        else:
                            print("A tabela indicada não existe no banco de dados. nenhum dado foi deletado")
                            break

                    else:
                        print("Os dados NÃO foram deletados")
                        break

                else:
                    print("opção inválida")

        else:
            print("O dado indicado não existe no banco de dados")

    else:
        print('Entrada inválida')


def listar(conn, tabela):
    dados = buscar(conn, tabela, '', '', '', 0)

    if tabela == 'usuarios':
        Usuario.listar_usuarios(conn)
    elif tabela == 'motoristas':
        Motorista.listar_motoristas(conn)
    elif tabela == 'cartoes':
        Cartao.listar_cartoes(conn)
    elif tabela == 'onibus':
        Onibus.listar_onibus(conn)


def listar_especial(conn, opcao):
    if opcao == 1:
        tabelas_param = 'usuarios.nome, usuarios.sobrenome, usuarios.data_nascimento, cartoes.qtd_creditos_disponivel,' \
                        'cartoes.tipo, cartoes.data_de_emissao'
        tabelas = 'alex_rocha.usuarios, alex_rocha.cartoes'
        nome_param = 'id_usuario'
        parametro = 'usuarios.id'

        dados = buscar(conn, tabelas, tabelas_param, nome_param, parametro, 2)
        if dados:
            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-1] = datetime.datetime.strptime(f'{dado[-1]}', "%Y-%m-%d").date().strftime('%d/%m/%Y')
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista, columns=['|  Nome  |', '| Sobrenome |', '|Data de Nascimento|',
                                                    '|Qtd de crétditos|', '|     Tipo    |', '|Data de Emissão|'])

            print(df.to_string(index=False))
        else:
            print("Não há dados")

    elif opcao == 2:
        tabelas_param = 'motoristas.nome, motoristas.sobrenome, motoristas.numero_cnh, onibus.numero_da_placa,' \
                        'onibus.numero_da_linha, onibus.modelo_do_onibus, onibus.ano_de_fabricacao'
        tabelas = 'alex_rocha.motoristas, alex_rocha.onibus'
        nome_param = 'id_motorista'
        parametro = 'motoristas.id'

        dados = buscar(conn, tabelas, tabelas_param, nome_param, parametro, 2)
        if dados:

            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-1] = datetime.datetime.strptime(f'{dado[-1]}', "%Y-%m-%d").date().year
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista, columns=['| Nome |', '|  Sobrenome  |', '|Nº da CNH|',
                                                    '|Nº da placa|', '|Nº da linha|', '|Modelo do ônibus|',
                                                    '|Ano de fabricação|'])

            print(df.to_string(index=False))
        else:
            print("Não há dados")
