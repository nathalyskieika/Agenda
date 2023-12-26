import sqlite3
from sqlite3 import Error

def ConexaoBanco():
	caminho="C:\\Users\\natha\\OneDrive\\Documentos\\projeto\\agenda\\agenda.db"
	con=None
	try:
		con=sqlite3.connect(caminho)
	except Error as ex:
		print(ex)
	return con

vcon=ConexaoBanco()

vsql="""CREATE TABLE tb_contatos(
	IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMECONTATO TEXT(30),
	TELEFONECONTATO TEXT(14),
	EMAILCONTATO TEXT(30)
);"""

def criarTabela(conexao,sql):
	try:
	  c=conexao.cursor()
	  c.execute(sql)
	  print("Tabela criada")
	except Error as ex:
 	   print(ex)

criarTabela(vcon, vsql)

vcon.close()

import sqlite3
from sqlite3 import Error

def ConexaoBanco():
	caminho="C:\\Users\\natha\\OneDrive\\Documentos\\projeto\\agenda\\agenda.db"
	con=None
	try:
		con=sqlite3.connect(caminho)
	except Error as ex:
		print(ex)
	return con

vcon=ConexaoBanco()

def inserir(conexao,sql):
	try:
	  c=conexao.cursor()
	  c.execute(sql)
	  conexao.commit()
	  print("Registro Inserido")
	except Error as ex:
	  print(ex)

def obter_dados_contato():
    nome=input("Digite o nome: ")
    telefone=input("Digite o telefone: ")
    email=input("Digite o email: ")
    return nome, telefone, email

vcon=ConexaoBanco()

while True:
    nome, telefone, email = obter_dados_contato()

    vsql="""INSERT INTO tb_contatos (NOMECONTATO, TELEFONECONTATO, EMAILCONTATO)
	VALUES('{}', '{}', '{}')""".format(nome, telefone, email)

    inserir(vcon,vsql)
	
    resposta=input("Deseja inserir outro contato? (s/n): ")

    if resposta.lower() != 's':
        break

vcon.close()

