from re import A


def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,       
    }
    
    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])


    poblacion = {
        'Argentina': 44000000,
        'Brasil': 225000000,
        'Colombia': 45000000,
    }

    # for x in poblacion.keys():
    #     print(x)

    # for x in poblacion.values():
    #     print(x)

    for x, t in poblacion.items(): 
        # x es el nombre dle pais y t es el numero de habitantes
        print(x + ' tiene ' + str(t) + ' habitantes')

if __name__ == "__main__":
    run()