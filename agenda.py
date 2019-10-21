def print_menu():
    print ('1. imprimir la agenda')
    print ('2. ingresar numero nuevo')
    print ('3. remover numero')
    print ('4. buscar un numero')
    print ('5. salir')
def menu2():
    print ('1. imprimir la agenda completa')
    print ('2. imrpimir lista buena')
    print ('3. imprimir lista mala')
directorio = {}
listabuena = {}
nombres = {}
listamala = {}
menu_choice = 0
menu_impro = 0

print_menu()
while menu_choice != 5:
    menu_choice = int(input("Escribe un numero (1-5):"))
    
    
    if menu_choice == 1:
        menu2()
        menu_impro = int(input("Escribe un numero (1-3):"))
        
        if menu_impro == 1:
            print ("Agenda completa:")
            for x in directorio.keys():
                print ("Nombre: ",x," \tNumero: ",directorio[x],"\tTipo:",nombres[x])
            print_menu()
            
        elif menu_impro == 2:
            print ("Lista buena:")
            for x in listabuena.keys():
                print ("Nombre: ",x," \tNumero: ",listabuena[x])
            print_menu()
            
        elif menu_impro == 3:
            print( "Lista mala:")
            for x in listamala.keys():
               print ("Nombre: ",x," \tNumero: ",listamala[x]  ) 
            print_menu()


    elif menu_choice == 2:
        print ("ingresa el nombre, el numero y si va para la lista buena o lista mala")
        nombre = input("Nombre:")
        numero = input("Numero:")
        directorio[nombre] = numero
        lista = int(input("lista buena 1, lista mala 2:"))
        
        if lista == 1:
            listabuena[nombre] = numero
            tipo = ("esta en la lista buena")
            nombres[nombre]=tipo
            print_menu()



        elif lista == 2:
            listamala[nombre] = numero
            tipo = ("esta en la lista mala")
            nombres[nombre]=tipo
            print_menu()

            
            
    elif menu_choice == 3:
        print ("eliminar el contacto")
        nombre = input("Nombre:")
        if nombre in directorio:
            del(directorio[nombre])
            print_menu()

        if nombre in listabuena:
            del(listabuena[nombre])
            print_menu()

        if nombre in listamala:
            del(listamala[nombre])
            print_menu()

        else:
            print( "Este ",nombre,"no se encuentra en la agenda ")
            print_menu()

            
            
    elif menu_choice == 4:
        print ("buscar el numero de la persona")
        nombre = input("nombre:")
        if nombre in directorio:
            print ("El numero es ",directorio[nombre])
        else:
            print("Este ",nombre,"no se encuentra en la agenda ")
            print_menu()

            
    elif menu_choice != 5:
        print_menu()
            
    

