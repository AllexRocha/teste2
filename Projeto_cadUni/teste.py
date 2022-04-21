import pyodbc

import pyodbc
server = 'sql-estudo.database.windows.net'
driver = '{ODBC Driver 17' \
         ' for SQL Server}'
database = 'db-estudos'
username = 'alex.rocha@blueshift.com.br'
Authentication='ActiveDirectoryInteractive'
port = '1433'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)#+';PWD='+password)
conexao = pyodbc.connect(conn)
print(conexao)