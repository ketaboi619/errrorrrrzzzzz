#programa gestion productos mercado 

nombreUsuario = None

#variables

productos = []
producto = {}

print("ZZZZZZappaa")
print("1. Agregar productos lista mercado ")
print("2. Mostrar productos lista mercado ")
print("3. Modificar productos lista mercado ")
print("4. Retirar productos lista mercado ")
print("Presiona 5 para salir")

opcion = 100
while opcion != 5:
    opcion = int(input("Digita una opcion")) 

    if opcion == 1:
        print("Creando lista")
        producto["id"] =  input("Digite el codigo del producto")
        producto["nombre"] = input("Digite el nombre del producto")
        producto["presentación"] = input("Digite presentación del producto")
        producto["cantidad"] = int(input("Digite cantidad del producto"))
        producto["precio"] = int(input("Digite precio del producto"))

        productos.append(producto)
        print(productos)

    elif opcion == 2:
        print("Mostrando lista")

    elif opcion == 3:
        print("Modificando lista")
    elif opcion == 4:
        print("Retirando lista")

    else:
        print("zzzzzzzzzzzerror")    

