import pandas as pd
from funcoes_uteis import *

try:
    excluir_arquivo('vendidos.csv')
    excluir_arquivo('lista_cancel.csv')
except:
    pass

while True:

    print('###############BEM VINDO AO SISTEMA POCCOBUS #######################\n')
<<<<<<< HEAD
=======
    print('Selecione uma das opções:\n ')
>>>>>>> ceb1a8ed435b13d387ac2046bf8f2fa82ab2a09b

    print('\t(1) - Comprar um Assento\n'
          '\t(2) - Cancelar compra\n'
          '\t(10) - Finalizar')


<<<<<<< HEAD

=======
    print('\t(1) - Comprar um Assento\n'
          '\t(2) - Cancelar compra\n'
          '\t(3) - Resetar o sistema\n'
          '\t(4) - Finalizar')

<<<<<<< HEAD
    opcao = input('\n\nSelecione uma das opções:')
=======
    opcao = input()
>>>>>>> origin/master
>>>>>>> ceb1a8ed435b13d387ac2046bf8f2fa82ab2a09b

    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            dados = ler_dados()
            dados_vendidos = comprar(dados[0], dados[1])
        elif opcao == 2:
            dados = ler_dados()
            cancelar_compra(dados[0], dados[1], dados[2])
        elif opcao == 3:
            resetar()
        elif opcao == 4:
            dados = ler_dados()
            finalizar(dados[0], dados[1], dados[2])
            break
    else:
        print('Opção inválida')

<<<<<<< HEAD
    elif opcao == 2:
        dados = ler_dados()
        cancelar_compra(dados[0])

    elif opcao == 10:
        dados = ler_dados()
        finalizar(dados[0], dados[1])
        break
=======
>>>>>>> origin/master
