import  random


def password_de():
    upper = ['K', 'A', 'M', 'I', 'L']
    number = ['1', '0', '5', '3', '8', '6']
    lower = [ 'm', 'e', 'n', 'd', 'z']
    symbol = [',', '.', '!', '#' ]


    character = upper + lower + number + symbol

    password = []

    for i in range(8):
        # colocamos el numero 15 puesto que queremos que la password tenga 15 CHARACTERS
        # colocamos random.choice puesto que este nos ayuda a seleccionar los caracteres aleatoriamento de la lista character
        character_random = random.choice(character)
        password.append(character_random)

    password = ''. join(password)
    return password

def run():
    password = password_de()
    print('You new password is '+ password)
    


if __name__ == '__main__':
    run()
