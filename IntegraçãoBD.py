import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port=5432,
    database ='postgresDB',
    user = 'admin', 
    password = 'admin123'
)

cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS public."AGENDA"
(
    id integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    telefone char(12) COLLATE pg_catalog."default" NOT NULL
)
TABLESPACE pg_default;
ALTER TABLE public."AGENDA"
    OWNER to admin;
               """)

#Inserir dados na tabela
cursor.execute(
    """
INSERT INTO public."AGENDA" (id, nome, telefone)
VALUES (1, 'teste1', '021999999999');
"""
)
cursor.execute("""
INSERT INTO public."AGENDA" (id, nome, telefone)
VALUES (2, 'teste 2', '021888888888');
""")
conn.commit()

#Ler os dados
cursor.execute("""
SELECT id, nome ,telefone FROM public."AGENDA";
""")
row = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

conn.commit()

#Fechar conexão
cursor.close()
conn.close()