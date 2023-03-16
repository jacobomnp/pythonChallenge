'''
RETO 1
Escribe un programa que muestre por consola los numeros
del 1 al 100 (ambos incluidos y con un salto de línea entre cada impresión)
sustituyendo:
-Multiplos de 3 por la palabra 'fizz'
- multiplos de 5 por la palabra 'buzz'
- multiplos de 3 y de 5 a la vez por la palabra 'fizzbuzz
'''

def fizzbuzz(numero):
    for i in range(1, numero+1):
        if (i % 5 == 0) and (i % 3 == 0):
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)

fizzbuzz(100)
