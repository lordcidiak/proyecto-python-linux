def print_menu():
    print '1. imprimir la agenda completa'
    print '2. imrpimir lista blanca'
    print '3. imprimir lista negra'
    print '4. ingresar numero nuevo'
    print '5. remover numero'
    print '6. buscar un numero'
    print '7. salir'
    print
numbers = {}
listablanca = {}
listanegra = {}
menu_choice = 0
print_menu()
while menu_choice != 7:
    menu_choice = input("Escribe un numero (1-7):")
    if menu_choice == 1:
        print "Numeros de telefono:"
        for x in numbers.keys():
            print "Nombre: ",x," \tNumero: ",numbers[x]
            if numbers[x] == listablanca[x]:
            print "Esta en la lista blanca"
            if numbers[x] == listanegra[x]:
            print "Esta en la lista negra"
    elif menu_choice == 2:
        print "Numeros de telefono:"
        for x in listablanca.keys():
            print "Nombre: ",x," \tNumero: ",listablanca[x]
    elif menu_choice == 3:
        print "Numeros de telefono:"
        for x in listanegra.keys():
            print "Nombre: ",x," \tNumero: ",listanegra[x]   
    elif menu_choice == 4:
        print "ingresa el nombre, el numero y si va para la lista blanca o lista negra"
        nombre = raw_input("Nombre:")
        numero = raw_input("Numero:")
        numbers[nombre] = numero
        lista = raw_input("lista blanca 1, lista negra 2:")
        if lista == 1:
            listablanca[nombre] = numero
        elif lista == 2:
            listanegra[nombre] = numero
    elif menu_choice == 5:
        print "eliminar el contacto"
        name = raw_input("Nombre:")
        if numbers.has_key(nombre):
            del numbers[nombre]
            del listablanca[nombre]
            del listanegra[nombre]
        else:
            print "Este ",nombre,"no se encuentra en la agenda "
    elif menu_choice == 6:
        print "buscar el numero de la persona"
        name = raw_input("nombre:")
        if numbers.has_key(nombre):
            print "El numero es ",numbers[nombre]
        else:
            print "Este ",nombre,"no se encuentra en la agenda "
    elif menu_choice != 7:
        print_menu()
