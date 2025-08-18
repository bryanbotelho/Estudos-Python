def zenit_polar_replace(text):
    #Aplicar a codificação Z-E-N-I-T P-O-L-A-R utilizando o replace
    replacements = [('z', 'p'), ('e', 'o'),('n', 'l'), ('i', 'a'),('t', 'r'),
                    ('Z', 'P'), ('E', 'O'),('N', 'L'), ('I', 'A'),('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
        return text
    
def main():
    #Entrada da frase e aplicação da codificação
    phrase = "The quick brow fox jumps over the lazy dog"
    phrase_title = phrase.title()

    #Dividir a frase em palavras
    words = phrase.split()

    #Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    #Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Title:", phrase_title)
    print("Coded:", coded_phrase)

if __name__ == "__main__":
    main()

        
                    