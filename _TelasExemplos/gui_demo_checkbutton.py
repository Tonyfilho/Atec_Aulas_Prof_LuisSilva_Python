#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções
def saudacao():
          messagebox.showinfo('Dialogo','Saudações ARCI')
          
#Gui frame
root = Tk()
root.geometry('300x200')
root.title('Gui Checkbutton Demo')
root.resizable(False,False)

check1 = IntVar()
check2 = IntVar()
C1 = Checkbutton(root, text='Music', variable=check1,\
                 onvalue = 1, offvalue = 0, height=5,\
                 width = 20)

C2 = Checkbutton(root, text='Video', variable=check2,\
                 onvalue = 1, offvalue = 0, height=5,\
                 width = 20)
C1.pack()
C2.pack()


#layout

#visualização
root.mainloop()




