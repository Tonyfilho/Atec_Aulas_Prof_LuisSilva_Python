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
import tk as tk
# +++++++++++++++++++++++++++++++++++++++++++
# Bibliotecas
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import tkinter as tk
import csv
from time import sleep

# +++++++++++++++++++++++++++++++++++++++++++
# dados Globais


Int_img = ['Botao_Off1_d.png', 'Botao_On1_d.png']
estado1, estado2 = False, False

dados = [];
# +++++++++++++++++++++++++++++++++++++++++++
# Metodos
def donothing():
    pass


# ++++++++++++++++++++++++++++++++
def ler_ficheiro():
    i = 0
    f = open('alarmes.dat', 'r')
    linha = f.readline()
    print('{} : {}'.format(i, linha))
    while linha != '':
        i += 1
        linha = f.readline()
        print('{} : {}'.format(i, linha))


# ++++++++++++++++++++++++++++++++
def Autor():
    messagebox.showinfo('Dialogo Autor',
                        '\nName : Luis Filipe\nFunction : It Trainning\nCurso: CET´s Palmela\n\nMake the thing\'s easy')


# ++++++++++++++++++++++++++++++++
def Linguagem():
    messagebox.showinfo('Dialogo Linguagem',
                        '\nLanguage : Python\nVersion : 3.80 ')


# ++++++++++++++++++++++++++++++++
def Programa():
    messagebox.showinfo('Dialogo Programa',
                        '\nPrograma que mostra\na possibilidade de usar MenuBar\nnuma aplicação Python GUI(Tkinter)')


# ++++++++++++++++++++++++++++++++
def abandonar():
    perg = messagebox.askquestion('Dialogo Abandonar',
                                  '\nConfirma que deseija\nabandonar a aplicação.\n')
    if perg == 'yes':
        root.destroy()


# ++++++++++++++++++++++++++++++++
def Alarme1():
    global estado1
    global bt1
    global imag1

    estado1 = not (estado1)

    if estado1 == True:
        # string da caixa de texto
        ms1.set('ON')

        # Imagem do interruptor
        imag1 = PhotoImage(file=Int_img[1])
        b1.configure(image=imag1)

        # cor do led
        c.itemconfig(al1, fill='red')
        c.itemconfig(al3, fill='red')

        # captura dia, data, hora
        hoje = datetime.now()
        data = hoje.strftime("%d-%m-%Y")
        horas = hoje.strftime("%H:%M")

        # abrir o ficheiro para adicionar dados
        arquivo = open('alarmes.dat', 'a')

        # escreve os dados por linha
        arquivo.write('Porta 1 Porta 3')
        arquivo.write(',')
        arquivo.write(data)
        arquivo.write(',')
        arquivo.write(horas)
        arquivo.write('\n')

        # fechar o ficheiro
        arquivo.close()
    else:
        ms1.set('OFF')
        imag1 = PhotoImage(file=Int_img[0])
        b1.configure(image=imag1)
        c.itemconfig(al1, fill='orange')
        c.itemconfig(al3, fill='orange')


# ++++++++++++++++++++++++++++++++
def Alarme2():
    global estado2
    global bt2
    global imag2

    estado2 = not (estado2)

    if estado2 == True:
        # string da caixa de texto
        ms2.set('ON')

        # Imagem do interruptor
        imag2 = PhotoImage(file=Int_img[1])
        b2.configure(image=imag2)

        # cor do led
        c.itemconfig(al2, fill='red')
        c.itemconfig(al4, fill='red')

        # captura dia, data, hora
        hoje = datetime.now()
        data = hoje.strftime("%d-%m-%Y")
        horas = hoje.strftime("%H:%M")

        # abrir o ficheiro para adicionar dados
        arquivo = open('alarmes.dat', 'a')

        # escreve os dados por linha
        arquivo.write('Porta 2, Porta 4')
        arquivo.write(',')
        arquivo.write(data)
        arquivo.write(',')
        arquivo.write(horas)
        arquivo.write('\n')

        # fechar o ficheiro
        arquivo.close()
    else:
        ms2.set('OFF')
        imag2 = PhotoImage(file=Int_img[0])
        b2.configure(image=imag2)
        c.itemconfig(al2, fill='orange')
        c.itemconfig(al4, fill='orange')


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++Show
def show():
    lista = []  # você só precisa de uma lista - ela é uma matriz multidimensional

    with open('alarmes.dat', newline='') as csvfile:
        # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
        spamreader = csv.reader(csvfile, delimiter=',')  # separe por vírgula

        # o módulo csv detectará novas linhas automaticamente
        for i in spamreader:
            lista.append(i)

    # os elementos começam ser contados em zero, i.e. lista[0][1] == 'julian'
    print(lista[1])  # imprime a linha 2 da lista, inteira
    print(lista[2])  # imprime apenas o segundo item da linha 2




    for i in lista:
        Data = i[2]
        Hora = i[0]
        Sensor = i[1]
        listBox.insert("", "end", values=(i, Sensor, Data, Hora))




# +++++++++++++++++++++++++++++++++++++++++++
# GUI
root = Tk()
root.title("Alarme Atec")  # -------------------------------------Titulo
root.geometry("1000x700")  # -------------------------------------Dimensão total da TELA
root.resizable(True, True)  # ---------------------------------- redimensionavel

