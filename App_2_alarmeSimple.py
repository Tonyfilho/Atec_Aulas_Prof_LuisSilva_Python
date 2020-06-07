'''
1- possibilidade
tenho a parede, a janela e o alarme
a primeira como diz as legendas não há alarme
a segunda como diz a legenda há alarme
o que muda é a cor do led.


versao 2
os interruptores são substituidos por imagens
de interruptores
'''

Int_img = ['Botao_Off1_d.png','Botao_On1_d.png']


estado1 , estado2 = False, False

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
          else:
                    ms1.set('OFF')
                    imag1 = PhotoImage(file=Int_img[0])
                    b1.configure(image=imag1)
                    c.itemconfig(al1,fill='green')
                    

def Alarme2():
          pass

from tkinter import *

root = Tk()
root.title("Exemplo")
root.geometry("600x480")
root.resizable(False,False)

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
E2.insert(END,'ON')
E2.pack(side=LEFT, padx=20, pady = 20)

p1.pack()

#painel grafico
c = Canvas(root,width="600", height="320", bg="yellow")

#sem alarme
linha  = c.create_line(50,150,550,150, fill = "black", width=10, dash=(6,6))#Parede
linha2 = c.create_line(100,148,200,148, fill = 'gray', width=20)#janela
al1 = c.create_oval(130,130,170,170,fill='green')#Alarme

#com alarme
linha3 = c.create_line(400,148,500,148, fill = 'gray', width=20)#janela
al2 = c.create_oval(430,130,470,170,fill='red')#Alarme
c.pack()

#painel inferior
p2= Frame(root, widt="600", height="80", bg= "pink")
img1 = PhotoImage(file = Int_img[0])
b1 = Button(p2, image=img1 , command=Alarme1)#text="Alarme1 OFF"
b1.pack(side = LEFT, padx = 20, pady = 20)

img2 = PhotoImage(file = Int_img[1])
b2 = Button(p2, image=img2, command= Alarme2)#text="Alarme2 ON"
b2.pack(side = LEFT, padx = 200, pady = 20)
p2.pack()

root.mainloop()
