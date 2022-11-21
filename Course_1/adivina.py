import random 


def run():
    numero_al = random.randint(1, 100)
    numero_usuario = int(input('Escribe una numero del 1 al 100: '))
    while numero_usuario != numero_al:
        if numero_usuario < numero_al:
            print('Busca un numero mayor: ')
        else:
            print('Busca un numero menor ')
        numero_usuario = int(input(' Elige otro numero: '))   
    print("!Ganaste!")
    

if __name__ == '__main__':
    run()