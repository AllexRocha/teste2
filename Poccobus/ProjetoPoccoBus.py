import pandas as pd
from funcoes_uteis import *

while True:

    print('###############BEM VINDO AO SISTEMA POCCOBUS #######################\n')
    print('Selecione uma das opções:\n ')

    print('\t(1) - Comprar um Assento\n'
          '\t(2) - Cancelar compra\n'
          '\t(10) - Finalizar')




    opcao = int(input())

    if opcao == 1:
        dados = ler_dados()
        dados_vendidos = comprar(dados[0], dados[1])

    elif opcao == 2:
        dados = ler_dados()
        cancelar_compra(dados[0])

    elif opcao == 10:
        dados = ler_dados()
        finalizar(dados[0], dados[1])
        break
