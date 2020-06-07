#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções

#Gui frame
root = Tk()
root.geometry('280x180')
root.title('Gui Scrollbar Demo')
root.resizable(False,False)

scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)

lista = Listbox(root, yscrollcommand=scroll.set)
for line in range(50):
          lista.insert(END, "this is line number : " + str(line))
          
lista.pack( side = TOP,  anchor = CENTER)
scroll.config(command= lista.yview)

#visualização
root.mainloop()




