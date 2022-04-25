# Sistema POCCOBUS

O sistema de compras de assento POCCOBUS permite que o usuário customize o seu próprio layout
informando a quantidade de linhas e colunas de acordo com a disposição dos assentos, bem como a quantidade de corredores
É possível selecionar o local do assento através de coordenadas e também é possível cancelar a compra destes assentos.

O sistema também gera um arquivo txt que contém um resumo das vendas, cancelamentos e assentos disponíveis em determinada data e hora.
Ao usuário tambémn é permitido que seja feito o reset de todas as informações, limppando todos os dados
e permitindo que seja customizado um novo layout com disposição de assentos customizável.

## Interface Inicial

	############### BEM VINDO AO SISTEMA POCCOBUS #######################

	(1) - Comprar um Assento
	(2) - Cancelar compra
	(3) - Resetar o sistema
	(4) - Finalizar

	Selecione uma das opções:1
	Arquivo não encontrado. Criando e configurando novo layout ...
	Indique a quantidade de linhas: 8
	Indique a quantidade de colunas: 5
	Quantos corredores você quer que o ônibus tenha: 1
	Indique o número da 1ª coluna do corredor vago de 0 a 4: 2
inicialmente caso não exista um layout pré-definido será criado uma matriz que nesse caso tem 8 linhas e 5 colunas, com um corredor na posição da coluna 2.

	##################### COMPRAR ASSENTOS #######################

	LEGENDA
	    M : Assento do motorista
		▒ : Corredor e frente do ônibus
		▓ : Assentos disponíveis para compra
		░ : Assentos selecionado
		X : Assentos indisponíveis para compra

		A	B	C	D	E
	0	M	▒	▒	▒	▒
	1	▓	▓	▒	▓	▓
	2	▓	▓	▒	▓	▓
	3	▓	▓	▒	▓	▓
	4	▓	▓	▒	▓	▓
	5	▓	▓	▒	▓	▓
	6	▓	▓	▒	▓	▓
	7	▓	▓	▒	▓	▓

O layout dos assentos é mostrado quando o usuário escolhe a opção de comprar um assento


	  LEGENDA
	      M : Assento do motorista
	  	▒ : Corredor e frente do ônibus
	  	▓ : Assentos disponíveis para compra
	  	░ : Assentos selecionado
	  	X : Assentos indisponíveis para compra

	  		A	B	C	D	E
	  	0	M	▒	▒	▒	▒
	  	1	▓	▓	▒	▓	▓
	  	2	▓	▓	▒	▓	▓
	  	3	▓	▓	▒	▓	▓
	  	4	▒	▓	▒	▓	▓
	  	5	▓	▓	▒	▓	▓
	  	6	▓	▓	▒	▓	▓
	  	7	▓	▓	▒	▓	▓

	  O assento A4 está disponível ! Deseja fazer a compra ? S(sim)/ N(não): s
	  Compra do assento A4 realizada com sucesso !

O usuário deverá informar a coordena do assento desejado. Sendo a coluna indicada por letras e as linhas por números começando de zero. O sistema não permite que sejam inseridos valores maiores que as dimensões atuais da matriz e nem coordenadas inválidas como 'aaaa' ou 2222 ou a222 ou aaa2.
Ao indicar a coordenada a mesma é destacada e é perguntado ao usuário se o mesmo deseja efetuar a comprar. E caso a coordenada já seja de um assento comprado, o sistema informará isso ao usuário com0o um assento indisponível.


Após realizar a compra do assento é perguntado se o usuário quer ou não finalizar.
caso indique não será solicitada a coordenada do assento desejado novamente

  ## Cancelando a compra

É permitido ao usuário que a compra efetuada seja cancelada, bastando informar a coordenada desejada. Caso o assento tenha sido comprado anteriormente, independente da data, o sistema irá cancelá-lo.
Caso o assento esteja disponível para compra, o sistema informará que o assento não foi comprado e não pode ser cancelado.

	  LEGENDA
	    M : Assento do motorista
		▒ : Corredor e frente do ônibus
		▓ : Assentos disponíveis para compra
		░ : Assentos selecionado
		X : Assentos indisponíveis para compra

		A	B	C	D	E
	0	M	▒	▒	▒	▒
	1	▓	▓	▒	▓	▓
	2	▓	▓	▒	▓	▓
	3	▓	▓	▒	▓	▓
	4	X	▓	▒	▓	▓
	5	▓	▓	▒	▓	▓
	6	▓	▓	▒	▓	▓
	7	▓	▓	▒	▓	▓


	indique a coordenada do assento desejado ou digite sair para finalizar: a4
	Compra cancelada. Aperte Enter para continuar...

## Resetando configurações

Ao resetar as configurações é permitido ao usuário mudar a disposição da matriz, resetando
os assentendos que foram comprador e apagando o arquivo histórico de txt relacao_assentos.txt. A configuração será bem parecida com quando o usuário configura a matriz inicialmente.

	############### BEM VINDO AO SISTEMA POCCOBUS #######################

	(1) - Comprar um Assento
	(2) - Cancelar compra
	(3) - Resetar o sistema
	(4) - Finalizar


	Selecione uma das opções:3
	Tem certeza que deseja resetar os dados S(sim)/N(não)?s
	Indique a quantidade de linhas: 5
	Indique a quantidade de colunas: 5
	Quantos corredores você quer que o ônibus tenha: 1
	Indique o número da 1ª coluna do corredor vago de 0 a 4: 2
	Sistema resetado. Pressione Enter para continuar ...
