'''Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

import datetime

i = 0

Current_year = datetime.datetime.now().year

user_age = input('Ingrese su edad actual: ')

year_user = input('Ingrese el año en que nacio (AAAA): ')

try:

    user_age = int(user_age)

    year_user = int(year_user)

    while i < user_age and year_user < Current_year:

        i += 1

        year_user += 1

        if i == 1:

            print('En {} tienes {} año'.format(year_user, i))

        else: 
            
            print('En {} tienes {} años'.format(year_user, i))
    
    if i == 0 and year_user == Current_year:

        i = 1

        print('En {} tienes {} año'.format(Current_year, i))
    
    else:

        print('¡ERROR!: EL AÑO INGRESADO NO CORRESPONDE AL AÑO ACTUAL O ANTERIORES.')

except ValueError:

    print('¡ERROR!: LOS DATOS INGRESADOS NO SON VALIDOS.')

