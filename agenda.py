def print_menu():
    print ('1. imprimir la agenda completa')
    print ('2. imrpimir lista buena')
    print ('3. imprimir lista mala')
    print ('4. ingresar numero nuevo')
    print ('5. remover numero')
    print ('6. buscar un numero')
    print ('7. salir')
directorio = {}
listabuena = {}
nombres = {}
listamala = {}
menu_choice = 0
print_menu()
while menu_choice != 7:
    menu_choice = int(input("Escribe un numero (1-7):"))
    
    
    if menu_choice == 1:
        print ("La agenda es:")
        for x in directorio.keys():
            print ("Nombre: ",x," \tNumero: ",directorio[x],"\tTipo:",nombres[x])
            
            
    elif menu_choice == 2:
        print ("Lista buena:")
        for x in listabuena.keys():
            print ("Nombre: ",x," \tNumero: ",listabuena[x])
            
            
    elif menu_choice == 3:
        print( "Lista mala:")
        for x in listamala.keys():
            print ("Nombre: ",x," \tNumero: ",listamala[x]  ) 
            
            
    elif menu_choice == 4:
        print ("ingresa el nombre, el numero y si va para la lista buena o lista mala")
        nombre = input("Nombre:")
        numero = input("Numero:")
        directorio[nombre] = numero
        lista = int(input("lista buena 1, lista mala 2:"))
        if lista == 1:
            listabuena[nombre] = numero
            tipo = ("esta en la lista buena")
            nombres[nombre]=tipo


        elif lista == 2:
            listamala[nombre] = numero
            tipo = ("esta en la lista mala")
            nombres[nombre]=tipo
            
            
    elif menu_choice == 5:
        print ("eliminar el contacto")
        nombre = input("Nombre:")
        if nombre in directorio:
            del(directorio[nombre])
        if nombre in listabuena:
            del(listabuena[nombre])
        if nombre in listamala:
            del(listamala[nombre])
        else:
            print( "Este ",nombre,"no se encuentra en la agenda ")
            
            
    elif menu_choice == 6:
        print ("buscar el numero de la persona")
        nombre = input("nombre:")
        if nombre in directorio:
            print ("El numero es ",directorio[nombre])
        else:
            print("Este ",nombre,"no se encuentra en la agenda ")
            
    elif menu_choice != 7:
        menu()
            
    
