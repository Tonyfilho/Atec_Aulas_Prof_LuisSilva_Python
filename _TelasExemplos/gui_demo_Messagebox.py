#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções
def Sair():
          perg = messagebox.askquestion('Dialogo Sair', 'Confirma abandonar App')
          if perg == 'yes':
                    root.destroy()
                    


#Gui frame
root = Tk()
root.geometry('280x80')
root.title('Gui askquestion demo')
root.resizable(False,False)

b1 = Button(root, text='Sair da App', command= Sair)
b1.pack(anchor = CENTER)

#visualização
root.mainloop()




