'''Ejercicio 3

Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''

palabra1 = input('Ingresa una palabra: ')

palabra2 = input('Ingresa otra palabra: ')

try: 

    #Se comprueba que si es un número no realice avance el programa.
    prueba1 = int(palabra1)

    prueba2 = int(palabra2)

    print('¡¡ERROR!!: LOS CARACTERES INGRESADOS NO SON VALIDOS.')

#Si comprueba que no es un conjunto de números entonces realiza ya el programa.

except ValueError:

    if palabra1[-3 : ] == palabra2[-3 : ]:

        print('{} y {} Si riman.'.format(palabra1, palabra2))

    elif palabra1[-2 : ] == palabra2[-2 : ]:

        print('{} y {} riman un poco.'.format(palabra1, palabra2))
    
    else:

        print('{} y {} No riman'.format(palabra1, palabra2))



    