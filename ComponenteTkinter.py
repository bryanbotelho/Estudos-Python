from tkinter import *

root = Tk()
root.title("Exemplo de botão")

def clicar():
    print("Botão Clicado !")

w=Button(root, text="Clique aqui", command=clicar)

w.pack()
root.mainloop()
