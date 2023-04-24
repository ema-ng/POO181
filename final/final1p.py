a=1024
b=1.0


def menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("que operacion desa realizar:"))
            correcto=True
        except ValueError:
            print('escoje una opcion del menu')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1.convertir megabites a gigabites")
    print ("2.convertir gigabites a gigabites")
    print ("3.convertir gigabites a terabites")
    print ("4.convertir terabites  a gigabites")
    print ("5.salir")
     
    print ("Elige una opcion")
 
    opcion = menu()
 
    if opcion == 1:
        e=int(input("ingresa la cantidad a convertir: "))
        d=(e*b)/a
        print("el valor es: ",d,"GB")
    elif opcion == 2:
        e=int(input("ingresa la cantidad a convertir: "))
        d=(e/b)*a
        print("el valor es: ",d,"MB")
    elif opcion == 3:
         e=int(input("ingresa la cantidad a convertir: "))
         d=(e/a)*b
         print("el valor es: ",d,"TB")
    elif opcion == 4:
        e=int(input("ingresa la cantidad a convertir: "))
        d=(e*a)/b
        print("el valor es: ",d,"GB")
        
    elif opcion == 5:
        salir = True
    else:
        print ("elige una opcion del menu")
 
print ("Fin")

    
