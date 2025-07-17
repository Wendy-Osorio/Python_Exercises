'''Ejercicio 4

Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula'''

print('BIENVENIDO AL SISTEMA DE VOTACIÓN.\nCandidato A: Partido Rojo\nCandidato B: Partido Verde\nCandidato C: Partido Azul')


voto = input('\nElige a tu candidato: ')

if voto.lower() == 'a':

    print('Felicidades ha votado por el partido Rojo.')

else:

    if voto.lower() == 'b':

        print('Felicidades ha votado por el partido Verde.')

    else: 

        if voto.lower() == 'c':
            
            print('Felicidades ha votado por el partido Azul.')

        else:

            print('¡¡ERROR!!: HA INGRESADO UNA OPCIÓN NO VALIDA.')



