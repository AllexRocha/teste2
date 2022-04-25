# 						 PROJETO CADUNI

O projeto caduni permite fazer o gerenciamento de usuários e cartões assim como de motoristas e a frota de ônibus de uma empresa de transportes. Oferecendo cadastro, listagem, atualização e exclusão de usuários, motoristas, cartões e ônibus de um banco de dados

## Menu principal

	########################* Sistema de cadastro CADUni *#########################
	(1) - Cadastrar dados
	(2) - Listar dados
	(3) - Atualizar dados
	(4) - Deletar dados
	(5) - Finalizar o programa


	Indique uma opção: 

## Cadastro 



É possível cadastrar Usuários , cartões, motoristas e ônibus. Sendo que os cartões ficam atrelados aos usuários e os ônibus aos motoristas. Sendo que cada usuário pode ter um cartão de cada tipo.


	################ * Cadastrar dados * ##############
	(1) - Cadastrar Usuários
	(2) - Cadastrar Motoristas
	(3) - Cadastrar Cartões
	(4) - Cadastrar Ônibus
	(5) - Retornar


	Indique uma opção desejada:



### Cadastro de usuário

	################ * Cadastrar Usuário * ##############

	Insira o nome do usuário: José
	Insira o sobrenome do usuário: Almeida
	Insira o e-mail do usuário: josealmeida@gmail.com
	Insira o bairro do usuário: Vale do Amanhecer
	Informe a data de nascimento no formato dd/mm/yyyy: 05/09/1967
	O(A) usuário(a) José Almeida foi cadastrado(a) com sucesso.
	Pressione Enter para continuar ...
### Cadastro de motorista

	################ * Cadastrar Motorista * ##############
	
	Insira o nome do motorista: Wesly
	Insira o sobrenome do motorista: Santana
	Insira a cnh do motorista: 22354
	Informe a data de nascimento no formato dd/mm/yyyy: 17/05/1980
	O(A) motorista(a) Wesly Santana foi cadastrado(a) com sucesso.
	
	Pressione Enter para continuar ...



### Cadastro de cartão

`################ * Cadastrar Cartão * ##############`

`Insira a quantidade de créditos disponível: 500`
`(1) - Comum`
`(2) - Estudante`
`(3) - Vale-Transporte`
`(4) - Idoso`

`Selecione o tipo do cartão: 1`
 `|id| |  Nome  | |  Sobrenome  |       |    E-mail   | |     Bairro     | |Data de nascimento|`
    `1       alex           rocha alexjorocha@gmail.com             lnorte           05/09/1993`
    `3      Lucas           Alves          LA@gmail.com              rua 3           05/09/1993`
    `4      José             Luis          JL@gmail.com        Brasil novo           07/11/1980`
    `5      Maria            Rosa       Maria@gmail.com  Jardim Equatorial           18/07/1976`
    `6  Aparecida      das Graças     Apgraça@gmail.com           Laguinho           05/06/1955`
    `7      José          Almeida Josealmeida@gmail.com  vale do amanhecer           05/09/1967`


`Informe o ID do usuário ao qual o cartão irá pertencer: 4`
`O cartão foi cadastrado com sucesso` 

`Pressione Enter para continuar ...`

### Cadastro de ônibus

`################ * Cadastrar Ônibus * ##############`

`Informe o número da placa do veículo: 1245785698`
`Informe o número da linha do veículo: 475`
`Informe o modelo do ônibus: Elétrico`
`Informe o ano de fabricação do ônibus: 2017`
 `|id|  |numero da cnh| | nome | | sobrenome | |data de nascimento|`
    `1            22354     José      da Rocha           25/12/1980`
    `2            22458   janete      estefane           05/09/1978`
    `3            22345    Julio        Mattos           05/09/1990`
    `4            24457  Aristeu       Fonseca           22/08/1960`
    `5           223456    Paulo       Santana           17/05/1980`
    `6            22354    Wesly       Santana           17/05/1980`

`Informe o número o id do motorista do ônibus: 1`
`O ônibus modelo: Elétrico, placa: 1245785698, linha: 475 foi inserido com sucesso` 

`Pressione Enter para continuar ...`

