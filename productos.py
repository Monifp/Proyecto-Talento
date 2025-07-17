 # productos.py
"""Módulo de lógica de negocio para la gestión de productos.
Responsable de agregar, modificar, eliminar y listar productos,
con validaciones y manejo de errores.
"""
import database as db
import ui
import sqlite3
import database as db
import ui

def agregar_nuevo_producto():
    """Orquesta la adición de un nuevo producto.
    Muestra un menú de categorías y permite al usuario seleccionar una o crear una nueva.
    Valida que el nombre, descripción, cantidad y precio sean correctos.
    Si la categoría no existe, permite crearla. 
    Args: no tiene
    Returns: no tiene
    """
    categorias = db.obtener_categorias_db()
    categoria_id = None

    print("\nPor favor, elija una categoría o cree una nueva:")
     
    ui.mostrar_lista_seleccion_con_opcion_nueva(categorias, "Crear una nueva categoría")
    
    opcion_crear_nueva = len(categorias) + 1

    while True: # Bucle para seleccionar o crear categoría
        try:
            opcion_elegida = int(ui.obtener_input("Seleccione una opción: "))
            
            if 1 <= opcion_elegida <= len(categorias):
                # El usuario eligió una categoría existente
                categoria_id = categorias[opcion_elegida - 1][0]
                break
            elif opcion_elegida == opcion_crear_nueva:
                # El usuario eligió crear una nueva categoría
                while True:
                    nombre_cat = ui.obtener_input("Ingrese el nombre de la nueva categoría: ")
                    if nombre_cat:
                        try:
                            # Se llama a la función de DB que retorna el ID
                            categoria_id = db.agregar_categoria_db(nombre_cat)
                            ui.mostrar_mensaje_exito(f"Categoría '{nombre_cat}' creada.")
                            break
                        except sqlite3.IntegrityError:
                            ui.mostrar_mensaje_error(f"La categoría '{nombre_cat}' ya existe. Intente con otro nombre.")
                    else:
                        ui.mostrar_mensaje_error("El nombre no puede estar vacío.")
                if categoria_id:
                    break # Salir del bucle principal de selección
            else:
                ui.mostrar_mensaje_error("Opción fuera de rango.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un número.")

     

    while True: # Bucle para ingresar los datos del producto
        
        nombre = ui.obtener_input("Ingrese el nombre del producto: ")
        if nombre:
            break
        ui.mostrar_mensaje_error("El nombre no puede estar vacío.")

     
    while True: # Bucle para ingresar la descripción del producto
        descripcion = ui.obtener_input("Ingrese la descripción del producto: ")
        if descripcion:
            break
        ui.mostrar_mensaje_error("La descripción no puede estar vacía.")

    while True: # Bucle para ingresar la cantidad del producto
        try:
            cantidad = int(ui.obtener_input("Ingrese la cantidad inicial en stock: "))
            if cantidad > 0:
                break
            else:
                ui.mostrar_mensaje_error("La cantidad debe ser mayor a cero.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un número entero.")

    while True: # Bucle para ingresar el precio del producto
        try:
            precio = int(ui.obtener_input("Ingrese el precio del producto (entero): "))
            if precio >= 0:
                break
            else:
                ui.mostrar_mensaje_error("El precio no puede ser negativo.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un número entero.")

    db.agregar_producto_db(nombre, descripcion, cantidad, precio, categoria_id)
    ui.mostrar_mensaje_exito(f"Producto '{nombre}' agregado.")


 
