import math
'''Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general 
es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que 
al final muestre el mensaje: “La solución es: <solucion>”'''

#? imagen de la ecuación (https://img-c.udemycdn.com/redactor/raw/article_lecture/2020-11-06_00-09-32-7407317e03e1ae3fab900911b2b0bc5a.jpg)


a = float(input('Ingresa el valor de a: '))

b = float(input('Ingresa el valor de b: '))

c = float(input('Ingresa el valor de c: '))

#*Operación matematica

x1 = (- b + (math.sqrt(((b**2) - 4 * (+a * c))))) / (2 * a)

x2 = (- b - (math.sqrt(((b**2) - 4 * (+a * c))))) / (2 * a)


#*Resultado

print('El resultado positivo de la ecuación es:',x1)
print('El resultado negativo de la ecuación es:',x2)

