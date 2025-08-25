import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    RemoverDado = '''DROP TABLE Veiculo;'''
    cursor.execute(RemoverDado)

    CriarVeiculo = '''CREATE TABLE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY (marca) REFERENCES Marca(id)
                    );'''

    cursor.execute(CriarVeiculo)
    
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro no banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()