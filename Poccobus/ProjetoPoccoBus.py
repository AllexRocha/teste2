import pandas as pd
from funcoes_uteis import *

while True:

    print('###############BEM VINDO AO SISTEMA POCCOBUS #######################\n')
    print('Selecione uma das opções:\n\n ')

    print('(1) - Comprar um Assento')

    print('(10) - Finalizar')

    opcao = int(input())

    if opcao == 1:
        dados = ler_dados()
        dados_vendidos = comprar(dados[0], dados[1])

    if opcao == 10:
        dados = ler_dados()
        finalizar(dados[0], dados[1])
        break
