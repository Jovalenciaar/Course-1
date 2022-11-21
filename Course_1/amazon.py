def conversor(tipo_moneda, btc):
    dolares = input(" Cuantos " + tipo_moneda + " tienes?: ")
    dolares = float (dolares)
    numero_btc = dolares / btc
    numero_btc = str(numero_btc)
    print(" Tienes " + numero_btc +  " BTC " )

menu =  """
Bienvenido al conversor de monedas 💲

1 - Dolares
2 - Euro 
3 - Pesos argentinos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Dolares", 21000)
elif opcion == 2:
    conversor("Euro", 18000)
elif opcion ==  3:
    conversor("Pesos argentinos", 2400000)    
else:
    print("Ingresa una opcion correcta por favor")




