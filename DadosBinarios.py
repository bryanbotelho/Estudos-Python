from PIL import Image
import numpy as np

def main ():
    
    #carregar a imagem original
    img = Image.open("simple_icon.png")

    #Converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    print("\n", img_data.shape, "\n")

    #Salvar os dados binários em um arquivo
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)

    #Copiar o arquivo binário
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()
    
    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)
    
    #Manipúlação dos dados do arquivo binário copia
    #Exemplo: Inverter os bytes
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())
    
    #Carregar e mostrar a imagem manupulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)

    #Inverter todos os bytes
    modified_data = np.fliplr(modified_data)

    modified_data = Image.fromarray(modified_data)
    modified_data.show()

if __name__ == "__main__":
    main()