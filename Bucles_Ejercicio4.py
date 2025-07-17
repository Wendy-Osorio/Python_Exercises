'''Ejercicio 4

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, 
pero, solo imprimiendo los números que sean impares'''

num1 = input('\nIngrese el primer número para conocer su rango impar: ')

num2 = input('\nIngrese el segundp número para conocer su rango impar: ')

try: 

    num1 = int(num1)

    num2 = int(num2)

    if num1 < 0 or num2 < 0:

        if num1 > num2:

            print('!ERROR!: EL SEGUNDO NÚMERO NO PUEDE SER MAYOR AL PRIMER NÚMERO.')
        
        else:
            
            for i in range(num1, num2+1):

                if i % 2 == 0:

                    continue

                print(i)
                
    else: 

        if num1 > num2:

            print('!ERROR!: EL SEGUNDO NÚMERO NO PUEDE SER MENOR AL PRIMER NÚMERO.')

        else:

            print('El rango impar entre {} y {} es:'.format(num1, num2))

            for i in range(num1, num2+1):

                if i % 2 == 0:

                    continue

                print(i)

except ValueError:

    print('!ERROR!: LOS DATOS INGRESADOS NO SON CORRECTOS.')