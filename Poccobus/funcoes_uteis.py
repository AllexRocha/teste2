import pandas as pd
import os
import datetime


# Essa função serve para criar e escrever no arquivos .txt
def escrever_txt(vendidos, assentos, lista_cancel):
    assentos_disp = []
    string = ''
    for i in range(ord('A'), ord('A') + assentos.shape[1]):
        for j in range(1, assentos.shape[0]):
            if assentos.at[j, chr(i)] == '▓':
                assentos_disp.append(chr(i) + str(j))
    try:
            arquivo = open('relacao_assentos.txt')
            string = arquivo.read()
            if string:
                posicao = string.find('=')
                string = string[0:posicao - 1]
                with open('relacao_assentos.txt', 'w') as arquivo:
                    arquivo.write(string)
    except FileNotFoundError as e:
        print(f'{e}:gerando novo arquivo txt ...')

    with open('relacao_assentos.txt', 'a') as arquivo:

        arquivo.write('\n-------------------------------------------------------------------\n')
        data = datetime.datetime.now()
        data_formatada = data.strftime('%d/%m/%Y %H:%M')
        arquivo.write(f'Data e hora: {data_formatada}\n\n')

        if len(vendidos) > 0:
            arquivo.write('Assentos vendidos: ')
            arquivo.write(', '.join(vendidos) + '\n')

        if len(lista_cancel) > 0:
            arquivo.write('Assentos cancelados: ')
            arquivo.write(', '.join(lista_cancel) + '\n')

        arquivo.write('Assentos disponíveis: ' + ', '.join(assentos_disp) + '\n\n')

        arquivo.write("===================================================================\n"
                      "Layout atual da posição dos assentos\n\n"
                      "LEGENDA\n "
                      "\tM: Assento do motorista\n"
                      "\t▒: Assentos disponíveis para compra\n"
                      "\t▓: Assentos disponíveis para compra\n"
                      "\tX: Assentos indisponíveis para compra\n\n")

        arquivo.write('\t\t' + '\t'.join(assentos.columns) + '\n')

        for i in range(0, assentos.shape[0]):
            arquivo.write('\t' + str(i) + '\t')
            for j in range(ord('A'), ord('A') + assentos.shape[1]):
                arquivo.write(assentos.at[i, chr(j)] + '\t')
            arquivo.write('\n\n')


# Essa função serve para renderizar a imagem que representa os acentos do ônibus
def renderizar_imagem(assentos):
    strings = ''
    strings += '\t\t' + '\t'.join(assentos.columns) + '\n'

    for i in range(0, assentos.shape[0]):
        strings += '\t' + str(i) + '\t'
        for j in range(ord('A'), ord('A') + assentos.shape[1]):
            icone = assentos.at[i, chr(j)]
            if icone == 'M':
                icone = '\033[34mM\033[m'
            elif icone == '▒':
                icone = '\033[37m▒\033[m'
            elif icone == '░':
                icone = '\033[33m▒\033[m'
            elif icone == '▓':
                icone = '\033[32m▓\033[m'
            elif icone == 'X':
                icone = '\033[31mX\033[m'
            strings += icone + '\t'
        strings += '\n'

    print("LEGENDA\n "
          "\t\033[34mM\033[m : Assento do motorista\n"
          "\t\033[37m▒\033[m : Corredor e frente do ônibus\n"
          "\t\033[32m▓\033[m : Assentos disponíveis para compra\n"
          "\t\033[33m░\033[m : Assentos selecionado\n"
          "\t\033[31mX\033[m : Assentos indisponíveis para compra\n")

    print(strings)


# cria e configura o layput/matriz dos assentos do ônibus conforme o usuário desejar
def criar_matriz():
    num_linhas = int(input("Indique a quantidade de linhas: "))
    num_colunas = int(input("Indique a quantidade de colunas: "))

    num_corredores = int(input("Quantos corredores você quer que o ônibus tenha: "))

    corredores = []
    for i in range(num_corredores):
        corredores.append(
            int(input(f"Indique o número da {i + 1}ª coluna do corredor vago de 0 a {num_colunas - 1}: ")))

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            if i == 0:
                if j == 0:
                    linha.append('M')
                else:
                    linha.append('▒')
            else:
                if j in corredores:
                    linha.append('▒')
                else:
                    linha.append('▓')
        matriz.append(linha)

    assentos = pd.DataFrame(matriz, columns=criar_colunas(num_colunas))

    return assentos


def criar_colunas(num_colunas):
    colunas = []
    for i in range(ord('A'), ord('A') + num_colunas):
        colunas.append(chr(i))
    return colunas


def cancelar_compra(assentos, vendidos, lista_cancel):
    print('##################### CANCELAR COMPRAS #######################\n')
    renderizar_imagem(assentos)
    try:
        coord = input("\nindique a coordenada do assento desejado ou digite sair para finalizar: ").upper()

        coord_x = coord[0]
        coord_y = coord[1]
        if coord[1].isdigit():
            coord_y = int(coord[1])
        else:
            print('Coordenada do eixo horizontal inválida')

        if coord == 'SAIR':
            pass

        else:
            if len(coord) == 2:

                if assentos.at[coord_y, coord_x] == 'X':
                    assentos.at[coord_y, coord_x] = '▓'
                    input('Compra cancelada. Aperte Enter para continuar...')
                    ler_dados()
                    assentos.to_csv('database.csv', index=False)
                    try:
                        vendidos.remove(coord)
                    except:
                        pass

                    lista_cancel.append(coord)
                    lista_cancel = pd.DataFrame(lista_cancel).transpose()
                    lista_cancel.to_csv('lista_cancel.csv', index=False)
                    if len(vendidos) > 0:
                        vendidos = pd.DataFrame(vendidos).transpose()
                        vendidos.to_csv('vendidos.csv', index=False)
                else:
                    input('A coordenada informada não é de um assento comprado. Aperte Enter para continuar...')
            else:
                input('A coordenada informada não é válida. Aperte Enter para continuar...')

    except (IndexError, ValueError) as e:

        print(f"Erro ao cancelar a compra: {e}")
        input("Aperte qualquer tecla para continuar ...")


