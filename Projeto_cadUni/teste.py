import pyodbc
import datetime
parametros = ['','','','','','']
sobrenome = 'testetse'
n =parametros[2].find('sobrenome=')
while True:
    if not (parametros.find('sobrenome=') +1):
        # del(parametros[2])
        parametros.insert(1, f"sobrenome='{sobrenome}'")


