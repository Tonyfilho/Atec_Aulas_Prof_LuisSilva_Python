#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções

#Gui frame
root = Tk()
root.geometry('280x180')
root.title('Gui Text Demo')
root.resizable(False,False)

texto = Text(root)
texto.insert(INSERT, "Olá ARCI\n")
texto.insert(END, "\nBye Bye")

texto.pack()

#visualização
root.mainloop()