## Listando dados




	################ * listar dados * ##############
	(1) - Listar Usuários
	(2) - Listar Motoristas
	(3) - Listar Cartões
	(4) - Listar Ônibus
	(5) - Listar usuários e cartões
	(6) - listar Motoristas e ônibus
	(7) - Retornar


	Indique a opção desejada: 

para a listagem de dados, as opções acima são oferecidas



### Listagem de usuários

​	`################## * Listando Usuários * ###############`

 `|id| |  Nome  | |  Sobrenome  |       |    E-mail   | |     Bairro     | |Data de nascimento|`
    `1       alex           rocha alexjorocha@gmail.com             lnorte           05/09/1993`
    `3      Lucas           Alves          LA@gmail.com              rua 3           05/09/1993`
    `4      José             Luis          JL@gmail.com        Brasil novo           07/11/1980`
    `5      Maria            Rosa       Maria@gmail.com  Jardim Equatorial           18/07/1976`
    `6  Aparecida      das Graças     Apgraça@gmail.com           Laguinho           05/06/1955`
    `7      José          Almeida Josealmeida@gmail.com  vale do amanhecer           05/09/1967`
`Pressione Enter para continuar ...`



### Listagem de motoristas

`###################### * Listando Motoristas * ################`

 `|id|  |numero da cnh| | nome | | sobrenome | |data de nascimento|`
    `1            22354     José      da Rocha           25/12/1980`
    `2            22458   janete      estefane           05/09/1978`
    `3            22345    Julio        Mattos           05/09/1990`
    `4            24457  Aristeu       Fonseca           22/08/1960`
    `5           223456    Paulo       Santana           17/05/1980`
    `6            22354    Wesly       Santana           17/05/1980`

`Pressione Enter para continuar ...`



### Listagem de cartões

`####################### * Listando Cartões * ##########################`

 `|id|  |Quantidade de créditos|   |   Tipo   | |Data de emissão|  |id do usuário|`
    `1                    458.69 Vale-Tranporte        22/04/2022                1`
    `2                    500.00          Comum        25/04/2022                4`

`Pressione Enter para continuar ...`



### Listagem de ônibus

`################# * Listando Ônibus * #####################`

 `|id|  |Nº da placa|  |Nº da linha| |Mod. do ônibus|  |Ano de fabricação|  |id do motorista|`
  `1     1245785698            475         Elétrico                 2017                  1`

`Pressione Enter para continuar ...`



### Listagem de usuários e seus cartões

`################### * Listando Usuários e cartões * ##########################`

`|  Nome  | | Sobrenome | |Data de Nascimento|  |Qtd de crétditos| |     Tipo    | |Data de Emissão|`
      `alex         rocha           1993-09-05              458.69  Vale-Tranporte        22/04/2022`
     `José           Luis           1980-11-07              500.00           Comum        25/04/2022`
      `alex         rocha           1993-09-05              456.00       Estudante        25/04/2022`
      `alex         rocha           1993-09-05              564.00           Comum        25/04/2022`

`Pressione Enter para continuar ..`.



### Listagem de motoristas e os ônibus

`################## * Listando Motoristas e ônibus * ################`

`| Nome | |  Sobrenome  |  |Nº da CNH|  |Nº da placa|  |Nº da linha| |Modelo do ônibus|  |Ano de fabricação|`
    `José        da Rocha        22354     1245785698            475           Elétrico                 2017`

`Pressione Enter para continuar ...`



## Atualização de dados

Ao atualizar um dado deve ser selecionado o id do usuário a ser atualizado e após isso o parâmetro desejado, digitar o novo dado e fazer isso para cada parâmetro que se deseja. Ao final selecionar sair para que as atualizações sejam efetivadas

`################ * Atualizando Usuário * ##############`

 `|id| |  Nome  | |  Sobrenome  |       |    E-mail   | |     Bairro     | |Data de nascimento|`
    `1       alex           rocha alexjorocha@gmail.com             lnorte           05/09/1993`
    `3      Lucas           Alves          LA@gmail.com              rua 3           05/09/1993`
    `4      José             Luis          JL@gmail.com        Brasil novo           07/11/1980`
    `5      Maria            Rosa       Maria@gmail.com  Jardim Equatorial           18/07/1976`
    `6  Aparecida      das Graças     Apgraça@gmail.com           Laguinho           05/06/1955`
    `7      José          Almeida Josealmeida@gmail.com  vale do amanhecer           05/09/1967`


