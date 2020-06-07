'''
Grava dados num ficheiro de texto
chamada alarmes.dat
cada linha do ficheiro dispõe de três colunas separadas por virgulas

exemplo:
'Porta 1','06-05-2020','09:12'
'Porta 2','06-05-2020','10:20'

@autor : Luis Filipe
@Data  : 05-05-2020
@Linguagem : Python

'''

#+++++++++++++++++++++++++++++++++++++++++++
#Bibliotecas
from tkinter import *
from tkinter import messagebox
from datetime import datetime

#+++++++++++++++++++++++++++++++++++++++++++
#dados Globais
Int_img = ['Botao_Off1_d.png','Botao_On1_d.png']
estado1 , estado2 = False, False


#+++++++++++++++++++++++++++++++++++++++++++
#Metodos
def donothing():
          pass
#++++++++++++++++++++++++++++++++
def ler_ficheiro():
          pass

def Autor():
    messagebox.showinfo('Dialogo Autor','\nName : Luis Filipe\nFunction : It Trainning\nCurso: CET´s Palmela\n\nMake the thing\'s easy')

def Linguagem():
    messagebox.showinfo('Dialogo Linguagem','\nLanguage : Python\nVersion : 3.80 ')

def Programa():
    messagebox.showinfo('Dialogo Programa','\nControlo de Habitação \ne alarmistica de intrusão\ncom Python e Arduino')

def abandonar(): 
    perg = messagebox.askquestion('Dialogo Abandonar', '\nConfirma que deseija\nabandonar a aplicação.\n')
    if perg == 'yes':
          root.destroy()

#++++++++++++++++++++++++++++++++
def Alarme1():
          global estado1
          global bt1
          global imag1
           
          estado1 = not(estado1)
          if estado1 == True:
                    ms1.set('ON')
                    imag1 = PhotoImage(file=Int_img[1])
                    b1.configure(image=imag1)
                    c.itemconfig(al1,fill='red')
                    
                    hoje = datetime.now()
                    data = hoje.strftime("%d-%m-%Y")
                    horas = hoje.strftime("%H:%M")
                    
                    arquivo = open('alarmes.dat','a')                     
                    arquivo.write('Porta 1')
                    arquivo.write(',')
                    arquivo.write(data)
                    arquivo.write(',')
                    arquivo.write(horas)
                    arquivo.write('\n')
                    arquivo.close()                      
          else:
                    ms1.set('OFF')
                    imag1 = PhotoImage(file=Int_img[0])
                    b1.configure(image=imag1)
                    c.itemconfig(al1,fill='orange')
                    
#++++++++++++++++++++++++++++++++
def Alarme2():
          global estado2
          global bt2
          global imag2
           
          estado2 = not(estado2)
          if estado2 == True:
                    ms2.set('ON')
                    imag2 = PhotoImage(file=Int_img[1])
                    b2.configure(image=imag2)
                    c.itemconfig(al2,fill='red')
                    
                    hoje = datetime.now()
                    data = hoje.strftime("%d-%m-%Y")
                    horas = hoje.strftime("%H:%M")
                    
                    arquivo = open('alarmes.dat','a')                     
                    arquivo.write('Porta 2')
                    arquivo.write(',')
                    arquivo.write(data)
                    arquivo.write(',')
                    arquivo.write(horas)
                    arquivo.write('\n')
                    arquivo.close()                      
          else:
                    ms2.set('OFF')
                    imag2 = PhotoImage(file=Int_img[0])
                    b2.configure(image=imag2)
                    c.itemconfig(al2,fill='orange')


#+++++++++++++++++++++++++++++++++++++++++++
#GUI
root = Tk()
root.title("Exemplo")
root.geometry("600x800")
root.resizable(False,False)


#+++++++++++++++++++++++++++++++++++++++++++
#MenuBar
menubar = Menu()
#Menu
filemenu = Menu(menubar, tearoff = 0)
#MenuItem
filemenu.add_command(label='Ler ficheiro', command = ler_ficheiro)
filemenu.add_separator()
filemenu.add_command(label='Sair', command= abandonar)
#Titulo do Menu
menubar.add_cascade(label='File', menu=filemenu)

filehlp = Menu(menubar, tearoff= 0)
filehlp.add_command(label = 'Programa', command = Programa)
filehlp.add_command(label = 'Linguagem', command = Linguagem)
filehlp.add_separator()
filehlp.add_command(label = 'Autor', command = Autor)
menubar.add_cascade(label='Help', menu = filehlp)

#juntar o menu a root
root.config(menu=menubar)


#+++++++++++++++++++++++++++++++++++++++++++
#painel superior
p1 = Frame(root, widt="600", height="80", bg= "pink")

lb1 = Label(p1, text="Alarme1", fg="blue")
lb1.pack(side=LEFT , padx=50, pady= 20)

ms1 = StringVar()
E1 = Entry(p1 ,textvariable = ms1)
E1.insert(END,'OFF')
E1.pack(side=LEFT, padx=20, pady = 20)

lb2 = Label(p1, text="Alarme2", fg="blue")
lb2.pack(side=LEFT , padx=50, pady= 20)

ms2 = StringVar()
E2 = Entry(p1, textvariable = ms2)
E2.insert(END,'OFF')
E2.pack(side=LEFT, padx=20, pady = 20)

p1.pack()

#+++++++++++++++++++++++++++++++++++++++++++
#painel grafico
c = Canvas(root,width="600", height="660", bg="yellow")

#sem alarme
img_ps0 = PhotoImage(file = 'piso_zero.png') #imagem de fundo planta
fundo = c.create_image(20,20, image= img_ps0, anchor=NW)
al1 = c.create_oval(40,50,60,70,fill='orange')#Alarme

#sem alarme
al2 = c.create_oval(50,510,70,530,fill='orange')#Alarme
c.pack()

#painel inferior
p2= Frame(root, widt="600", height="80", bg= "pink")
img1 = PhotoImage(file = Int_img[0])
b1 = Button(p2, image=img1 , command=Alarme1)#text="Alarme1 OFF"
b1.pack(side = LEFT, padx = 20, pady = 20)

img2 = PhotoImage(file = Int_img[0])
b2 = Button(p2, image=img2, command= Alarme2)#text="Alarme2 ON"
b2.pack(side = LEFT, padx = 200, pady = 20)
p2.pack()


#+++++++++++++++++++++++++++++++++++++++++++
#mostrar o GUI 
root.mainloop()
