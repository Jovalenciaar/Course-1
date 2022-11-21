# # CONVERSOR DE MONEDA 1 EJERCICIO
# # def run():
#     pesos_col = int(input('Cuantos Pesos colombianos tienes?: '))
#     dolares = 3875
#     cantida_dol = pesos_col / dolares
#     # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
#     cantida_dol = round(cantida_dol, 3)
#     cantida_dol = str(cantida_dol)
#     print('Tienes $ ' + cantida_dol + ' Dolares ')


# if __name__ == '__main__':
#     run()

# ---------------------------------------------------------------------------------------------------------------

# def run():
#     menu = '''
#     Bienvenidos al conversor de monedas

#     Elige una opcion:
    
#     1 - BTC
#     2 - ETH
#     3 - Pesos Colombianos
        
#     '''

#     option = int(input(menu))
#     if option == 1:
        # BTC = int(input('Cuantos BTC tienes?: '))
        # valor_BTC = 21000
        # cantida_BTC = BTC * valor_BTC
        # # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
        # cantida_BTC = round(cantida_BTC, 3)
        # cantida_BTC = str(cantida_BTC)
        # print('Tienes $ ' + cantida_BTC + ' Dolares ')
#     elif option == 2:
#         ETH = int(input('Cuantos ETH tienes?: '))
#         valor_ETH = 1200
#         cantidad_ETH = ETH * valor_ETH
#         # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
#         cantidad_ETH = round(cantidad_ETH, 3)
#         cantidad_ETH = str(cantidad_ETH)
#         print('Tienes $ ' + cantidad_ETH + ' Dolares ')
#     elif option == 3:
#         pesos_col = int(input('Cuantos Pesos colombianos tienes?: '))
#         dolares = 3875
#         cantida_dol = pesos_col / dolares
#         # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
#         cantida_dol = round(cantida_dol, 3)
#         cantida_dol = str(cantida_dol)
#         print('Tienes $ ' + cantida_dol + ' Dolares ')
#     else:
#         print('Elige una opcion correcta ')


# if __name__ == '__main__':
#     run()

# -----------------------------------------------------------------------------------------------------------------

# def run ():
    
#     # SE TIENE QUE DEFINIR UNA FUNCION PARA QUE ESTA SE PUEDA CORRER Y NO TENGAMOS QUE REPETIR LOS MISMO
#     # SE CREA UN FUNCION Y DENTRO DE LOS PARENTESIS COLOCAMOS LAS DOS VARIABLES QUE NECESITAMOS
#     def conversor( tipo_moneda, valor):
#         moneda = int(input('Cuantos ' + tipo_moneda +  ' tienes?: '))
#         cantidad  = moneda * valor
#         # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
#         cantidad = round(cantidad, 3)
#         cantidad = str(cantidad)
#         print('Tienes $ ' + cantidad+ ' Dolares ')

#     def conversor_2( tipo_moneda, valor):
#         moneda = int(input('Cuantos ' + tipo_moneda +  ' tienes?: '))
#         cantidad  = moneda / valor
#         # COLOCAMOS ROUND PARA ESPECIFICAR EL NUMERO DE DECIMALES QUE QUEREMOS VER, EN ESTE CASO 3
#         cantidad = round(cantidad, 3)
#         cantidad = str(cantidad)
#         print('Tienes $ ' + cantidad+ ' Dolares ')
    
    
#     menu = '''
#     Bienvenidos al converos de monedas
    
#     1 - BTC
#     2 - ETH 
#     3 - Pesos Colombianos
    
#     ELige un opcion: 
#     '''

#     option = int(input(menu))
#     if option == 1:
#         conversor('BTC', 21000)
#     elif option ==2:
#         conversor('ETH', 1200)
#     elif option == 3:
#         conversor_2('Pesos Colombianos', 3875)
#     else:
#         print('Elige una opcion correcta. ')

       

# if __name__ =='__main__':
#     run()

#RETUN  ------------------------------------------------------------
# def suma(a, b):
#     print('Se suman dons numeros')
#     resultado = a + b
#     return resultado

# sumatorio = suma (1, 4)
# print(sumatorio)
# ------------------------------------------------------------

# # PALINDROMO

# def palidromo(palabra):


#     palabra = palabra.lower()
#     palabra = palabra.replace(' ', '')
#     palabra_inv = palabra[::-1]
#     if palabra == palabra_inv:
#         return True
#     else:
#         return False


# def run():
     
        
#     palabra = str(input('Escribe una palabra: '))
#     es_pal = palidromo(palabra)
#     if es_pal == True:
#         print('Es palindromo')
#     else:
#         print('No es palindromo')


# if __name__ == '__main__':
#     run()

# --------------------------------------------------------------------------------------------

# BUCLES


# def run():
#     LIMITE = 10000

#     x = 0
#     potencia_2 = 2 ** x
#     while potencia_2 < LIMITE:
#         print(' 2 elevado a ' + str(x) + ' es igual a: ' + str(potencia_2))
#         # Colocamos x +=1 para que x vaya sumando 1 digito cada vez mas,
#         # pero para cerrar el bucle tenemos que volver a definir la variable potenci_2
#         x += 1
#         potencia_2 = 2 ** x


# if __name__ == '__main__':
#     run()

#-------------------------------------------------------------------------------
# TABLA DE MULTIPLICAR

# def run():
    

#     tabla = int(input('Que tabla quieres saber: '))
#     for x in range(1, 11):
#         print(str(tabla) + '*' +str(x) + '=' + str(tabla * x))
         

# if __name__ == '__main__':
#     run()
# # _--------------------------------------------------------------------------



