'''Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''

lista = []

pares = []

impares = []

#Menu principal
def menuPrincipal():

    print('Menú Principal:\n1. Ver lista\n2. Agregar un nuevo número a la lista\n3. Ordenar lista\n4. Salir')

    resp = input('¿Qué operación desea realizar?: ')

    try:

        resp = int(resp)

        if resp == 1:

            ver_listas()
        
        if resp == 2:

            add()

        if resp == 3:

            ordenar_listas()

        if resp == 4:
            
            print("Saliendo del programa...")
            exit()

        else:

            print('ERROR INGRESASTE UNA OPCION NO VALIDA...INTENTALO DE NUEVO.\n')

            menuPrincipal()
    
    except ValueError:

        print('ERROR INGRESASTE UNA OPCION NO VALIDA...INTENTALO DE NUEVO.\n')

        menuPrincipal()

#Ve lista
def ver_listas():

    print('Lista: {}\n'.format(lista))

    menuPrincipal()

#Agregar nuevos valores a la lista
def add():

    num = input('Ingrese un número: ')

    try:
        
        #Verificar si el valor ingresado por el usuario es un número entero
        num = int(num)

        #Una vez verificado se agrega ese valor a la lista
        lista.append(num)

        #Se muestra la lista con los valores agregados
        print('Se ha agregado exitosamente un nuevo número a la lista...\nLista: {}'.format(lista))

        #Se manda a llamar la función resp_add para preguntarle al usuario si quiere agregar otro valor a la lista o no
        resp_add()

    except ValueError:

        try:

            #Se comprueba que el valor ingresado por el usuario sea un número de tipo flotante
            num = float(num)

            #Una vez verificado se agrega ese valor a la lista
            lista.append(num)

            #Se muestra la lista con los valores agregados
            print('Se ha agregado exitosamente un nuevo número a la lista...\nLista: {}'.format(lista))
            
            #Se manda a llamar la función resp_add para preguntarle al usuario si quiere agregar otro valor a la lista o no
            resp_add()

        except ValueError:

            #Si el usuario ingresa una opción no valida entonces vuelve a empezar el proceso de la función add()
            print('ERROR INGRESASTE UNA OPCION NO VALIDA...INTENTALO DE NUEVO.\n')

            add()

#Ordenar la lista
def ordenar_listas():

    #OPCIONES A ORDENAR:
    print('Menú:\n1.Ordenar en pares\n2.Ordenar impares\n3.Regresar al menú principal')

    #Se le pregunta al usuario que operación del menú desea realizar
    resp = input('¿Qué operación desea realizar?: ')

    try:

        #Se comprueba que la opción ingresada sea un número
        resp = int(resp)

        #Condiciones según la respuesta del usuario

        #Si la respuesta del usuario es 1 entonces se muestra y ordenan los números de la lista en pares
        if resp == 1:

            for num in lista:

                if num % 2 == 0:

                    pares.append(num) #Se agrega a la lista de pares todos los números que correspondan

                    pares.sort() #Ordena la lista de forma ascendente
                    
            print('Pares: {}\n'.format(pares))
            
            ordenar_listas()

        #Si la respuesta del usuario es 2 entonces se muestra y ordena la lista en impares
        if resp == 2:

            for num in lista:

                if num % 2 == 1:

                    impares.append(num) #Se agrega a la lista de impares todos los números que correspondan

                    impares.sort() #Ordena la lista de forma ascendente
                    
            print('Impares: {}\n'.format(impares))

            ordenar_listas()

        #Si la respuesta del usuario es 3 entonces se regresa al menú principal
        if resp == 3:

            print("")
            menuPrincipal()
            
        else:

            #Si el usuario ingresa una opción no valida entonces vuelve a empezar el proceso de la función ordenar_lista()
            print('ERROR INGRESASTE UNA OPCION NO VALIDA...INTENTALO DE NUEVO.\n')

            ordenar_listas()

    except ValueError:

        #Si el usuario ingresa una opción no valida entonces vuelve a empezar el proceso de la función ordenar_lista()
        print('ERROR INGRESASTE UNA OPCION NO VALIDA...INTENTALO DE NUEVO.\n')

        ordenar_listas()

def resp_add():

    #Se le pregunta al usuario si desea agregar otro valor a la lista
    resp = input('\n¿Deseas agregar otro número a la lista? S/N: ')

    #Condiciones según la respuesta del usuario
    if resp.lower() == 's':
            
        #Si la respues es S (si) entonces el proceso vuelve a empezar con la función add()
        add()
        
    if resp.lower() == 'n':

        #Si la respuesta es N (no) entonces el proceso se detiene y redirige al menú principal
        print("")
        menuPrincipal()

    else:
            
        #Si el usuario ingresa una opción no valida entonces vuelve a empezar el proceso de la función resp_add()
        print('ERROR INGRESASTE UNA OPCION NO VALIDA....\n')

        resp_add()

#Inicio del programa
menuPrincipal()