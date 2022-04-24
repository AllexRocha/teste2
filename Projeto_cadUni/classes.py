from database import inserir, update, buscar
import pandas as pd
from datetime import  datetime



class Pessoa:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self.__sobrenome = valor

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self.__data_nascimento = valor


class Usuario(Pessoa):
    def __init__(self, nome, sobrenome, data_nascimento, email, bairro):
        super().__init__(nome, sobrenome, data_nascimento)
        self.__email = email
        self.__bairro = bairro

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, valor):
        self.__bairro = valor

    def inserirUsuario(self, conexao):

        tabela = 'usuarios'
        colunas = '(nome, sobrenome, email, bairro, data_nascimento)'
        valores = '(?, ?, ?, ?, ?)'
        parametros = (self.nome, self.sobrenome, self.email, self.bairro, self.data_nascimento)

        retorno = inserir(conexao, tabela, colunas, valores, parametros)

        if retorno:
            print(f"O(A) usuário(a) {self.nome} {self.sobrenome} foi cadastrado(a) com sucesso.")
        else:
            print("Erro ao cadastrar usuário")

    def atualizar(self, conn, tabela, id):

        parametros = []
        filtro = f'id={id}'
        while True:
            print("indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):\n"
                  "\t1 - nome"
                  "\t2 - sobrenome"
                  "\t3 - email"
                  "\t4 - bairro"
                  "\t5 - data_nascimento"
                  "\t6 - (sair)\n")
            opcao = input()
            if opcao.isdigit():
                opcao = int(opcao)

            if opcao == 1:
                self.nome = input("Digite o novo nome: ")
                if not ('nome=?' in parametros):
                    parametros.insert(0, f"nome='{self.nome}'")

            elif opcao == 2:
                self.sobrenome = input("Digite o novo sobrenome: ")
                if not ('sobrenome=?' in parametros):
                    parametros.insert(1, f"sobrenome='{self.sobrenome}'")

            elif opcao == 3:
                self.email = input("Digite o novo e-mail: ")
                if not ('email=?' in parametros):
                    parametros.insert(2, f"email='{self.email}'")

            elif opcao == 4:
                self.bairro = input("Digite o novo bairro: ")
                if not ('bairro=?' in parametros):
                    parametros.insert(3, f"bairro='{self.bairro}'")

            elif opcao == 5:
                data = input("Informe a nova data de nascimento no formato dd/mm/yyyy: ")
                self.data_nascimento = datetime.strptime(data, "%d/%m/%Y").date()
                if not ('data_nascimento=?' in parametros):
                    parametros.insert(4, f"data_nascimento='{self.data_nascimento}'")

            elif opcao == 6:
                break

            else:
                print("opção inválida")

        if len(parametros):
            parametros = ','.join(parametros)

            status = update(conn, tabela, parametros, filtro)
            if status:
                print("Usuário atualizado com sucesso")
            else:
                print("Não foi possível atualizar o usuário")

    @staticmethod
    def listar_usuarios(conn):

        dados = buscar(conn, 'usuarios', '', '', '', 0)
        if dados:
            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-1] = datetime.strptime(f'{dado[-1]}', "%Y-%m-%d").date().strftime('%d/%m/%Y')
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista, columns=['|id|', '|  Nome  |', '|  Sobrenome  |', '|    E-mail   |',
                                                    '|     Bairro     |', '|Data de nascimento|'])
            print(df.to_string(index=False))
        else:
            print("Não há dados")


