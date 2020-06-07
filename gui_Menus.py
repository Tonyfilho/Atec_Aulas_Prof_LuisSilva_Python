'''
Menubar, Menu, MenuItem

@autor : Luis Filipe
@Data  : 05-05-2020
@Linguagem : Python

'''

#+++++++++++++++++++++++++++++++++++++++++++
#Bibliotecas
from tkinter import *
from tkinter import messagebox


#+++++++++++++++++++++++++++++++++++++++++++
#dados Globais


#+++++++++++++++++++++++++++++++++++++++++++
#Metodos
def donothing():
          pass

#++++++++++++++++++++++++++++++++
def acao1():
          messagebox.showinfo('Dialogo Ação 1','\nRealizar a ação 1\n')

def Autor():
    messagebox.showinfo('Dialogo Autor','\nName : Luis Filipe\nFunction : It Trainning\nCurso: CET´s Palmela\n\nMake the thing\'s easy')

def Linguagem():
    messagebox.showinfo('Dialogo Linguagem','\nLanguage : Python\nVersion : 3.80 ')

def Programa():
    messagebox.showinfo('Dialogo Programa','\nPrograma que mostra\na possibilidade de usar MenuBar\nnuma aplicação Python GUI(Tkinter)')

def abandonar(): 
    perg = messagebox.askquestion('Dialogo Abandonar', '\nConfirma que deseija\nabandonar a aplicação.\n')
    if perg == 'yes':
          root.destroy()


#+++++++++++++++++++++++++++++++++++++++++++
#GUI
root = Tk()
root.title("Exemplo")
root.geometry("600x800")
root.resizable(False,False)


#+++++++++++++++++++++++++++++++++++++++++++
#MenuBar
menubar = Menu()

#Menu filemenu
filemenu = Menu(menubar, tearoff = 0)

#MenuItem
filemenu.add_command(label='Ação 1', command = acao1)
filemenu.add_separator()
filemenu.add_command(label='Sair', command= abandonar)

#Titulo do Menu
menubar.add_cascade(label='File', menu=filemenu)

#Menu filehlp
filehlp = Menu(menubar, tearoff= 0)

#MenuItem
filehlp.add_command(label = 'Programa', command = Programa)
filehlp.add_command(label = 'Linguagem', command = Linguagem)
filehlp.add_separator()
filehlp.add_command(label = 'Autor', command = Autor)

#Titulo do Menu
menubar.add_cascade(label='Help', menu = filehlp)

#juntar o menu a root
root.config(menu=menubar)



#+++++++++++++++++++++++++++++++++++++++++++
#mostrar o GUI 
root.mainloop()
