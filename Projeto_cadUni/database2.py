import pyodbc
import datetime
from utils import *


def conectar():

    try:
        server = 'sql-estudo.database.windows.net'
        database = 'db-estudos'
        username = 'alex.rocha@blueshift.com.br'
        Authentication = 'ActiveDirectoryIntegrated'
        driver = '/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.9.so.1.1'   # tive que usar o caminho do driver no meu computador aqui
        string_conexao = F'DRIVER={driver};SERVER=tcp'+server+';PORT=1433;DATABASE='+database+';UID='+username+';AUTHENTICATION='+Authentication+''

        # server = "sql-estudo.database.windows.net,1433"
        # database = "db-estudos"
        # username = "alex.rocha@blueshift.com.br"
        password = "Aa@91293250"
        driver = '/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.9.so.1.1'   # tive que usar o caminho do driver no meu computador aqui
        # string_conexao = f'Driver={driver};Server='+server+';Database='+database+';UID='+username+';PWD='+ password;
        #string_conexao = f'Driver={driver};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'

        conexao = pyodbc.connect(string_conexao)
        return conexao
    except pyodbc.Error as e:
        print(f"Não foi possível se conectar: {e}")

def desconectar(conexao):
    """
    Função para desconectar do servidor.
    """
    if conexao:
        conexao.close()

def inserir(tabela, colunas, valores, parametros):

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = f"INSERT INTO alex_rocha.{tabela} {colunas} VALUES {valores}"

        cursor.execute(sql, parametros)
        conexao.commit()

        if cursor.rowcount == 1:
            resposta = True
        else:
            resposta = False

        desconectar(conexao)
        return resposta

    except pyodbc.Error as e:
        print(f"Erro ao inserir valores {e}")


def buscar(tabela,nome_parametro, parametro):
#     """Faz busca no banco de dados"""

    conexao = conectar()
    cursor = conexao.cursor()

    if nome_parametro == '':
        cursor.execute(
            f"SELECT * FROM alex_rocha.{tabela}")
    else:
        cursor.execute(
            f"SELECT * FROM alex_rocha.{tabela} WHERE {nome_parametro} = {parametro}")

    dados = cursor.fetchall()
    desconectar(conexao)
    if len(dados) > 0:
        return dados
    else:
        print("Dados inexistentes")
        return

def update(tabela, parametros, filtro):
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    sql = f"UPDATE alex_rocha.{tabela} SET {parametros} WHERE {filtro}"
    cursor.execute(sql)

    if cursor.rowcount == 1:
        print('dado atualizado com sucesso.')
    else:
        print(f'Erro ao atualizar o dado com id = {id}')

def delete(tabela, id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM alex_rocha.{tabela} WHERE id = {id}")
    conexao.commit()

    if cursor.rowcount == 1:
        print('dado excluído com sucesso.')
    else:
        print(f'Erro ao excluir o dado com id = {id}')


    desconectar(conexao)

if __name__ == "__main__":
  listar('usuarios')
