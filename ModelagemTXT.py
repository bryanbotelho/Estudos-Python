def main():

    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []

    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

        #Criar o arquivo original
        with open ("Arquivo_maiusculo.txt", "w", encoding='utf-8') as arquivo:
            for frase in frases:
                arquivo.write(frase + "\n")
        print ("Arquivo original criado. Agora vamos manupular os dados.")

        #Manipular os dados (Transformar em maiúsculo)
        dados_modificados = []
        with open ("Arquivo_maiusculo.txt", "r") as arquivo:
            for linha in arquivo: 
                dados_modificados.append(linha.strip().upper())

        #Sobrescrever os dados        
        with open ("Arquivo_maiusculo.txt" ,"w")  as arquivo:
                   for linha in dados_modificados:
                        arquivo.write(linha + "\n")
        print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
     main()