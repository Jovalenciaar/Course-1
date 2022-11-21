# def run():
#     # for x in range (20):
#     #     if x % 2 != 0 :
#     #         continue
#     #     print(x)

#     # for i in range(20):
#     #     print(i)
#     #     if i == 16:
#     #         break

#     texto = input('Escribe un texto:')
#     for letra in texto:
#         if letra == 'l':
#             break
#         print(letra)  


# if __name__ == '__main__':
#     run() 


def run():
    LIMITE = 200

    numero = int(input('Escribe un numero:'))
    # numero = numero * 2
    
    # for numero in range(2000):
    #     if numero % 2 !=0:
    #         continue
    #     print(numero)
        
    
    while numero < LIMITE:
        numero = numero * 2
        if numero == 110:
            break
            print(numero)        
    

if __name__ == "__main__":
    run()
