'''Ejercicio 1: 
Escribe un programa con la siguiente operación aritmetica (https://img-c.udemycdn.com/redactor/raw/article_lecture/2020-11-05_23-59-30-e5bb152c676fb083c4c02e79021ac6a4.jpg)'''

num1 = 3
num2 = 2
num3 = 5 

resultado = pow(((num1 + num2) / (num2 * num3)), 2)

print(resultado)

'''Ejercicio 2:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
Cada payaso pesa 112 g y cada muñeca 75 g. 
Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, se debe sumar.'''

CantPayasos = 23
CantMunecas = 54

PesoPaquete = ((CantPayasos * 112) + (CantMunecas * 75))

print( "El peso total es de:",PesoPaquete, "g")


