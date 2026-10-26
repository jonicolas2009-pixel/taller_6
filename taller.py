productos = []
cantidades = []
 
 
def buscar_indice(nombre):
    """Devuelve el índice del producto o -1 si no existe (ignora mayúsculas)."""
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1
 
 
def leer_cantidad(mensaje):
    """Pide un entero >= 0 y repite hasta que el usuario lo escriba bien."""
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Debe ingresar un numero entero mayor o igual a 0.")
        texto = input(mensaje).strip()
    return int(texto)
 
 
def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return
    # Decision: no se permiten productos repetidos (se compara sin mayusculas)
    if buscar_indice(nombre) != -1:
        print("Ese producto ya esta registrado. Use la opcion 4 para cambiar su cantidad.")
        return
    cantidad = leer_cantidad("Cantidad disponible: ")
    productos.append(nombre)
    cantidades.append(cantidad)
    print("Producto registrado correctamente.")
 
 
def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        print("\n--- INVENTARIO ---")
        for i in range(len(productos)):
            print(i + 1, productos[i], "-", cantidades[i])
 
 
def buscar_producto():
    nombre = input("Nombre del producto a buscar: ").strip()
    posicion = buscar_indice(nombre)
    if posicion == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Encontrado:", productos[posicion], "-", cantidades[posicion], "unidades")
 
 
def modificar_cantidad():
    nombre = input("Producto a modificar: ").strip()
    posicion = buscar_indice(nombre)
    if posicion == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Cantidad actual:", cantidades[posicion])
        cantidades[posicion] = leer_cantidad("Nueva cantidad: ")
        print("Cantidad actualizada.")
 
 
def eliminar_producto():
    nombre = input("Producto a eliminar: ").strip()
    posicion = buscar_indice(nombre)
    if posicion == -1:
        print("El producto no existe en el inventario.")
    else:
        # Se elimina en AMBAS listas con el mismo indice para mantenerlas sincronizadas
        productos.pop(posicion)
        cantidades.pop(posicion)
        print("Producto eliminado.")
 
 
def mostrar_resumen():
    print("Productos diferentes registrados:", len(productos))
 
 
def producto_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        mayor = max(cantidades)
        print("Mayor cantidad disponible:", mayor)
        for i in range(len(productos)):
            if cantidades[i] == mayor:
                print("-", productos[i])
 
 
def mostrar_menu():
    print("\n===== GESTOR DE INVENTARIO =====")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad")
    print("5. Eliminar producto")
    print("6. Cantidad de productos diferentes")
    print("7. Producto con mayor cantidad")
    print("8. Salir")
 
 
def main():
    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            producto_mayor_cantidad()
        elif opcion == "8":
            print("Hasta luego.")
        else:
            print("Opcion no valida. Escriba un numero del 1 al 8.")
 
 
main()
