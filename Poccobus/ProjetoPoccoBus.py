import pandas as pd
from funcoes_uteis import *

try:
    excluir_arquivo('vendidos.csv')
    excluir_arquivo('lista_cancel.csv')
except:
    pass

while True:

    print('###############BEM VINDO AO SISTEMA POCCOBUS #######################\n')

    print('\t(1) - Comprar um Assento\n'
          '\t(2) - Cancelar compra\n'
          '\t(3) - Resetar o sistema\n'
          '\t(4) - Finalizar')

    opcao = input('\n\nSelecione uma das opções:')

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

