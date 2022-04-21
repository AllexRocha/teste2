from database2 import *
import pandas as pd


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

    def inserirUsuario(self):

        tabela = 'usuarios'
        colunas = '(nome, sobrenome, email, bairro, data_nascimento)'
        valores = '(?, ?, ?, ?, ?)'
        parametros = (self.nome, self.sobrenome, self.email, self.bairro, self.data_nascimento)

        retorno = inserir(tabela, colunas, valores, parametros)

        if retorno:
            print(f"O(A) usuário(a) {self.nome} {self.sobrenome} foi cadastrado(a) com sucesso.")
        else:
            print("Erro ao cadastrar usuário")

    def atualizar(self, tabela, id):

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
                self.data_nascimento = formatar_data(data, 0)
                if not ('data_nascimento=?' in parametros):
                    parametros.insert(4, f"data_nascimento='{self.data_nascimento}'")

            elif opcao == 6:
                break

            else:
                print("opção inválida")

        parametros = ','.join(parametros)

        update(tabela, parametros, filtro)


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

    def inserirMotorista(self):

        tabela = 'motoristas'
        colunas = '(numero_cnh, nome, sobrenome, data_nascimento)'
        valores = '(?, ?, ?, ?)'
        parametros = (self.num_cnh, self.nome, self.sobrenome, self.data_nascimento)

        retorno = inserir(tabela, colunas, valores, parametros)

        if retorno:
            print(f"O(A) motorista(a) {self.nome} {self.sobrenome} foi cadastrado(a) com sucesso.")
        else:
            print("Erro ao cadastrar motorista")
    @staticmethod
    def listar_motoristas():

        dados = buscar('motoristas', '', '')
        dados_lista = []
        for dado in dados:
            dado = list(dado)
            dados_lista.append(dado)


        df = pd.DataFrame(dados_lista, columns= ['id', 'nome', 'sobrenome', 'numero da cnh', 'data de nascimento'])
        print(df.to_string(index=False))

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

    def inserir_cartao(self):
        tabela = 'cartoes'
        colunas = '(qtd_creditos_disponivel, tipo, data_de_emissao, id_usuario)'
        valores = '(?, ?, ?, ?)'
        parametros = (self.qtd_creditos, self.tipo, self.data_emissao, self.id_usuario)

        retorno = inserir(tabela, colunas, valores, parametros)

        if retorno:
            print(f"O cartão foi cadastrado com sucesso ")
        else:
            print("Erro ao cadastrar cartão")


    @staticmethod
    def listar_cartoes():

        dados = buscar('cartoes', '', '')
        dados_lista = []
        for dado in dados:
            dado = list(dado)
            dados_lista.append(dado)



        df = pd.DataFrame(dados_lista, columns= ['id', 'Quantidade de créditos', 'Tipo', 'Data de emissão', 'id do usuário'])

        print(df.to_string(index=False))

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

    def inserir_onibus(self):
        tabela = 'onibus'
        colunas = '(numero_da_placa, numero_da_linha, modelo_do_onibus, ano_de_fabricacao, id_motorista)'
        valores = '(?, ?, ?, ?, ?)'
        parametros = (self.num_placa, self.num_linha, self.modelo_onibus, self.ano_fabricacao, self.id_motorista)

        retorno = inserir(tabela, colunas, valores, parametros)

        if retorno:
            print(
                f"O ônibus modelo: {self.modelo_onibus}, placa: {self.num_placa}, linha: {self.num_linha} foi inserido com sucesso ")
        else:
            print("Erro ao cadastrar ônibus")

    @staticmethod
    def listar_onibus():

        dados = buscar('onibus', '', '')
        dados_lista = []
        for dado in dados:
            dado = list(dado)
            dados_lista.append(dado)

        df = pd.DataFrame(dados_lista,
                          columns=['id', 'Nº da placa', 'Nº da linha', 'Mod. do ônibus','Ano de fabricação', 'id do motorista'])

        print(df.to_string(index=False))