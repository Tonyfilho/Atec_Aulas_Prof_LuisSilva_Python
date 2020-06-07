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
from tkinter import ttk
from time import sleep

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
          i = 0
          f = open('alarmes.dat','r')
          linha = f.readline()
          print('{} : {}'.format(i, linha ))
          while  linha != '' :
                    i += 1
                    linha = f.readline()
                    print('{} : {}'.format(i, linha))
                                    
#++++++++++++++++++++++++++++++++
def Autor():
    messagebox.showinfo('Dialogo Autor',
                        '\nName : Luis Filipe\nFunction : It Trainning\nCurso: CET´s Palmela\n\nMake the thing\'s easy')
    
#++++++++++++++++++++++++++++++++
def Linguagem():
    messagebox.showinfo('Dialogo Linguagem',
                        '\nLanguage : Python\nVersion : 3.80 ')
    
#++++++++++++++++++++++++++++++++
def Programa():
    messagebox.showinfo('Dialogo Programa',
                        '\nPrograma que mostra\na possibilidade de usar MenuBar\nnuma aplicação Python GUI(Tkinter)')
    
#++++++++++++++++++++++++++++++++
def abandonar(): 
    perg = messagebox.askquestion('Dialogo Abandonar',
                                  '\nConfirma que deseija\nabandonar a aplicação.\n')
    if perg == 'yes':
          root.destroy()

#++++++++++++++++++++++++++++++++
def Alarme1():
          global estado1
          global bt1
          global imag1
           
          estado1 = not(estado1)
          
          if estado1 == True:
                    #string da caixa de texto
                    ms1.set('ON')
                    
                    #Imagem do interruptor
                    imag1 = PhotoImage(file=Int_img[1])
                    b1.configure(image=imag1)
                    
                    #cor do led
                    c.itemconfig(al1,fill='red')
                    
                    #captura dia, data, hora
                    hoje = datetime.now()
                    data = hoje.strftime("%d-%m-%Y")
                    horas = hoje.strftime("%H:%M")
                    
                    # abrir o ficheiro para adicionar dados
                    arquivo = open('alarmes.dat','a')
                    
                    # escreve os dados por linha
                    arquivo.write('Porta 1')
                    arquivo.write(',')
                    arquivo.write(data)
                    arquivo.write(',')
                    arquivo.write(horas)
                    arquivo.write('\n')
                    
                    #fechar o ficheiro
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
                    #string da caixa de texto
                    ms2.set('ON')
                    
                    #Imagem do interruptor
                    imag2 = PhotoImage(file=Int_img[1])
                    b2.configure(image=imag2)

                    #cor do led
                    c.itemconfig(al2,fill='red')
                    
                    #captura dia, data, hora
                    hoje = datetime.now()
                    data = hoje.strftime("%d-%m-%Y")
                    horas = hoje.strftime("%H:%M")
                    
                    # abrir o ficheiro para adicionar dados
                    arquivo = open('alarmes.dat','a')

                    # escreve os dados por linha
                    arquivo.write('Porta 2')
                    arquivo.write(',')
                    arquivo.write(data)
                    arquivo.write(',')
                    arquivo.write(horas)
                    arquivo.write('\n')
                    
                    #fechar o ficheiro
                    arquivo.close()                      
          else:
                    ms2.set('OFF')
                    imag2 = PhotoImage(file=Int_img[0])
                    b2.configure(image=imag2)
                    c.itemconfig(al2,fill='orange')

#+++++++++++++++++++++++++++++++++++++++++++
#GUI
root = Tk()
root.title("Exemplo")  #Titulo
root.geometry("500x800") #Dimensão
root.resizable(False,False) #não redimensionavel


#+++++++++++++++++++++++++++++++++++++++++++
#MenuBar
menubar = Menu()

#+++++++++++++++++++++++++++++++++++++++++++
#Menu
filemenu = Menu(menubar, tearoff = 0)

#+++++++++++++++++++++++++++++++++++++++++++
#MenuItem
filemenu.add_command(label='Ler ficheiro', command = ler_ficheiro)
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

#juntar o menu a root
root.config(menu=menubar)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Notebook
note = ttk.Notebook(root)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tab 0
tab0 = Frame(note)

imagemCapa = PhotoImage(file = 'casa2_imagem.png')
lb_capa = Label(tab0, image = imagemCapa)
lb_capa.pack(side = LEFT, pady = 10)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tab 1
tab1 = Frame(note)

#+++++++++++++++++++++++++++++++++++++++++++
#painel superior
p1 = Frame(tab1, widt="600", height="80", bg= "pink")

#Label
lb1 = Label(p1, text="Alarme1", fg="blue")
lb1.pack(side=LEFT , padx=20, pady= 20)

#Caixa de Texto
ms1 = StringVar()
E1 = Entry(p1 ,textvariable = ms1)
E1.insert(END,'OFF')
E1.pack(side=LEFT, padx=20, pady = 20)

#Label
lb2 = Label(p1, text="Alarme2", fg="blue")
lb2.pack(side=LEFT , padx=20, pady= 20)

#caixa de texto
ms2 = StringVar()
E2 = Entry(p1, textvariable = ms2)
E2.insert(END,'OFF')
E2.pack(side=LEFT, padx=20, pady = 20)

#adicionar o painel
p1.pack()

#+++++++++++++++++++++++++++++++++++++++++++
#painel grafico
c = Canvas(tab1,width="600", height="630", bg="yellow")

#sem alarme
img_ps0 = PhotoImage(file = 'piso_zero.png') #imagem de fundo planta
fundo = c.create_image(20,20, image= img_ps0, anchor=NW)
al1 = c.create_oval(40,50,60,70,fill='orange')#Alarme


#sem alarme
al2 = c.create_oval(50,510,70,530,fill='orange')#Alarme
c.pack()

#+++++++++++++++++++++++++++++++++++++++++++
#painel inferior
p2= Frame(tab1, widt="600", height="80", bg= "pink")

#Imagem
img1 = PhotoImage(file = Int_img[0])

#Button
b1 = Button(p2, image=img1 , command=Alarme1)#text="Alarme1 OFF"
b1.pack(side = LEFT, padx = 80, pady = 20)

#imagem
img2 = PhotoImage(file = Int_img[0])

#Button
b2 = Button(p2, image=img2, command= Alarme2)#text="Alarme2 ON"
b2.pack(side = LEFT, padx = 100, pady = 20)

#adicionar o painel
p2.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tab 2
tab2 = Frame(note)


#Imagem da bola
img3 = PhotoImage(file='redball.gif')

#Titulo dos separadores
note.add(tab0, text='  Capa da App  ', image = img3, compound= LEFT)
note.add(tab1, text='  Planta da Habitação  ', image = img3, compound= LEFT)
note.add(tab2, text='  Registo de ocorrencias  ', image = img3, compound= LEFT)

note.pack(expand=1, fill = BOTH)

#+++++++++++++++++++++++++++++++++++++++++++
#mostrar o GUI 
root.mainloop()
