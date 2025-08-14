#Manipúlação part 1 - Leitura de todo conteúdo
arquivo = open('ManipString.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print ("Tipo de conteúdo: ", type(conteudo))
print ('Conteúdo retornado pelo read:')
print(repr(conteudo))
arquivo.close()

#Manipulação part 2 - Leitura de Linhas
arquivo2 = open('ManipString.txt', 'r', encoding='utf-8')
conteudo2 = arquivo2.readline()
print ("Tipo de conteúdo: ", type(conteudo2))
print ('Conteúdo retornado pelo read:')
print(repr(conteudo2))
proximo_conteudo = arquivo2.readline()
print ("Proximo conteúdo retornado: ")
print(repr(proximo_conteudo))
arquivo2.close()

#Manipulação part 3 - Contador
with open('ManipString.txt', 'r', encoding='utf-8') as arquivo3:
    contador = 0
    print('Representação do arquivo')
    for linha in arquivo3:
        if linha:
            contador += 1
    print("Total de linhas = ", contador)

with open('ManipString.txt', 'r', encoding='utf-8') as arquivo3:
    contador = 0
    print('Representação do arquivo após strip')
    for linha in arquivo3:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
        print("Total de linhas = ", contador)

arquivo3.close()

#Manipulação part 4 - Contagem por filtro
with open('ManipString.txt', encoding='utf-8') as arquivo4:
    texto = arquivo4.read()
    contador = texto.count("Olá")
    print("Total de Olás = ", contador)

arquivo4.close()

#Manip part 5 - Split de String
frase1 = "Eu gosto de jogar vídeo game"

lista_termo1 = frase1.split()
print(lista_termo1)

frase2 = "Maça  banana       uva              pera"
lista_termo2 = frase2.split()
print(lista_termo2)

frase3 = "Carro,Moto,Avião"
lista_termo3  =frase3.split(',')
print(lista_termo3)

#Manip part 6 - Contagem repetitiva
frase = "Eu amo comer amoras no café da manha"

print("Contagem direta: ", frase.count('amo'))

contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print("Contagem correta: ", contador)