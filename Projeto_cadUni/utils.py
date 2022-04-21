"""funções úteis"""

from classes import *
from database2 import *
import datetime


def formatar_data(data, opcao):
    if opcao == 0:  # para enviar ao banco de dados
        try:
            return datetime.datetime.strptime(data, "%d/%m/%Y").date()
        except:
            print("O formato de data não está correto")

    if opcao == 1:  # para formatar a data recebida do banco de dados
        try:
            return datetime.datetime.strptime(data, "%Y-%m-%d").date().strftime('%d/%m/%Y')
        except:
            print("Erro ao converter a data")


def cadastrar_usuario():
    nome = input("Insira o nome do usuário: ")
    sobrenome = input("Insira o sobrenome do usuário: ")
    email = input("Insira o e-mail do usuário: ")
    bairro = input("Insira o bairro do usuário: ")
    data = input("Informe a data de nascimento no formato dd/mm/yyyy: ")
    data_nascimento = formatar_data(data, 0)

    usuario = Usuario(nome, sobrenome, data_nascimento, email, bairro)
    usuario.inserirUsuario()

def cadastrar_motorista():
    nome = input("Insira o nome do motorista: ")
    sobrenome = input("Insira o sobrenome do motorista: ")
    numero_cnh = input("Insira a cnh do motorista: ")
    data = input("Informe a data de nascimento no formato dd/mm/yyyy: ")
    data_nascimento = formatar_data(data, 0)

    motorista = Motorista(nome, sobrenome, data_nascimento, numero_cnh)
    motorista.inserirMotorista()


def cadastrar_onibus():
    numero_placa = int(input("Informe o número da placa do veículo: "))
    numero_linha = int(input("Informe o número da linha do veículo: "))
    modelo_do_onibus = input("Informe o modelo do ônibus: ")
    data = input("Informe o ano de fabricação do ônibus: ")
    ano_de_fabricacao = formatar_data('01/01/' + data, 0)

    num_cnh = int(input("Informe o número da cnh do motorista do ônibus: "))
    id_motorista = buscar('motoristas', 'numero_cnh', num_cnh)

    onibus = Onibus(numero_placa, numero_linha, modelo_do_onibus, ano_de_fabricacao, id_motorista[0][0])
    onibus.inserir_onibus()

def cadastrar_cartao():
    global id_usuario
    qtd_creditos = float(input("Insira a quantidade de creitos disponível: "))
    tipo = input("Diga o tipo do cartão (comum, estudante, vale-transporte ou idoso): ")
    data_emissao = datetime.datetime.now().date()
    nome = input("Informe o nome do usuário ao qual o cartão irá pertencer: ")
    usuarios = buscar('usuarios', 'nome', f"'{nome}'")


    if len(usuarios) > 0:
        if len(usuarios) == 1:
            id_usuario = usuarios[0][0]

        else:
            sobrenome = input("Existem mais de um usuário com o nome informado, por favor indique o sobrenome do usuário: ")
            for usuario in usuarios:
                if sobrenome in usuario:
                    id_usuario = usuario[0]
                    break

        cartao = Cartao(id_usuario, qtd_creditos, tipo, data_emissao)
        cartao.inserir_cartao()
    else:
        print("Não existe usuário cadastrado com o nome informado")

def atualizar():
    tabela = input("Informe a tabela em que consta o dado a ser atualizado: ")
    id = int(input("Informe o ID do dado a ser atualizado: "))

    dado = buscar(tabela, 'id', id)

    if tabela == 'usuarios':
        usuario = Usuario(dado[0][1], dado[0][2], dado[0][3], dado[0][4], dado[0][5])
        usuario.atualizar(tabela, id)
    elif tabela == 'cartoes':
        cartao = Cartao(dado[0][0], dado[0][1], dado[0][2], dado[0][3])
    elif tabela == 'motoristas':
        motorista = Motorista(dado[0][0], dado[0][1], dado[0][2], dado[0][3])
    elif tabela == 'onibus':
        onibus = Onibus(dado[0][0], dado[0][1], dado[0][2], dado[0][3], dado[0][4])



def deletar():

    tabela = input("Informe a tabela em que consta o dado a ser deletado: ")
    id = int(input("Informe o ID do dado a ser deletado: "))


    print("O usuário e todo registro relacionado a ele serão deletados do sistema,"
                      " Deseja continuar ?")
    while True:
        opcao = input("Digite S(sim)/N(não): ").upper()

        if opcao == 'S' or opcao == 'N':
            if opcao == 'S':
                if tabela == 'usuarios':
                    dados = buscar('cartoes', 'id_usuario', id)
                    if tabela == 'usuarios':
                        dados = buscar('cartoes', 'id_usuario', id)
                        if dados:
                            delete('cartoes',dados[0][0])
                elif tabela == 'motoristas':
                    dados = buscar('onibus', 'id_motorista', id)
                    if dados:
                        print("Há um ou mais ônibus vinculados a este motorista,"
                              " por favor selecione um novo motorista para vincular")

                delete(tabela, id)
                break
            else:
                print("Os dados NÃO foram deletados")
                break
        else:
            print("opção inválida")

def listar(tabela):
    dados = buscar(tabela, '', '')

    for dado in dados:
        print(dado)

if __name__ == "__main__":
    # cadastrar_motorista()
    # Motorista.listar_motoristas()
    # Cartao.listar_cartoes()
    Onibus.listar_onibus()