'''Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal'''

vocal = input('Ingresa una vocal: ')


if vocal.lower() == 'a':
    
    print('Ingresaste la vocal A.')

else:

    if vocal.lower() == 'e':

        print('Ingresaste la vocal E.')
    
    else:

        if vocal.lower() == 'i':

            print('Ingresaste la vocal I.')
        
        else: 

            if vocal.lower() == 'o':

                print('Ingresaste la vocal O.')

            else:

                if vocal.lower() == 'u':

                    print('Ingresaste la vocal U.')
                
                else:

                    print('¡¡ERROR!!: LOS CARACTERES INGRESADOS NO SON UNA VOCAL')

