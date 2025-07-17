'''Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. 
Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''

alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


numero = input('Ingrese un número del 1 al 27: ')

try:

    numero = int(numero)

    if numero > 0 and numero <= 27:
            
        print('Ingresaste el número "{}" que corresponde a la letra: "{}"'.format(numero, alfabeto[numero - 1]))
        
    else:

        print('El valor que ingreso no esta entre el rango de letras que contiene el abecedario.')

except ValueError:

    print('¡ERROR!: LOS CARACTERES INGRESADOS NO SON VALIDOS.')

