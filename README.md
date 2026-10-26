# Gestor de inventario con listas

Programa de consola en Python para administrar los productos y las cantidades disponibles de una tienda pequeña. Fue desarrollado como proyecto del Taller 5 (Listas) de Lógica de Programación.

## Objetivo

Practicar el manejo de listas, índices, ciclos, condicionales y funciones propias usando **dos listas paralelas**:

- `productos`: nombres de los productos.
- `cantidades`: unidades disponibles. El elemento `cantidades[i]` corresponde a `productos[i]`.

## Requisitos

- Python 3.8 o superior.
- No usa librerías externas, archivos, bases de datos, clases ni diccionarios.

## Cómo ejecutarlo

```bash
python main.py
```

## Instrucciones de uso

Al iniciar aparece un menú. Escriba el número de la opción y presione Enter.

| Opción | Acción |
|--------|--------|
| 1 | Registrar un producto y su cantidad |
| 2 | Mostrar todo el inventario |
| 3 | Buscar un producto por nombre |
| 4 | Modificar la cantidad de un producto |
| 5 | Eliminar un producto |
| 6 | Ver cuántos productos diferentes hay |
| 7 | Ver el producto con mayor cantidad |
| 8 | Salir |

## Funciones implementadas

- `buscar_indice(nombre)`: devuelve la posición del producto o `-1` si no existe.
- `leer_cantidad(mensaje)`: pide un entero mayor o igual a 0 y repite si el dato es incorrecto.
- `registrar_producto()`: agrega el nombre y la cantidad a las dos listas.
- `mostrar_inventario()`: recorre las listas con un ciclo `for`.
- `buscar_producto()`, `modificar_cantidad()`, `eliminar_producto()`: verifican que el producto exista antes de actuar.
- `mostrar_resumen()`: muestra la cantidad de productos diferentes.
- `producto_mayor_cantidad()`: muestra el producto (o productos, si hay empate) con más unidades.
- `mostrar_menu()` y `main()`: controlan el menú y las opciones inválidas.

## Decisiones de diseño

- **Sin productos repetidos:** antes de registrar se busca el nombre (sin distinguir mayúsculas). Así cada producto tiene un único índice y las listas no se desordenan.
- **Listas sincronizadas:** al eliminar se usa `pop()` con el mismo índice en ambas listas.

## Autor

Joan Nicolas Rey Gomez
