import pandas as pd
import os


with open('texto.txt', 'r+') as arquivo:
    texto = arquivo.read()
    arquivo.write('\nafdafsggfdbgdb')
    print(texto)

# with open('texto.txt', 'a') as arquivo:
#     arquivo.write('asdsdfdddfdsf')
# file = 'vendidos.csv'
# if (os.path.exists(file) and os.path.isfile(file)):
#     os.remove(file)
#     print("file deleted")
# else:
#     print("file not found")

# v = pd.DataFrame([])
#
# v.to_csv('v.csv', index=False)
#
#
# v = v.values.tolist()[0]
#
# v.append('A1')
# v.append('B5')
#
# v = pd.DataFrame(v).transpose()
# v.to_csv('v.csv', index=False)

# v2 = pd.read_csv('v.csv', index_col=False)
#
# v2 = v2.values.tolist()[0]
# v2.append('C5')
# v2.append('E4')
#
# v2 = pd.DataFrame(v2).transpose()
# v2.to_csv('v2.csv', index=False)

#
# with open('relacao_assentos.txt', 'r') as arquivo:
#
#     string = arquivo.read()
#
#     print(string.find("="))
#
#     string = string[0:102]
#     print(string)