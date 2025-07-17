'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", "Python", 3.14]

print('Bienvenido, tú lista es:', lista)

dato1 = input('\nIngresa el primer dato a cambiar en la lista: ')

lista[0] = dato1

dato2 = input('Ingrese el segundo dato a cambiar en la lista: ')

lista[1] = dato2

print('\nTu lista ahora es:',lista)