class Motorista(Pessoa):
    def __init__(self, nome, sobrenome, data_nascimento, num_cnh):
        super().__init__(nome, sobrenome, data_nascimento)
        self.__num_cnh = num_cnh

    @property
    def num_cnh(self):
        return self.__num_cnh

    @num_cnh.setter
    def num_cnh(self, valor):
        self.__num_cnh = valor

    def inserirMotorista(self, conn):

        tabela = 'motoristas'
        colunas = '(numero_cnh, nome, sobrenome, data_nascimento)'
        valores = '(?, ?, ?, ?)'
        parametros = (self.num_cnh, self.nome, self.sobrenome, self.data_nascimento)

        retorno = inserir(conn, tabela, colunas, valores, parametros)

        if retorno:
            print(f"O(A) motorista(a) {self.nome} {self.sobrenome} foi cadastrado(a) com sucesso.")
        else:
            print("Erro ao cadastrar motorista")

    def atualizar(self, conn, tabela, id):

        parametros = []
        filtro = f'id={id}'
        while True:
            print("indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):\n"
                  "\t1 - nome"
                  "\t2 - sobrenome"
                  "\t3 - numero_cnh"
                  "\t4 - data_nascimento"
                  "\t5 - (sair)\n")
            opcao = input()
            if opcao.isdigit():
                opcao = int(opcao)

            if opcao == 1:
                self.nome = input("Digite o novo nome: ")
                if not ('nome=?' in parametros):
                    parametros.insert(0, f"nome='{self.nome}'")

            elif opcao == 2:
                self.sobrenome = input("Digite o novo sobrenome: ")
                if not ('sobrenome=?' in parametros):
                    parametros.insert(1, f"sobrenome='{self.sobrenome}'")

            elif opcao == 3:
                self.num_cnh = input("Digite o novo número da cnh: ")
                if not ('numero_cnh=?' in parametros):
                    parametros.insert(2, f"numero_cnh='{self.num_cnh}'")

            elif opcao == 4:
                data = input("Informe a nova data de nascimento no formato dd/mm/yyyy: ")
                self.data_nascimento = datetime.strptime(data, "%d/%m/%Y").date()
                if not ('data_nascimento=?' in parametros):
                    parametros.insert(4, f"data_nascimento='{self.data_nascimento}'")

            elif opcao == 5:
                break

            else:
                print("opção inválida")

        if len(parametros):

            parametros = ','.join(parametros)

            status = update(conn, tabela, parametros, filtro)
            if status:
                print("Motorista atualizado com sucesso")
            else:
                print("Não foi possível atualizar o motorista")

    @staticmethod
    def listar_motoristas(conn):

        dados = buscar(conn, 'motoristas', '', '', '', 0)
        if dados:
            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-1] = datetime.strptime(f'{dado[-1]}', "%Y-%m-%d").date().strftime('%d/%m/%Y')
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista, columns=['|id|', '|numero da cnh|', '| nome |',
                                                    '| sobrenome |', '|data de nascimento|'])
            print(df.to_string(index=False))
        else:
            print("Não há dados")