def comprar(assentos, vendidos):
    # Selecionando o acento no ônibus. Neste momento o programa entra em um loop para que os assentos sejam selecionados

    while True:

        print('##################### COMPRAR ASSENTOS #######################\n')
        renderizar_imagem(assentos)

        coord = input("\nindique a coordenada do assento desejado ou digite sair para finalizar: ").upper()

        if coord == 'SAIR':
            break

        coord_x = coord[0]
        coord_y = coord[1]
        if coord[1].isdigit():
            coord_y = int(coord[1])
        else:
            print('Coordenada do eixo horizontal inválida')
            input("Aperte qualquer tecla para continuar ...")
            continue
        if not coord_x.isalpha():
            print('Coordenada do eixo vertical inválida')
            input("Aperte qualquer tecla para continuar ...")
            continue
        if coord == 'SAIR':
            break

        if len(coord) == 2:
            if coord_x == 'C' or (ord(coord_x) > (ord('A') + assentos.shape[1] -1)):
                print(f"A coluna {coord_x} não é válida")
                input("Aperte qualquer tecla para continuar ...")
                continue

            if coord_y == 0 or coord_y > assentos.shape[0] -1:
                print(f"A fileira {coord_y} não é válida")
                input("Aperte qualquer tecla para continuar ...")
                continue

            if assentos.at[coord_y, coord_x] == 'X':
                print(f"Infelizmente, o assento {coord} não está disponível\n ")
                while True:
                    opcao = input("Deseja encolher outro acento? S(sim)/ N(não): ").upper()
                    if opcao != 'S' and opcao != 'N':
                        print("Digite uma opção válida")
                        continue
                    break
                if opcao == 'S':
                    continue
                else:
                    break
            else:
                assentos.at[coord_y, coord_x] = '░'
                renderizar_imagem(assentos)
                while True:

                    opcao_1 = input(
                        f"O assento {coord} está disponível ! Deseja fazer a compra ? S(sim)/ N(não): ").upper()
                    if opcao_1 != 'S' and opcao_1 != 'N':
                        print("Digite uma opção válida")
                        continue
                    break
                if opcao_1 == 'S':
                    print(f"Compra do assento {coord} realizada com sucesso !")
                    assentos.at[coord_y, coord_x] = 'X'
                    vendidos.append(coord)

                elif opcao_1 == 'N':
                    assentos.at[coord_y, coord_x] = '▓'
                    while True:
                        opcao_2 = input("Deseja encolher outro assento? S(sim)/ N(não): ").upper()
                        if opcao_2 != 'S' and opcao_2 != 'N':
                            print("Digite uma opção válida")
                            continue
                        break
                    if opcao_2 == 'S':
                        continue
                    else:
                        break

            opcao_3 = input("Deseja finalizar ? S(sim)/ N(não): ").upper()

            if opcao_3 != 'S' and opcao_3 != 'N':
                print("Digite uma opção válida")
                continue
            if opcao_3 == 'N':
                continue
            else:
                break

        else:
            print("coordenada ou opção inválida")
            input("Aperte qualquer tecla para continuar ...")
            continue

    if len(vendidos) > 0:
        vendidos = pd.DataFrame(vendidos).transpose()
        vendidos.to_csv('vendidos.csv', index=False)
        assentos.to_csv('database.csv', index=False)


def ler_dados():
    # Carregamento inicial do programa

    try:
        lista_cancel = pd.read_csv('lista_cancel.csv', index_col=False)
        if len(lista_cancel):
            lista_cancel = lista_cancel.values.tolist()[0]
        else:
            lista_cancel = lista_cancel.values.tolist()

    except:
        lista_cancel = pd.DataFrame([])
        lista_cancel.to_csv('lista_cancel.csv', index=False)
        lista_cancel = lista_cancel.values.tolist()

    try:
        vendidos = pd.read_csv('vendidos.csv', index_col=False)
        if len(vendidos):
            vendidos = vendidos.values.tolist()[0]
        else:
            vendidos = vendidos.values.tolist()



    except:
        vendidos = pd.DataFrame([])
        vendidos.to_csv('vendidos.csv', index=False)
        vendidos = vendidos.values.tolist()

    try:
        assentos = pd.read_csv('database.csv', index_col=False)


    except:

        print('Arquivo não encontrado. Criando e configurando novo layout ...')
        assentos = criar_matriz()
        # criar csv
        assentos.to_csv('database.csv',  index=False)

    return [assentos, vendidos, lista_cancel]


def excluir_arquivo(file):
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)


def finalizar(assentos, vendidos, lista_cancel):
    try:
        escrever_txt(vendidos, assentos, lista_cancel)
        print("Programa Finalizado. Dados registrados")
        excluir_arquivo('vendidos.csv')
        excluir_arquivo('lista_cancel.csv')
    except:
        print("O programa finalizou mas os dados não foram registrados")


def resetar():
    opcao = input("Tem certeza que deseja resetar os dados S(sim)/N(não)?")

    if opcao.isalpha():
        opcao = opcao.upper()
        if opcao == 'S':
            assentos = criar_matriz()
            # criar csv
            assentos.to_csv('database.csv', index = False)
            excluir_arquivo('relacao_assentos.txt')
            input("Sistema resetado. Pressione Enter para continuar ...")
        elif opcao == 'N':
            print('Reset cancelado')

    else:
        print('Opção inválida')
