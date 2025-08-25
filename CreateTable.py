import sqlite3 as conector

try:
    conexão = conector.connect("./meu_banco.db")
    cursor = conexão.cursor()

    CriarPessoa = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''
    CriarMarca = '''CREATE TABLE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''
    CriarVeiculo = '''CREATE TABLE Veiculo (
                    placa INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa)
                    );'''

    cursor.execute(CriarPessoa)
    cursor.execute(CriarMarca)
    cursor.execute(CriarVeiculo)

    conexão.commit()
except conector.DatabaseError as err:
    print("Erro no banco de dados", err)

finally:
    if conexão:
        cursor.close()
        conexão.close()

