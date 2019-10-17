def print_menu():
    print ('1. imprimir la agenda completa')
    print ('2. imrpimir lista blanca')
    print ('3. imprimir lista negra')
    print ('4. ingresar numero nuevo')
    print ('5. remover numero')
    print ('6. buscar un numero')
    print ('7. salir')
numbers = {}
listablanca = {}
tipo = {}
listanegra = {}
menu_choice = 0
print_menu()
while menu_choice != 7:
    menu_choice = int(input("Escribe un numero (1-7):"))
    
    
    if menu_choice == 1:
        print ("La agenda es:")
        for x in numbers.keys():
            print ("Nombre: ",x," \tNumero: ",x,"\tTipo:",numbers[x])
            
            
    elif menu_choice == 2:
        print ("Numeros de telefono:")
        for x in listablanca.keys():
            print ("Nombre: ",x," \tNumero: ",listablanca[x])
            
            
    elif menu_choice == 3:
        print( "Numeros de telefono:")
        for x in listanegra.keys():
            print ("Nombre: ",x," \tNumero: ",listanegra[x]  ) 
            
            
    elif menu_choice == 4:
        print ("ingresa el nombre, el numero y si va para la lista blanca o lista negra")
        nombre = input("Nombre:")
        numero = input("Numero:")
        numbers[nombre] = numero
        lista = int(input("lista blanca 1, lista negra 2:"))
        if lista == 1:
            listablanca[nombre] = numero
            tipo = ("lista blanca")
            numbers[nombre] = tipo


        elif lista == 2:
            listanegra[nombre] = numero
            tipo = ("lista negra")
            numbers[nombre] = tipo


            
            
    elif menu_choice == 5:
        print ("eliminar el contacto")
        nombre = input("Nombre:")
        if nombre in numbers:
            del(numbers[nombre])
        if nombre in listablanca:
            del(listablanca[nombre])
        if nombre in listanegra:
            del(listanegra[nombre])
        else:
            print( "Este ",nombre,"no se encuentra en la agenda ")
            
            
    elif menu_choice == 6:
        print ("buscar el numero de la persona")
        nombre = input("nombre:")
        if nombre in numbers:
            print ("El numero es ",numbers[nombre])
        else:
            print("Este ",nombre,"no se encuentra en la agenda ")
            
    elif menu_choice != 7:
        menu()
            
    
