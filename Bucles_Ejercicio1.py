'''Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

i = 0

num = input('Ingrese un número para ver su tabla de multiplicar: ')

try:

    num = int(num)

    while i <= 10:

        #interacion o contador
        i += 1

        #operación matematica
        resultado = num * i

        print('{} x {} = {}'.format(num, i, resultado))

except ValueError:

    print('¡ERROR!: LOS CARACTERES INGRESADOS NO SON VALIDOS.')