#funcoes
'''Sintaxe da funcao
#def nome(argumentos - dados locais) :
            acoes
            pode ter ou nao
            return qualquer coisa
            funcoes: tipo procedimentos nao devolve (void) e sub programas do tipo funcao devolve alguma coisa

'''

def potencia(a, b) :
        return a ** b

def main():
   print('%d' % (potencia(2,7)))


def mostra(x):
    print('%d' % (x))

def main2():
    y=potencia(2,7)
    mostra(y)

main()
main2()

