'''Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, 
conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

from decimal import Decimal, ROUND_DOWN


p1 = float(input('Ingrese la calificación de la practica #1: '))

p2 = float(input('Ingrese la calificación de la practica #2: '))

p3 = float(input('Ingrese la calificación de la practica #3: '))

exParcial = float(input('Ingrese la calificación del examen parcial: '))

exFinal = float(input('Ingrese la calificación del examen final: '))


#*Operaciones matematicas

pp = (p1 + p2 + p3) / 3

prom = Decimal(pp + (2 * exParcial) + (3 * exFinal)) / 6

promFinal = prom.quantize(Decimal('.01'), rounding=ROUND_DOWN) #Simplifica un número decimal a dos digitos despues del punto

#*Resultado

print('El promedio es: ', promFinal)
