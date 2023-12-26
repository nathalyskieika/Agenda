import sqlite3
from sqlite3 import connect, Error

def ConexaoBanco():
	caminho="C:\\Users\\natha\\OneDrive\\Documentos\\projeto\\agenda\\agenda.db"
	con=None
	try:
		con=sqlite3.connect(caminho)
	except Error as ex:
		print(ex)
	return con

vcon=ConexaoBanco()
def deletar(conexao,sql):
	try:
		c=conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		print(ex)
	finally:
		print("Registro removido")


vcon = ConexaoBanco()

excluir=input("Você deseja excluir algum contato? (s/n)")

if excluir.lower() == 's': 
    if vcon:
        id_contato_para_deletar = input("Digite o ID do contato que deseja deletar: ")
        vsql = f"DELETE FROM tb_contatos WHERE IDCONTATO={id_contato_para_deletar}"
        deletar(vcon, vsql)

if vcon:
    vcon.close()
