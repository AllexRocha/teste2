import pyodbc
import datetime

ano = input()
ano2 = datetime.datetime.strptime('1/1/' + ano, "%d/%m/%Y").date()
print(ano2)