# def tabla(x):
#     for contador in range (1, 11):
#         print(str(x) + ' * ' + str(contador) + ' = ' + str(x * contador))
#     #    SE TIENE QUE PONER OTRA VARIABLE EN ESTE CASO CONTADOR PARA QUE ESTE VAYA INCREMENTADO

# def run():
     
    
#     menu = '''
    
#     Bienvenidos a las tablas de multiplicar
    
#     Elige un opcion:
    
#     A - Tabla del 1
#     B - Tabla del 2
#     C - Tabla del 3
#     D - Tabla del 4
#     E - Tabla del 5
#     F - Tabla del 6
#     G - Tabla del 7 
#     H - Tabla del 8
#     I - Tabla del 9
#     J - Tabla del 10 

#     '''

#     option = input(menu)
#     if option == 'A':
#         tabla(1)
#     elif option == 'B':
#         tabla(2)
#     elif option == 'C':
#         tabla(3)
#     elif option == 'D':
#         tabla(4)
#     elif option == 'E':
#         tabla(5)
#     elif option == 'F':
#         tabla(6)
#     elif option == 'G':
#         tabla(7)
#     elif option == 'H':
#         tabla(8)
#     elif option == 'I':
#         tabla(9)
#     elif option == 'J':
#         tabla(10)
#     else:
#         print('Elige una opcion')


# if __name__ =='__main__':
#     run()

# ----------------------------------------------------------------------------------------------------------

# def run():
#     for i in range (100):
#         if i % 2 != 0:
#             continue
#         print(i)
#         if i == 46:
#             break

# if __name__ == '__main__':
#     run()
# --------------------------------------------------------------------------------------------------------------

# VIDEO JUEGO ADIVINA

import random

def run():
    numero_comp = random.randint(1, 30)
    numero_elegido = int(input('Elige un numero del 1 al 30 :  Tendras 5 vidas '))
    vidas = 5
    while numero_elegido != numero_comp:    
        if numero_elegido > numero_comp:
            print('Elige un numero menor, tienes ' + str(vidas) + ' vidas')
        else:
            print('Elige un numero mayor, tienes ' + str(vidas) + ' vidas')
        numero_elegido = int(input('Elige otro numero: '))
        vidas -=1
        if numero_comp == numero_elegido:
            print ('Ganaste!! ' + ' el numero ha adivinar era: ' + str(numero_comp))
            break
        if vidas == 0:
            print('Game over, tienes ' + str(vidas) + ' vidas, ' + ' el numero ha adivinar era: ' + str(numero_comp) )
            break


if __name__ == '__main__':
    run()

#   ---------------------------------------------------------------------------------------------------------------------------  

# ALMACENAR LISTAS
# LAS LISTAS SE GUARDAN CON [], EN ESTAS LISTAS SE SEPARAN LOS OBJETOS CON UNA COMA

# numero = [2, 4, 6, 8, 10, 'numero enteros']

# ******PARA ACCEDER AL OBEJTO NUMERO '6' TENGO QUE SELECIONAR EL OBJETO NUEMRO 3 EJEMPLO:
 
# numero [3] = 6

# *****SI QUIERO AGREGAR UN OBEJTO A MI LISTA: 

# CON EL METODO (.APPEND(ELEMENTO QUE QUIERO AGREGAR)) EJEMPLO:

# numero.append(14) = numero = [ 2, 4, 6, 8, 10, 'numero enteros', 14]

# ******SI QUIERO BORRAR UN ELEMENTO U OBJETO ESTO SE HACE CON EL METODO (.POP(# DEL INDICE QUE QUIERO BORRAR))
# EJEMPLO:

# Quiero borrar el objeto '4' que esta en el indice 1.enumerate

# numero.pop(1) = se elimina el objeto ue esta en el indice 1 y este caso es el nuemro '4'

# numero =[2, 6, 8, 10, 'numero enteros']

# =======================================================================================================

# def run():
#     diccionario = {
#         'Argentina'   : 1200,
#         'Colombia'    : 4000,
#         'Mexico'      : 21000,

#         LLAVE(NOMBRE) : VALOR
#     }

# # # LA LLAVE EN ESTE CASO SERIA EL NOMBRE DE NUESTRAS MONEDAS (BTC - ETH - DOLAR), SI QUEREMOS ACCEDER AL CONTENIDO
# #     QUE TIENE LA LLAVE 1 EN ESTE CASO 'BTC' COLOCAMOS IMPRIMIR DICCIONARIO Y EN LLAVE EL NOMBRE DE LA LLAVE QUE QUEREMOS 
    
    
#     # print(diccionario['valor_BTC'])
#     # for pais in diccionario.keys(): ES PARA VER EL NOMBRE DE LA LLAVE EN ESTE CASO LOS PAISES

#     # for pais in diccionario.values():ES PARA VER EL VALOR DE CADA LLAVE EN ESTE CASO (1.200- 4.000 - 21.000)

#     # for pais, poblancion in diccionario.items(): ES PARA VER EL TOTAL DE MIS OBJETOS EN diccionario NOMBRE Y VALOR
#     #     print(pais, poblancion)


# if __name__ =="__main__":
#     run()
# ============================================================================================

# import random

# def general_password():
#     mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
#     minisculad = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#     numero = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     caracter = ['@', '#', '$', '%', '^', '&', '*']

#     general = mayuscula + minisculad + numero + caracter

#     password = []

#     for i in range(15):
#         general_random = random.choice(general)
#         password.append(general_random)

#     password = ''.join(password)
#     return password

    
# def run():
#     password = general_password() 
#     print("Tu nueva password es: " + password)

# if __name__ == '__main__':
#     run()