from os import system

acum = 1
id =[]
producto = []
precio = []
cuenta = []

def insertar_producto():
    id.append(acum)
    producto.append(input("Ingrese nombre del producto: | "))
    precio.append(float(input("Ingrese precio del producto: | ")))

def imprimir_listado(indice, articulo, valor):
    for i in range(len(indice)):
        print(indice[i], ".| ", articulo[i], " | ", valor[i])

def sumar_precio(total):
    suma = 0
    for i in range(2, len(cuenta), 3):
                suma += cuenta[i]
    return suma

while (True):

    print("-------------------------")
    print("|   CAJA REGISTRADORA   |")
    print("-------------------------")
    print(" ")
    print("----------MENÚ-----------")
    print("|1. Agregar producto    |")
    print("|2. Remover producto    |")
    print("|3. Añadir a la cuenta  |")
    print("|4. Retirar de la cuenta|")
    print("|5. Cobrar              |")
    print("-------------------------")
    print(" ")

    op = int(input("Seleccione una opción del menú: | "))

    if(op==1):
        system("cls")
        print("----------Nuevo Producto----------")
        if(bool(producto)==False):  
            insertar_producto()
        else:
            acum += 1
            insertar_producto()

    elif(op==2):
        system("cls")    
        print("----------Listado de Productos----------")
        if(bool(producto)==True):
            imprimir_listado(id,producto,precio)
            
            print(" ")
            eliminar = int(input("Ingresa el ID del producto a eliminar: | "))
            acum -= 1
            id.pop(eliminar-1)
            producto.pop(eliminar-1)
            precio.pop(eliminar-1)

            for j in range(len(id)):
                id[j]= j+1        
            
            imprimir_listado(id,producto,precio)
            print(" ")
            print("El producto se ha eliminado con éxito")
        else:
            print("No se ha registrado ningún producto")

    elif(op==3):
        system("cls")
        if(bool(producto)==True):
            print("----------Listado de Productos----------")
            imprimir_listado(id,producto,precio)
            des = "s"
            
            while des=="s":          
                insertar = int(input("Ingresa el ID del producto para añadir a la cuenta: | "))
                cuenta.append(id[insertar-1])
                cuenta.append(producto[insertar-1])
                cuenta.append(precio[insertar-1])
                imprimir_listado(cuenta,cuenta,cuenta)
                des = input("Desea agregar otro producto a la cuenta s/n: | ")
            
            print("La cuenta es actual es de: ", sumar_precio(cuenta))

        else:
            print("No se ha registrado ningún producto")

    elif(op==4):
        system("cls")
        if(bool(cuenta)==True):
            print("----------Listado de Productos en la Cuenta----------")
            for i in range(0, len(cuenta), 3):
                    print(cuenta[i], ".| ", cuenta[i+1], " | ", cuenta[i+2])
            
            des = "s"
            
            while des=="s":
                eliminar = int(input("Ingresa el ID del producto para retirar de la cuenta: | "))
            
                cuenta.pop(eliminar-1)
                cuenta.pop(eliminar)
                cuenta.pop(eliminar+1)
                des = input("Desea eliminar otro producto de la cuenta s/n: | ")
            
            sumar_precio(cuenta)
            print("La cuenta es actual es de: ", sumar_precio(cuenta))
        else:
            print("No se ha registrado ningún producto")

    elif(op==5):
        system("cls")
        if(bool(cuenta)==True):
            print("La cuenta total es de: $", sumar_precio(cuenta))
            print("Gracias por su compra!")
            break
        else:
          print("No hay productos en la cuenta")
    else:
        system("cls")
        print("Opción inválida")

