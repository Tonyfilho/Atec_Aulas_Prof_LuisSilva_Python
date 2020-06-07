# interface gráfica

from tkinter import * # criar janela na interface grafica
from tkinter import messagebox


root  = Tk()
#root.geometry('640x480')#definicao do tamanho da janela
root.title('Gui Base Desenhar')#definicao do titulo
root.resizable(False, True)#expensao da tela

c = Canvas(root, width = 640 , height = 480 , bg =  'green')#zona grafica usa o root.geometry
c.create_oval(50, 50, 200,200, fill = 'blue')#coord superior (50,50) e coord.inferior(200,200) e fill = preenchimento do oval 
c.create_rectangle(250, 50, 300, 100, fill = 'red')
c.create_rectangle(250, 150, 300, 400, fill = 'yellow')
c.create_line(250, 410, 300, 460, fill ='black', width=8)#grossura da linha - width
c.create_line(250, 460, 300, 410, fill ='black', width=8)#grossura da linha - width
c.pack()

root.mainloop()







