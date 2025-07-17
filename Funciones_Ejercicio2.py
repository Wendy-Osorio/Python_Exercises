'''Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial.'''

#Se importa la bibloteca de math
import math

def factorial():

    #Se le pide un número al usuario
    num = input('Ingrese un número para saber su factorial: ')


    try:

        #Se verifica que el valor ingresado por el usuario sea un número entero positivo
        num = int(num)

        #Se imprime el factorial
        print('El factorial de {}! es: {}'.format(num, math.factorial(num)))
        
        repetir()

    except ValueError:

        #En caso de que los caracteres ingresados por el usuario no sean un número entonces regresa a la función factorial()
        print('LOS VALORES INGRESADOS NO SON VALIDOS... INTENTELO NUEVAMENTE\n')

        factorial()

def repetir():

    resp = input('¿Desea conocer el factorial de otro número? (S/N): ')

    if resp.lower() == 's':

        num = 0

        factorial()

    if resp.lower() == 'n':

        print('Saliendo del programa...')

        exit()

    else:

        #En caso de que los caracteres ingresados por el usuario no sean un número entonces regresa a la función factorial()
        print('LOS VALORES INGRESADOS NO SON VALIDOS... INTENTELO NUEVAMENTE\n')

        repetir()
    

factorial()

