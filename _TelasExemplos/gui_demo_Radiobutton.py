#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções
def sel():
          selection = 'Valor : '+str(var.get())
          l.config(text=selection)
          
          
#Gui frame
root = Tk()
root.geometry('300x180')
root.title('Gui Scale Demo')
root.resizable(False,False)

var = DoubleVar()
s1 = Scale(root, variable= var).pack(anchor = CENTER)
b1 = Button(root, text='Get Scale Valor', command=sel).pack(anchor = CENTER)
l = Label(root)
l.pack()

#visualização
root.mainloop()




