'''Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''


meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

numero = input('Ingrese un número del 1 al 12: ')

try:

    numero = int(numero)

    if numero > 0 and numero <= 12:
            
        print('Ingresaste el número {} que corresponde al mes de: {}'.format(numero, meses[numero - 1]))
        
    else:

        print('El valor que ingreso no pertenece a ningun mes del año.')

except ValueError:

    print('¡ERROR!: LOS CARACTERES INGRESADOS NO SON VALIDOS.')