class Cartao:
    def __init__(self, id_usuario, qtd_creditos, tipo, data_emissao):
        self.__id_usuario = id_usuario
        self.__qtd_creditos = qtd_creditos
        self.__tipo = tipo
        self.__data_emissao = data_emissao

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @property
    def qtd_creditos(self):
        return self.__qtd_creditos

    @qtd_creditos.setter
    def qtd_creditos(self, valor):
        self.__qtd_creditos = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def data_emissao(self):
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, valor):
        self.__data_emissao = valor

    def inserir_cartao(self, conn):
        tabela = 'cartoes'
        colunas = '(qtd_creditos_disponivel, tipo, data_de_emissao, id_usuario)'
        valores = '(?, ?, ?, ?)'
        parametros = (self.qtd_creditos, self.tipo, self.data_emissao, self.id_usuario)
        usuario_cartoes = buscar(conn, 'cartoes', '', 'id_usuario', self.id_usuario, 1)
        dup_cartao = False
        idoso_cartao = False
        idade_limite = 60

        if usuario_cartoes:
            for cartao in usuario_cartoes:
                if cartao[2] == self.tipo:
                    dup_cartao = True
                    break
        if dup_cartao:
            print(f'o usuário já possui um cartão do tipo: {self.tipo}')
        else:
            if self.tipo == 'Idoso':
                usuario = buscar(conn, 'usuarios','','id', self.id_usuario, 1)
                data_nasc = usuario[0][-1]
                data_atual = datetime.now().date()
                anos = abs((data_atual - data_nasc).days) / 365
                if anos > idade_limite:
                    idoso_cartao = True
                else:
                    print(f'o usuário não possui os requisitos para possuir cartão do tipo Idoso')
            if self.tipo != 'Idoso' or idoso_cartao:
                retorno = inserir(conn, tabela, colunas, valores, parametros)

                if retorno:
                    print(f"O cartão foi cadastrado com sucesso ")
                else:
                    print("Erro ao cadastrar cartão")

    def atualizar(self, conn, tabela, id):

        parametros = []
        filtro = f'id={id}'
        while True:
            print("indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):\n"
                  "\t1 - quantidade de créditos"
                  "\t2 - Tipo"
                  "\t3 - Data de emissão"
                  "\t4 - id_usuário"
                  "\t5 - (sair)\n")
            opcao = input()
            if opcao.isdigit():
                opcao = int(opcao)

            if opcao == 1:
                self.qtd_creditos = input("Digite a nova quantidade de créditos: ")
                if not ('qtd_creditos_disponivel=?' in parametros):
                    parametros.insert(0, f"qtd_creditos_disponivel='{self.qtd_creditos}'")

            elif opcao == 2:

                print('\n\t(1) - Comum\n'
                      '\t(2) - Estudante\n'
                      '\t(3) - Vale-Transporte\n'
                      '\t(4) - Idoso\n')
                opcao = input("Selecione o tipo do cartão: ")

                if opcao.isdigit():
                    opcao = int(opcao)

                if opcao == 1:
                    self.tipo = 'Comum'

                elif opcao == 2:
                    self.tipo = 'Estudante'

                elif opcao == 3:
                    self.tipo = 'Vale-Tranporte'

                elif opcao == 4:
                    self.tipo = 'Idoso'

                else:
                    print('Opção inválida')
                    pass

                if not ('tipo=?' in parametros):
                    parametros.insert(1, f"tipo='{self.tipo}'")

            elif opcao == 3:
                self.data_emissao = input("Digite a nova data de emissão do cartão: ")
                if not ('data_de_emissao=?' in parametros):
                    parametros.insert(2, f"data_de_emissao='{self.data_emissao}'")

            elif opcao == 4:
                self.id_usuario = input("Informe o novo id do usuário do cartão: ")
                if not ('id_usuario=?' in parametros):
                    parametros.insert(4, f"id_usuario='{self.id_usuario}'")

            elif opcao == 5:
                break

            else:
                print("opção inválida")

        if len(parametros):
            parametros = ','.join(parametros)

            status = update(conn, tabela, parametros, filtro)
            if status:
                print("Cartão atualizado com sucesso")
            else:
                print("Não foi possível atualizar o cartão")

    @staticmethod
    def listar_cartoes(conn):

        dados = buscar(conn, 'cartoes', '', '', '', 0)
        if dados:
            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-2] = datetime.strptime(f'{dado[-2]}', "%Y-%m-%d").date().strftime('%d/%m/%Y')
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista,
                              columns=['|id|', '|Quantidade de créditos|', '|   Tipo   |',
                                       '|Data de emissão|', '|id do usuário|'])

            print(df.to_string(index=False))
        else:
            print("Não há dados")


