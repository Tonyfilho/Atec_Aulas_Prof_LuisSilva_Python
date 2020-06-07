#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções
def donothing():
          x = 0
          
          
#Gui frame
root = Tk()
root.geometry('300x100')
root.title('Gui Menu Demo')
root.resizable(False,False)

mnb = Menu(root)
filemenu = Menu(mnb, tearoff = 0)
filemenu.add_command(label = 'New', command = donothing)
filemenu.add_command(label = 'Open', command = donothing)
filemenu.add_command(label = 'Save', command = donothing)
filemenu.add_command(label = 'Save as...', command = donothing)
filemenu.add_command(label = 'Close', command = donothing)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = donothing)
mnb.add_cascade(label='File', menu=filemenu)
root.config(menu=mnb)

#visualização
root.mainloop()




