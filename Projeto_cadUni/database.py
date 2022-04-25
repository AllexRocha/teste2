import pyodbc


def conectar():
    try:

        # #Conexão remota
        # server = 'sql-estudo.database.windows.net'
        # database = 'db-estudos'
        # username = 'alex.rocha@blueshift.com.br'
        # Authentication = 'ActiveDirectoryInteractive'
        # string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';AUTHENTICATION='+Authentication+''

        # Coneão local
        server = "localhost"
        database = "master"
        username = "alex.rocha@blueshift.com.br"
        password = "Aa@91293250"
        string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
        ## string_conexao = f'Driver={driver};Server='+server+';Database='+database+';UID='+username+';PWD='+ password;

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


def inserir(conn, tabela, colunas, valores, parametros):
    cursor = conn.cursor()
    try:
        sql = f"INSERT INTO alex_rocha.{tabela} {colunas} VALUES {valores}"

        cursor.execute(sql, parametros)
        conn.commit()

        if cursor.rowcount == 1:
            resposta = True
        else:
            resposta = False

        # desconectar(conexao)
        return resposta

    except pyodbc.Error as e:
        print(f"Erro ao inserir valores {e}")


def buscar(conn, tabelas, tabelas_param, nome_parametro, parametro, opcao):
    #     """Faz busca no banco de dados"""

    # opcao 0 : busca toda a tabela sem filtro
    # opcao 1: busca específica de parâmetro
    # opcao 2: busca entre tabelas relacionadas

    cursor = conn.cursor()

    try:
        if opcao == 0:
            cursor.execute(
                f"SELECT * FROM alex_rocha.{tabelas}")
        elif opcao == 1:
            cursor.execute(
                f"SELECT * FROM alex_rocha.{tabelas} WHERE {nome_parametro} = {parametro}")
        elif opcao == 2:
            cursor.execute(
                f"SELECT {tabelas_param} FROM {tabelas} WHERE {nome_parametro} = {parametro}")

        dados = cursor.fetchall()

        if len(dados) > 0:
            return dados
        else:
            return False

    except pyodbc.Error as e:
        print(f"Erro na leitura do banco de dados: {e}")


def update(conn, tabela, parametros, filtro):
    """
    Função para atualizar um produto
    """
    cursor = conn.cursor()

    sql = f"UPDATE alex_rocha.{tabela} SET {parametros} WHERE {filtro}"
    cursor.execute(sql)
    conn.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False


def delete(conn, tabela, id):
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM alex_rocha.{tabela} WHERE id = {id}")
    conn.commit()

    if cursor.rowcount == 1:
        return True
    else:
        return False