class Onibus:
    def __init__(self, num_placa, num_linha, modelo_onibus, ano_fabricacao, id_motorista):
        self.__num_placa = num_placa
        self.__num_linha = num_linha
        self.__modelo_onibus = modelo_onibus
        self.__ano_fabricacao = ano_fabricacao
        self.__id_motorista = id_motorista

    @property
    def num_placa(self):
        return self.__num_placa

    @num_placa.setter
    def num_placa(self, valor):
        self.__num_placa = valor

    @property
    def num_linha(self):
        return self.__num_linha

    @num_linha.setter
    def num_linha(self, valor):
        self.__num_linha = valor

    @property
    def modelo_onibus(self):
        return self.__modelo_onibus

    @modelo_onibus.setter
    def modelo_onibus(self, valor):
        self.__modelo_onibus = valor

    @property
    def ano_fabricacao(self):
        return self.__ano_fabricacao

    @ano_fabricacao.setter
    def ano_fabricacao(self, valor):
        self.__ano_fabricacao = valor

    @property
    def id_motorista(self):
        return self.__id_motorista

    @id_motorista.setter
    def id_motorista(self, valor):
        self.__id_motorista = valor

    def inserir_onibus(self, conn):
        tabela = 'onibus'
        colunas = '(numero_da_placa, numero_da_linha, modelo_do_onibus, ano_de_fabricacao, id_motorista)'
        valores = '(?, ?, ?, ?, ?)'
        parametros = (self.num_placa, self.num_linha, self.modelo_onibus, self.ano_fabricacao, self.id_motorista)

        retorno = inserir(conn, tabela, colunas, valores, parametros)

        if retorno:
            print(
                f"O ônibus modelo: {self.modelo_onibus}, placa: {self.num_placa}, linha: {self.num_linha} foi inserido com sucesso ")
        else:
            print("Erro ao cadastrar ônibus")

    def atualizar(self, conn, tabela, id):

        parametros = []
        filtro = f'id={id}'
        while True:
            print("indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):\n"
                  "\t1 - número da placa"
                  "\t2 - número da linha"
                  "\t3 - modelo do ônibus"
                  "\t4 - ano de fabricação"
                  "\t5 - id do motorista"
                  "\t6 - (sair)\n")
            opcao = input()
            if opcao.isdigit():
                opcao = int(opcao)

            if opcao == 1:
                self.num_placa = input("Digite o novo número da placa: ")
                if not ('numero_da_placa=?' in parametros):
                    parametros.insert(0, f"numero_da_placa='{self.num_placa}'")

            elif opcao == 2:
                self.num_linha = input("Digite o novo número da linha: ")
                if not ('numero_da_linha=?' in parametros):
                    parametros.insert(1, f"numero_da_linha='{self.num_linha}'")

            elif opcao == 3:
                self.modelo_onibus = input("Digite o novo modelo do ônibus: ")
                if not ('modelo_do_onibus=?' in parametros):
                    parametros.insert(2, f"modelo_do_onibus='{self.modelo_onibus}'")

            elif opcao == 4:
                ano = input("Informe o novo ano de fabricação no formato yyyy: ")
                self.ano_fabricacao = datetime.strptime('1/1/' + ano, "%d/%m/%Y").date()
                if not ('ano_de_fabricacao=?' in parametros):
                    parametros.insert(4, f"ano_de_fabricacao='{self.ano_fabricacao}'")

            elif opcao == 5:
                self.id_motorista = input("Digite o novo id do motorista do ônibus: ")
                if not ('id_motorista=?' in parametros):
                    parametros.insert(2, f"id_motorista='{self.id_motorista}'")

            elif opcao == 6:
                break

            else:
                print("opção inválida")

        if len(parametros):
            parametros = ','.join(parametros)

            status = update(conn, tabela, parametros, filtro)
            if status:
                print("Ônibus atualizado com sucesso")
            else:
                print("Não foi possível atualizar o ônibus")

    @staticmethod
    def listar_onibus(conn):

        dados = buscar(conn, 'onibus', '', '', '', 0)
        if dados:
            dados_lista = []
            for dado in dados:
                dado = list(dado)
                dado[-2] = dado[-2].year
                dados_lista.append(dado)

            df = pd.DataFrame(dados_lista,
                              columns=['|id|', '|Nº da placa|', '|Nº da linha|', '|Mod. do ônibus|',
                                       '|Ano de fabricação|',
                                       '|id do motorista|'])

            print(df.to_string(index=False))
        else:
            print("Não há dados")
