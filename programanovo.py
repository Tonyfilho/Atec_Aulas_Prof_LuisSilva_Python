'''
Nosso primeiro programa

'''

#Dados globais
escolha = 0
acabou = False
menu = ['\t0 - Abandonar' , '\t1- Admitir', '\t2 - Calcular' , '\t3 - Mostrar']
num1, num2, resul = 0 , 0 , 0

# funcoes
def admitir(st):
    j = int(input(st))
    return j

    
def calcular(x,  y):
    return x ** y

   
def mostrar(x,  y, z):
    print('%d = %d ** %d' % (z, x, y))


def mostrar_menu(nm):
    for k in menu:
        print('%s' % (k))
    t = int(input('escolha : '))  
    return t

def ler_menu(x):
        global num1 , num2, resul
        if x == 0:
               #abandonar
               print('%s' % ('\tAbandonar App'))
               fim = True
        elif x == 1:
            #admtir
                num1 = admitir('\t Insira um inteiro: ')
                num2 = admitir('\t Insira outro numero inteiro: ')
                fim = False
        elif x == 2:
            # calcular
                resul = calcular(num1, num2)
                print('\t %s\n' % ('Calculo realizado'))
                fim = False
        elif x == 3:
            #mostrar
                mostrar(num1, num2, resul)
                fim = False
        else:
            #default
                print('\n\t%s\n' % ('Valores entre 0  e 3'))
                fim = False
        return fim
        

# main
while acabou == False:
    escolha = mostrar_menu(menu)
    acabou = ler_menu(escolha)
