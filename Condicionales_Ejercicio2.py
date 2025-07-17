'''Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), 
mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).'''

numero = input('Ingresa un número: ')

try: 

    entero = int(numero)

    if entero >= 0:

        print('El valor absoluto de {} es: {}'.format(entero, entero))
    
    else:

        absoluto_negativo = entero * -1

        print('El valor absuluto de {} es: {}'.format(entero, absoluto_negativo))

except ValueError:

    print('¡¡ERROR!!: EL VALOR O LOS CARACATERES INGRESADOS NO SON NÚMEROS ENTEROS.')

