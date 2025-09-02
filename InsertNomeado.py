import sqlite3 as conector
from InsertQueryBD import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

pessoa = Pessoa(2000000072, 'José', '1978-05-23', True)

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''

cursor.execute(comando,{"cpf": pessoa.cpf,
                        "nome": pessoa.nome,
                        "data_nascimento": pessoa.data_nascimento,
                        "usa_oculos": pessoa.usa_oculos})
conexao.commit()

cursor.close()
conexao.close()