import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    AlterarDado = '''ALTER TABLE Veiculo
                ADD motor REAL;'''

    cursor.execute(AlterarDado)

    conexao.commit()
except conector.DatabaseError as err:
    print("Erro no banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()