def modificar_un_producto():
    """Orquesta la modificación de un producto con validaciones.
    Muestra una lista de productos y permite al usuario seleccionar uno por ID.
    Valida que el ID sea correcto y permite modificar nombre, descripción,
    cantidad, precio o categoría. Si la categoría no existe, permite crearla.   
    Args: no tiene
    Returns: no tiene
    """
    productos = db.obtener_productos_db()
    if not ui.mostrar_lista_productos(productos):
        return

    while True: # Bucle para seleccionar el producto a modificar
        try:
            id_prod_str = ui.obtener_input("Ingrese el ID del producto a modificar: ")
            id_prod = int(id_prod_str)
            if id_prod in [p[0] for p in productos]:
                break
            else:
                ui.mostrar_mensaje_error("ID de producto no válido.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un ID numérico.")

    while True: # Bucle para seleccionar el campo a modificar
        ui.mostrar_menu_modificar_producto()
        opcion = ui.obtener_input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                nuevo_nombre = ui.obtener_input("Ingrese el nuevo nombre: ")
                if nuevo_nombre:
                    db.modificar_producto_db(id_prod, 'nombre', nuevo_nombre)
                    ui.mostrar_mensaje_exito("Nombre actualizado.")
                    break
                ui.mostrar_mensaje_error("El nombre no puede estar vacío.")
        elif opcion == '2':
            while True:
                nueva_desc = ui.obtener_input("Ingrese la nueva descripción: ")
                if nueva_desc:
                    db.modificar_producto_db(id_prod, 'descripcion', nueva_desc)
                    ui.mostrar_mensaje_exito("Descripción actualizada.")
                    break
                ui.mostrar_mensaje_error("La descripción no puede estar vacía.")
        elif opcion == '3':
            while True:
                try:
                    nueva_cant = int(ui.obtener_input("Ingrese la nueva cantidad: "))
                    if nueva_cant >= 0:
                        db.modificar_producto_db(id_prod, 'cantidad', nueva_cant)
                        ui.mostrar_mensaje_exito("Cantidad actualizada.")
                        break
                    ui.mostrar_mensaje_error("La cantidad no puede ser negativa.")
                except ValueError:
                    ui.mostrar_mensaje_error("Debe ingresar un número entero.")
        elif opcion == '4':
            while True:
                try:
                    nuevo_precio = int(ui.obtener_input("Ingrese el nuevo precio: "))
                    if nuevo_precio >= 0:
                        db.modificar_producto_db(id_prod, 'precio', nuevo_precio)
                        ui.mostrar_mensaje_exito("Precio actualizado.")
                        break
                    ui.mostrar_mensaje_error("El precio no puede ser negativo.")
                except ValueError:
                    ui.mostrar_mensaje_error("Debe ingresar un número entero.")
        elif opcion == '5':
            categorias = db.obtener_categorias_db()
            print("\nElija la nueva categoría:")
            ui.mostrar_lista_seleccion_con_opcion_nueva(categorias, "Crear nueva categoría")  
            opcion_crear = len(categorias) + 1
            while True:
                try:
                    num_cat = int(ui.obtener_input("Seleccione el número: "))
                    if 1 <= num_cat <= len(categorias):
                        nueva_cat_id = categorias[num_cat - 1][0]
                        db.modificar_producto_db(id_prod, 'categoria_id', nueva_cat_id)
                        ui.mostrar_mensaje_exito("Categoría actualizada.")
                        break
                    # Lógica para crear categoría al modificar  
                    elif num_cat == opcion_crear:
                         while True:
                            nombre_cat = ui.obtener_input("Ingrese el nombre de la nueva categoría: ")
                            if nombre_cat:
                                nueva_cat_id = db.agregar_categoria_db(nombre_cat)
                                db.modificar_producto_db(id_prod, 'categoria_id', nueva_cat_id)
                                ui.mostrar_mensaje_exito("Categoría creada y producto actualizado.")
                                break
                            else:
                                ui.mostrar_mensaje_error("El nombre no puede estar vacío.")
                         break
                    else:
                        ui.mostrar_mensaje_error("Número fuera de rango.")
                except ValueError:
                    ui.mostrar_mensaje_error("Debe ingresar un número.")
            # Rompemos el bucle de modificación de categoría
            if 'nueva_cat_id' in locals():
                break

        elif opcion == '6':
            ui.mostrar_mensaje_info("Modificación finalizada.")
            break
        else:
            ui.mostrar_mensaje_error("Opción inválida.")


def eliminar_un_producto():
    """Orquesta la eliminación de un producto por ID.
    Muestra una lista de productos y permite al usuario seleccionar uno por ID.
    Valida que el ID sea correcto y elimina el producto.
    Si la eliminación es exitosa, muestra un mensaje de éxito.  
    Args: no tiene
    Returns: no tiene"""
    productos = db.obtener_productos_db()
    if not ui.mostrar_lista_productos(productos):
        return
    while True:
        id_prod_str = ui.obtener_input("Ingrese el ID del producto a eliminar (o 'S' para salir): ")
        if id_prod_str.upper() == 'S':
            ui.mostrar_mensaje_info("Operación cancelada.")
            return
        try:
            id_prod = int(id_prod_str)
            if id_prod in [p[0] for p in productos]:
                db.eliminar_producto_db(id_prod)
                ui.mostrar_mensaje_exito("Producto eliminado.")
                return
            else:
                ui.mostrar_mensaje_error("ID de producto no válido.")
        except ValueError:
            ui.mostrar_mensaje_error("Entrada no válida.")

def buscar_un_producto():
    """Orquesta la búsqueda de un producto por su ID.
    Permite al usuario ingresar un ID y muestra los detalles del producto si existe.
    Si el ID no es válido o el producto no se encuentra, muestra un mensaje de error.
    Args: no tiene
    Returns: no tiene
    """
    try:
        id_buscado = int(ui.obtener_input("Ingrese el ID del producto a buscar: "))
    except ValueError:
        ui.mostrar_mensaje_error("Debe ingresar un ID numérico.")
        return

    producto_encontrado = db.obtener_producto_por_id_db(id_buscado)

    if producto_encontrado:
        ui.mostrar_mensaje_exito("Producto encontrado:")
        ui.mostrar_lista_productos([producto_encontrado])
    else:
        ui.mostrar_mensaje_error(f"No se encontró ningún producto con el ID {id_buscado}.")

def gestionar_productos():
    """Muestra el menú de gestión de productos y maneja las opciones.
    Permite al usuario agregar, modificar, eliminar, buscar o listar productos.
    Args: no tiene
    Returns: no tiene
    """
    while True:
        ui.mostrar_menu_productos()
        opcion = ui.obtener_input("Seleccione una opción: ")
        if opcion == '1':
            agregar_nuevo_producto()
        elif opcion == '2':
            modificar_un_producto()
        elif opcion == '3':
            ui.mostrar_lista_productos(db.obtener_productos_db())
        elif opcion == '4':
            buscar_un_producto()
        elif opcion == '5':
            eliminar_un_producto()
        elif opcion == '6':
            break
        else:
            ui.mostrar_mensaje_error(" Opción inválida.")