# +++++++++++++++++++++++++++++++++++++++++++
# MenuBar
menubar = Menu()

# +++++++++++++++++++++++++++++++++++++++++++
# Menu
filemenu = Menu(menubar, tearoff=0)

# +++++++++++++++++++++++++++++++++++++++++++
# MenuItem
filemenu.add_command(label='Ler ficheiro', command=ler_ficheiro)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=abandonar)

# Titulo do Menu
menubar.add_cascade(label='File', menu=filemenu)

# Menu filehlp
filehlp = Menu(menubar, tearoff=0)

# MenuItem
filehlp.add_command(label='Programa', command=Programa)
filehlp.add_command(label='Linguagem', command=Linguagem)
filehlp.add_separator()
filehlp.add_command(label='Autor', command=Autor)

# Titulo do Menu
menubar.add_cascade(label='Help', menu=filehlp)

# juntar o menu a root
root.config(menu=menubar)

# juntar o menu a root
root.config(menu=menubar)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Notebook
note = ttk.Notebook(root)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab0 ----------------------------------------------------------------imagem da capa
tab0 = Frame(note)

imagemCapa = PhotoImage(file='casa2_imagem.png')
lb_capa = Label(tab0, image=imagemCapa)
lb_capa.pack(side=LEFT, pady=10)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab 1
tab1 = Frame(note)



# +++++++++++++++++++++++++++++++++++++++++++
# painel superior--------------------------------------1ºpainel da planta abitação
p1 = Frame(tab1, width="1200", height="40", bg="black")

# Label
lb1 = Label(p1, text="Alarme1", fg="blue")
lb1.pack(side=LEFT, padx=20, pady=20)

# Caixa de Texto
ms1 = StringVar()
E1 = Entry(p1, textvariable=ms1)
E1.insert(END, 'OFF')
E1.pack(side=LEFT, padx=20, pady=20)

# Label
lb2 = Label(p1, text="Alarme2", fg="blue")
lb2.pack(side=LEFT, padx=20, pady=20)

# caixa de texto
ms2 = StringVar()
E2 = Entry(p1, textvariable=ms2)
E2.insert(END, 'OFF')
E2.pack(side=LEFT, padx=20, pady=20)

# adicionar o painel
p1.pack()

# +++++++++++++++++++++++++++++++++++++++++++
# --------------------------------------------------------------------painel grafico01
c = Canvas(tab1, width="1200", height="550", bg="blue")

# sem alarme
img_ps0 = PhotoImage(file='piso_zero.png')  # imagem de fundo planta
fundo = c.create_image(170, 20, image=img_ps0, anchor=NW)#--------------------------ALTERADO
al1 = c.create_oval(200, 50, 220, 70, fill='orange')  # -----------------------------Alarme

# sem alarme
al2 = c.create_oval(210, 510, 230, 530, fill='orange')  # Alarme
#c.pack()

#---------------------------------------------------painel grafico02
# sem alarme
img_ps1 = PhotoImage(file='piso_um.png')  # imagem de fundo planta
fundo = c.create_image(620, 20, image=img_ps0, anchor=NW)#--------------------------ALTERADO
al3 = c.create_oval(660, 50, 680, 70, fill='orange')  # --------------------------------Alarme

# sem alarme
al4 = c.create_oval(670, 510, 690, 530, fill='orange')  # Alarme
c.pack()

# +++++++++++++++++++++++++++++++++++++++++++



# -----------------------------------------------------------------------painel inferior
p2 = Frame(tab1, width="1200", height="80", bg="black")

# Imagem
img1 = PhotoImage(file=Int_img[0])

# Button
b1 = Button(p2, image=img1, command=Alarme1)  # text="Alarme1 OFF"
b1.pack(side=LEFT, padx=80, pady=20)

# imagem
img2 = PhotoImage(file=Int_img[0])

# Button
b2 = Button(p2, image=img2, command=Alarme2)  # text="Alarme2 ON"
b2.pack(side=LEFT, padx=100, pady=20)

# adicionar o painel
p2.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab 2-----------------------------------------------------------------Registro de Ocorrências
tab2 = Frame(note)
p3 = Frame(tab2, width="1000", height="200", bg="")
#tabela = Label(p3, command=ler_ficheiro())

#----------------------------------------------------------------------------fim do teste
p3.pack()#------------------------------------------------------------fim do p3.tab2
#-------------------------------------------------------------------inicio do C.canvas.Tab02
d = Canvas(tab2, width="1200", height="550", bg="black")
label = tk.Label(d, text="Tabela de Eventos de Alarme", font=("Arial", 20)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Local do Alarme', 'Data', 'Hora')
listBox = ttk.Treeview(d, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)
showScores = tk.Button(d, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(d, text="Close", width=15, command=exit).grid(row=4, column=1)


d.pack()
# Imagem da bola
img3 = PhotoImage(file='redball.gif')

# Titulo dos separadores
note.add(tab0, text='  Capa da App  ', image=img3, compound=LEFT)
note.add(tab1, text='  Planta da Habitação  ', image=img3, compound=LEFT)
note.add(tab2, text='  Registo de ocorrencias  ', image=img3, compound=LEFT)

note.pack(expand=1, fill=BOTH)

# +++++++++++++++++++++++++++++++++++++++++++
# mostrar o GUI
root.mainloop()

