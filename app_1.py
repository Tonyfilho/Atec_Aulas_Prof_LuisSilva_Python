'''
1- possibilidade
tenho a parede, a janela e o alarme
a primeira como diz as legendas não há alarme
a segunda como diz a legenda há alarme
o que muda é a cor do led.

'''

estado1 , estado2 = False, False

def Alarme1():
          global estado1
           
          estado1 = not(estado1)
          if estado1 == True:
                    ms1.set('ON')
                    b1.configure(text="Alarme1 ON")
                    c.itemconfig(al1,fill='red')
          else:
                    ms1.set('OFF')
                    b1.configure(text="Alarme1 OFF")
                    c.itemconfig(al1,fill='green')
                    

def Alarme2():
          pass

from tkinter import *

root = Tk()
root.title("Exemplo")
root.geometry("600x480")

#painel superior
p1 = Frame(root, widt="600", height="80", bg= "pink")

lb1 = Label(p1, text="Alarme1", fg="blue")
lb1.pack(side=LEFT , padx=20, pady= 20)

ms1 = StringVar()
E1 = Entry(p1 ,textvariable = ms1)
E1.insert(END,'OFF')
E1.pack(side=LEFT, padx=20, pady = 20)

lb2 = Label(p1, text="Alarme2", fg="blue")
lb2.pack(side=LEFT , padx=20, pady= 20)

ms2 = StringVar()
E2 = Entry(p1, textvariable = ms2)
E2.insert(END,'ON')
E2.pack(side=LEFT, padx=20, pady = 20)

p1.pack()

#painel grafico
c = Canvas(root,width="600", height="320", bg="yellow")

#sem alarme
linha  = c.create_line(50,150,550,150, fill = "black", width=5, dash=(4,4))#Parede
linha2 = c.create_line(100,148,200,148, fill = 'gray', width=20)#janela
al1 = c.create_oval(130,130,170,170,fill='green')#Alarme

#com alarme
linha3 = c.create_line(400,148,500,148, fill = 'gray', width=20)#janela
al2 = c.create_oval(430,130,470,170,fill='red')#Alarme
c.pack()

#painel inferior
p2= Frame(root, widt="600", height="80", bg= "pink")
b1 = Button(p2, text="Alarme1 OFF", command=Alarme1)
b1.pack(side = LEFT, padx = 20, pady = 20)

b2 = Button(p2, text="Alarme2 ON", command= Alarme2)
b2.pack(side = LEFT, padx = 60, pady = 20)
p2.pack()

root.mainloop()
