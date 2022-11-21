# menu = '''
# Bienvenidos al conversor de monedas

# 1 - Dolares
# 2 - Pesos colombianos
# 3 - Pesos argentinos
# 4 - Euros

# Elige una opcion:
# '''

# opcion = input(menu)

# if opcion == '1':
#     Dolares= input('Cuantos dolares tienes:')
#     Dolares= float(Dolares)
#     eth= 1114
#     eth= eth / Dolares
#     eth= str(eth)
#     print(' Tienes '+ eth + 'ETH')
# elif opcion== '2':
#     Dolares= input(' Cuantos pesos colombianos tiene:')
#     Dolares= float(Dolares)
#     eth=4365000
#     eth= eth / Dolares
#     eth= str(eth)
#     print( ' Tienes '+ eth + 'Eth')
# elif opcion== '3':
#     Dolares = input(' Cuantos pesos argentinos tienes:')
#     Dolares= float(Dolares)
#     eth=137000
#     eth= eth / Dolares
#     eth= str(eth)
#     print(' Tienes ' + eth + ' ETH')
# elif opcion== '4':
#     Dolares= input('Cuantos Euros tienes:')
#     Dolares= float(Dolares)
#     eth= 1069
#     eth = eth / Dolares
#     eth= str(eth)
#     print(' Tienes '+ eth + ' ETH')
# else:
#     print('Elige una opcion correcta')


def conversor(tipo_moneda, eth):
    Moneda= input(' Cuantos '+ tipo_moneda + ' tienes:')
    Moneda= float(Moneda)
    eth= Moneda / eth
    eth= str(eth)
    print('Tienes ' + eth + ' ETH')


menu='''
Bienvenido al conversor de monedad

1 - Dolares
2 - Pesos Colombianos
3 - Euros
4 - Pesos Argentinos

Elige una opcion:'''

opcion= int(input(menu))

if opcion== 1:
    conversor('Dolares', 1114)
elif opcion == 2:
    conversor('Pesos Colombianos', 4365000)
elif opcion== 3:
    conversor('Euros', 1069)
elif opcion== 4:
    conversor('Pesos Argentinos', 137000)
else:
    print('Elige una opcion correcta')
