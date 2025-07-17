'''Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''


vocal = input('Ingresa una vocal en minuscula: ')

letra = input('Ingresa una letra en mayusculas: ')

vocales = ['a', 'e', 'i', 'o', 'u']

if (vocal in vocales and letra.isupper()):

    print('Tú vocal fue:',vocal.upper(), '\nY tu letra fue:', letra.lower())

else:
    print('ERROR: LOS DATOS INGRESADOS NO SON CORRECTOS')

    exit()

