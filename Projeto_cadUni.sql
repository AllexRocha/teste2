

CREATE TABLE alex_rocha.cartoes(
	id INT NOT NULL PRIMARY KEY IDENTITY (1, 1),
    qtd_creditos_disponivel FLOAT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    data_de_emissao DATE NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES alex_rocha.usuarios(id)
);

CREATE TABLE alex_rocha.usuarios(
	id INT NOT NULL PRIMARY KEY IDENTITY (1, 1),
    nome VARCHAR(40) NOT NULL,
    sobrenome VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
	bairro VARCHAR(50) NOT NULL,
	data_nascimento DATE NOT NULL
);

 CREATE TABLE alex_rocha.motoristas(
	id INT NOT NULL PRIMARY KEY IDENTITY (1, 1),
    numero_cnh INT NOT NULL,
    nome VARCHAR(40) NOT NULL,
    sobrenome VARCHAR(40) NOT NULL,
	data_nascimento DATE NOT NULL
);

CREATE TABLE alex_rocha.onibus(
	id INT NOT NULL PRIMARY KEY IDENTITY (1, 1),
    numero_da_placa INT NOT NULL,
    numero_da_linha INT NOT NULL,
    modelo_do_onibus VARCHAR(45),
    ano_de_fabricacao DATE NOT NULL,
    id_motorista INT NOT NULL,
    FOREIGN KEY (id_motorista) REFERENCES alex_rocha.motoristas(id)
);
