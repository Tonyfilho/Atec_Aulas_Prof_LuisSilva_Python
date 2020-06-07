#Bibliotecas
from tkinter import *
from tkinter import messagebox

#Funções

#Gui frame
root = Tk()
root.geometry('280x80')
root.title('Gui PanedWindow  demo')
root.resizable(False,False)

pw1 = PanedWindow()
pw1.pack(fill=BOTH, expand=1)

esq = Label(pw1, text='Esq pane')
pw1.add(esq)

pw2 = PanedWindow(pw1, orient = VERTICAL)
pw1.add(pw2)

cima = Label(pw2, text='Cima pane')
pw2.add(cima)

baixo = Label(pw2, text='Baixo pane')
pw2.add(baixo)

#visualização
root.mainloop()




