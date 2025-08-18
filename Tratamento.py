try:
    #Tentativa de criar um arquivo protegido por permissão
    with open("/diretório_protegido/arquivo.txt", "w") as arquivo:
        arquivo.write("Conteudo do arquivo")
except PermissionError:
    print("Você não tem permissão para criar o arquivo.") 


try:
    #Tentativa de criar um arquivo ja existente
    with open("arquivo_existente.txt", "x") as arqivo:
        arquivo.write("Conteudo do arquivo")
except FileExistsError:
    print("O arquivo ja existe.")


try:
    #Tentativa de arbrir um arquivo que não existe
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")