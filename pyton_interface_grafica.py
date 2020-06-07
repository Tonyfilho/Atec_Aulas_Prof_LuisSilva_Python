# interface gráfica

from tkinter import * # criar janela na interface grafica
from tkinter import messagebox


root  = Tk()
root.geometry('640x480')#definicao do tamanho da janela
root.title('Gui Demo')#definicao do titulo
root.resizable(False, True)#expensao da tela

def donothing():#funcao do  comando botao
    messagebox.showinfo('Titulo', 'Mensagem:  ')#criando caixa de mensagem


#tipos de layout:
#pack = coordenadas
#grid = linha e coluna
#place = x, y


#rotulo
l = Label(root, text='Ele é uma label', fg  ='white' , bg  ='blue' )
l.pack(side = LEFT)

#botoes
b = Button(root, text='Pressione este botão' ,  command = donothing)#criando botão
b.pack(side = LEFT)

#entry - caixas de textos
t = Entry(root, width=10 )
t.pack(side = LEFT)


root.mainloop()







