def print_menu():
    print '1. imprimir los numeros'
    print '2. ingresar numero nuevo'
    print '3. remover numero'
    print '4. buscar un numero'
    print '5. salir'
    print
numbers = {}
listablanca = {}
listanegra = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = input("Escribe un numero (1-5):")
    if menu_choice == 1:
        print "Numeros de telefono:"
        for x in numbers.keys():
            print "Nombre: ",x," \tNumero: ",numbers[x]
        print
    elif menu_choice == 2:
        print "ingresa el nombre, el numero y si va para la lista blanca o lista negra"
        nombre = raw_input("Nombre:")
        numero = raw_input("Numero:")
        numbers[nombre] = numero
        lista = raw_input("lista blanca 1, lista negra 2:")
        if lista == 1:
            listablanca[nombre] = numero
        elif lista == 2:
            listanegra[nombre] = numero
    elif menu_choice == 3:
        print "eliminar el contacto"
        name = raw_input("Nombre:")
        if numbers.has_key(nombre):
            del numbers[nombre]
            del listablanca[nombre]
            del listanegra[nombre]
        else:
            print "Este ",nombre,"no se encuentra en la agenda "
    elif menu_choice == 4:
        print "buscar el numero de la persona"
        name = raw_input("nombre:")
        if numbers.has_key(nombre):
            print "El numero es ",numbers[nombre]
        else:
            print "Este ",nombre,"no se encuentra en la agenda "
    elif menu_choice != 5:
        print_menu()
