'''Ejercicio 3

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros 
y mostrar el rango de numeros entre ambas cifras'''

#Se imprime el rango del 1 al 10
print('Rango:')

for i in range(1, 11):

    print(i)

#Se le pide al usuario que ingrese los datos necesarios para conocer su rango entre los ya mostrados
num1 = input('\nIngrese el primer número para conocer su rango: ')

num2 = input('\nIngrese el segundp número para conocer su rango: ')

#Se le pide al programa que realice la sentencia que sera clave para el programa
try:

    #Se verifica que el string ingresado sea de tipo númerico
    num1 = int(num1)

    num2 = int(num2)

    #Se comprueba si los números ingresados son negativos y que no corresponden al rango ya mostrado
    if num1 < 0 or num2 < 0:

        #Se comprueba si segundo número es mayor al primer número
        if num1 > num2:

            #Se imprime el mensaje correspondiente
            print('!ERROR!: LOS DATOS INGRESADOS NO CORRESPONDEN AL RANGO PREVIAMENTE MOSTRADO.')

        else:
            
            #En caso de que el segundo número no sea mayor al primer número entonces se imprime el siguiente mensaje
            print('!ERROR!: LOS DATOS INGRESADOS NO CORRESPONDEN AL RANGO PREVIAMENTE MOSTRADO.')

    #Si los números ingresados no son negativos entonces se continua con el programa         
    else: 

        #Se comprueba que el segundo número no sea menor al primer número
        if num1 > num2:

            #En caso de ser verdadero entonces se muestra el mesanje correspondiente
            print('!ERROR!: EL SEGUNDO NÚMERO NO PUEDE SER MENOR AL PRIMER NÚMERO.')

        else:

            #Se comprueba que los números ingresados esten entre el rango anteriormente mostrado (1 - 10)
            if num1 <= 10 and num2 <= 10:

                #En caso de ser verdadero entonces se imprime un mesaje
                print('\nEl rango entre {} y {} es:'.format(num1, num2))

                #Se imprime el rango de números ingresados por el usuario
                for i in range(num1, num2+1):

                    print(i)

            #En caso de que los números ingresados no esten entre el rango del 1 al 10 entonces se imprime el siguiente mensaje
            else:

                print('!ERROR!: LOS DATOS INGRESADOS NO CORRESPONDEN AL RANGO PREVIAMENTE MOSTRADO.')

#En caso de que el string ingresado no sea un número entonces se mostrara en pantalla el mensaje correspondiente
except ValueError:

    print('!ERROR!: LOS DATOS INGRESADOS NO SON CORRECTOS.')
