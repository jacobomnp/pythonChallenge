'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)

'''

import random

lower = "qwertyuiopasdfghjklñzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
numbers = "1234567890"
symbols = f"""|°!"#$%&/()=?¡´+[]-.,<>;:_*"""
validate = False

while validate == False:
    try:
        chars = int(input('¿Cuántos caracteres de 8 - 16?: '))
        if 7 < chars < 17:
            validate = True
        else:
            print('elija un rango de entre 8 y 16 caracteres')
    except:
        print('numero de caracteres no valido')
pwdParameters = False
while pwdParameters == False:
    password = ""
    validate = False
    while validate == False:
        carryNumber = input('incluir numeros? [y/n]: ').lower()
        if carryNumber == 'y':
            password += numbers
            validate = True
        elif carryNumber == 'n':
            validate = True
        else:
            print('seleccione una opcion')

    validate = False
    while validate == False:
        carryUpper = input('incluir mayus? [y/n]: ').lower()
        if carryUpper == 'y':
            password += upper
            validate = True
        elif carryUpper == 'n':
            validate = True
        else:
            print('seleccione una opcion')

    validate = False
    while validate == False:
        carryLower = input('incluir minus? [y/n]: ').lower()
        if carryLower == 'y':
            password += lower
            validate = True
        elif carryLower == 'n':
            validate = True
        else:
            print('seleccione una opcion')

    validate = False
    while validate == False:
        carrySymbols = input('incluir carateres especiales? [y/n]: ').lower()
        if carrySymbols == 'y':
            password += symbols
            validate = True
        elif carrySymbols == 'n':
            validate = True
        else:
            print('seleccione una opcion')
    if carryLower == 'n' and carryNumber == 'n' and carrySymbols == 'n' and carryUpper == 'n':
        print('seleccione al menos un tipo de carater')
    else:
        pwdParameters = True
passwordGenerates = "".join(random.sample(password, chars))
print(f'contraseña generada: {passwordGenerates}')