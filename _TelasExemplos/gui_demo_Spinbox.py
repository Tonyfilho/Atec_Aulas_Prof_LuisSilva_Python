#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções

#Gui frame
root = Tk()
root.geometry('280x80')
root.title('Gui Spinbox  demo')
root.resizable(False,False)

spi = Spinbox(root, from_=0, to= 10)
spi.pack(pady = 20)


#visualização
root.mainloop()




