import pyodbc
import datetime

d1 = '05/09/1993'
data_nasc = datetime.datetime.strptime(d1, "%d/%m/%Y")
data_atual = datetime.datetime.now()

anos = abs((data_atual - data_nasc).days)/365
print(anos)