`Informe o ID do dado a ser atualizado: 3`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`1`
`Digite o novo nome: Antônio`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`2`
`Digite o novo sobrenome: Moraes`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`3`
`Digite o novo e-mail: AntMoraes@gmail.com`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`4`
`Digite o novo bairro: Nova Esperança`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`5`
`Informe a nova data de nascimento no formato dd/mm/yyyy: 04/07/1980`
`indique um parâmetro que deseja atualizar e ao finalizar selecione (sair):`
	`1 - nome	2 - sobrenome	3 - email	4 - bairro	5 - data_nascimento	6 - (sair)`

`6`
`Usuário atualizado com sucesso`
`Pressione Enter para continuar ...`

## Exclusão de dados

### Exclusão de usuários

Ao excluir um usuário, também serão excluídos todos os cartões a este pertencentes

`#################### * Deletando Usuário * ###################`

 `|id| |  Nome  | |  Sobrenome    |    E-mail   | |     Bairro     | |Data de nascimento|`
    `1     alex         rocha  alexjorocha@gmail.com             lnorte           05/09/1993`
    `3    Antônio      Moraes   AntMoraes@gmail.com     Nova Esperança           04/07/1980`
    `4      José       Luis          JL@gmail.com        Brasil novo           07/11/1980`
    `5      Maria      Rosa       Maria@gmail.com  Jardim Equatorial           18/07/1976`
    `6  Aparecida      das Graças     Apgraça@gmail.com     Laguinho           05/06/1955`
    `7      José     Almeida Josealmeida@gmail.com  vale do amanhecer           05/09/1967`

`Informe o ID do dado a ser deletado: 1`
`O registro será excluído junto com todos os registros relacionados. Deseja continuar ?`
`Digite S(sim)/N(não): s`
`Dados deletados`
`Pressione Enter para continuar ...`



Note que os cartões também foram excluídos



`################################## * Listando Usuários e cartões * ##################################`

`|  Nome  | | Sobrenome | |Data de Nascimento|  |Qtd de crétditos| |     Tipo    | |Data de Emissão|`
     `José           Luis           1980-11-07               500.0           Comum        25/04/2022`

`Pressione Enter para continuar ...`

### Exclusão de motoristas

Ao excluir um motorista, caso o mesmo tenha ônibus cadastrados com o id do mesmo será necessário informar o id de outro motorista para vincular a esses ônibus anterior mente vinculados ao motorista que será excluído



`################ * Deletando Motorista * ##############`

 `|id|  |numero da cnh| | nome | | sobrenome | |data de nascimento|`
    `1            22354     José      da Rocha           25/12/1980`
    `2            22458   janete      estefane           05/09/1978`
    `3            22345    Julio        Mattos           05/09/1990`
    `4            24457  Aristeu       Fonseca           22/08/1960`
    `5           223456    Paulo       Santana           17/05/1980`
    `6            22354    Wesly       Santana           17/05/1980`


`Informe o ID do dado a ser deletado: 1`
`O registro será excluído junto com todos os registros relacionados. Deseja continuar ?`
`Digite S(sim)/N(não): s`
`Há um ou mais ônibus vinculados a este motorista, por favor selecione um novo motorista para vincular ou altere manualmente` 

 `|id|  |numero da cnh| | nome | | sobrenome | |data de nascimento|`
    `1            22354     José      da Rocha           25/12/1980`
    `2            22458   janete      estefane           05/09/1978`
    `3            22345    Julio        Mattos           05/09/1990`
    `4            24457  Aristeu       Fonseca           22/08/1960`
    `5           223456    Paulo       Santana           17/05/1980`
    `6            22354    Wesly       Santana           17/05/1980`

`Informe o id do novo motorista para vincular ao ônibusou digite (sair): 2`
`Dados deletados`

`Pressione Enter para continuar ...`



Note que o motorista com id 1 tinha um ônibus vinculado, então foi necessário vincular este ônibus ao motorista de id 2 para deletar o mesmo.
