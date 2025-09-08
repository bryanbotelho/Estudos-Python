import tkinter as tk
from tkinter import messagebox

def submit():
    #recupera os dados
    nome = nome_entry.get()
    email = email_entry.get()

    #Verifica RadioButton está
    linguagem_preferida = linguagem_var.get()

    print("Nome:", nome)
    print("Email:", email)
    print("Linguagem Preferida: ", linguagem_preferida)

    #Mostra uma caixa de mensagem com dados
    messagebox.showinfo(
        "Dados Submetidos",
        f"Nome: {nome}\nEmail: {email}\nLinguagem Preferida: {linguagem_preferida}")
    
#Cria a janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

#Cria um frame de widget
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#Label de entrada para Nome
nome_label = tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, sticky="e")

#Campo de entrada para Nome
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

#Label de entrada para email
email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e")

#Campo de entrada para Email
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Variável para armazenar a escolha
linguagem_var = tk.StringVar(value= "JavaScript")

#Radio para JavaScript
javascript_radio =  tk.Radiobutton(frame, text="JavaScript", variable=linguagem_var, value="JavaScript")
javascript_radio.grid(row=2, column=0)

#Radio para Python
python_radio =  tk.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
python_radio.grid(row=2, column=1)

#Botão Submit
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=3, columnspan=2, pady=40)

#Inicia o Loop
root.mainloop()