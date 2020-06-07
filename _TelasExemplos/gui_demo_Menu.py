#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções
def sel():
          selection = 'Escolheu a opção : '+str(var.get())
          l.config(text=selection)
          
          
#Gui frame
root = Tk()
root.geometry('300x100')
root.title('Gui RadioButton Demo')
root.resizable(False,False)

var = IntVar()
r1 = Radiobutton(root, text='Opção 1', variable= var, value=1 , command = sel).pack(anchor = W)
r2 = Radiobutton(root, text='Opção 2', variable= var, value=2 , command = sel).pack(anchor = W)
r3 = Radiobutton(root, text='Opção 3', variable= var, value=3 , command = sel).pack(anchor = W)

l = Label(root)
l.pack()

#visualização
root.mainloop()




