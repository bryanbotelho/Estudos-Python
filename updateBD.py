import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

#Definindo comando
comando1 = '''UPDATE Pessoa SET oculos= 1;''' #Atualiza todos os valores = 1
cursor.execute(comando1)

comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=2000000072;'''#Atualizando de forma dinâmica
cursor.execute(comando2, (False,))

comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos  WHERE cpf = :cpf;''' #Atualizando de forma nomeado
cursor.execute(comando3, {"usa_oculos": False, "cpf": 1000000099})

conexao.commit()

cursor.close()
conexao.close()