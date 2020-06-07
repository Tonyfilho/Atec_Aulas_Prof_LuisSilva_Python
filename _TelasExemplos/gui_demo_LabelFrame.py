#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções

#Gui frame
root = Tk()
root.geometry('280x80')
root.title('Gui LabelFrame demo')
root.resizable(False,False)

lbframe = LabelFrame(root, text= ' Isto é uma LabelFrame ')
lbframe.pack(fill=BOTH, expand='yes')

l = Label( lbframe, text='Texto dentro da LabelFrame')
l.pack(anchor = CENTER)


#visualização
root.mainloop()




