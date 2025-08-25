#Utilizando SQLite
import sqlite3 as conector
#Abrir conexão
conexao = conector.connect("URL SQLite")
#Aquisição do cursor
cursor = conexao.cursor()
#Executando comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()
#Efetivando comando
conexao.commit()
#Fechando a conexão
cursor.close()
conexao.close()


#utilizando MySQL
import mysql.connector as conector
#Abrir conexão
conexao = conector.connect("URL MySQL")
#Aquisição do cursor
cursor = conexao.cursor()
#Executando comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()
#Efetivando comando
conexao.commit()
#Fechando a conexão
cursor.close()
conexao.close()

#utilizando PostGres
import psycopg2 as conector
#Abrir conexão
conexao = conector.connect("URL PostgresSQL")
#Aquisição do cursor
cursor = conexao.cursor()
#Executando comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()
#Efetivando comando
conexao.commit()
#Fechando a conexão
cursor.close()
conexao.close()