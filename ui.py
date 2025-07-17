# ui.py
"""Módulo de Interfaz de Usuario (Presentation Layer).

Responsable de toda la interacción visual con el usuario en la consola.
Maneja la impresión de menús, listas, mensajes y la captura de datos,
utilizando la librería 'colorama' para mejorar la experiencia.
"""
from colorama import Fore, Style, Back

def mostrar_menu_principal():
    """Imprime el menú principal de la aplicación.
    Presenta las opciones disponibles para gestionar productos, categorías,
    generar reportes de stock o salir del programa.
    Args: no tiene
    Returns: no tiene
    """
    print(Fore.CYAN + "\n====== MENÚ PRINCIPAL ======")
    print("1.📦 Gestionar Productos")
    print("2.📋 Gestionar Categorías")
    print("3.📊 Generar Reporte de Stock")
    print("4.🔚 Salir del programa")
    print(Fore.CYAN + "==========================\n")

def mostrar_menu_productos():
    """Imprime el submenú de gestión de productos.
    Presenta las opciones para agregar, modificar, eliminar, buscar o listar productos.
    Args: no tiene
    Returns: no tiene
    """
    print(Fore.CYAN + "\n--- Menú de Productos ---")
    print("1. ✅ Agregar producto")
    print("2. ✏️ Modificar producto")
    print("3. 👁️  Visualizar todos los productos")
    print("4. 🔍 Buscar producto por ID")
    print("5. ❌ Eliminar producto")
    print("6. 🔙 Volver al menú principal")
    print(Fore.CYAN + "-------------------------\n")

def mostrar_menu_categorias():
    """Imprime el submenú de gestión de categorías.
    Presenta las opciones para agregar, modificar, eliminar o listar categorías.
    Args: no tiene
    Returns: no tiene
    """
    from colorama import Fore, Style
    print(Fore.CYAN + "\n--- Menú de Categorías ---")
    print("1. ✅  Agregar categoría")
    print("2. 👁️  Visualizar categorías")
    print("3. ✏️  Modificar categoría")
    print("4. ❌  Eliminar categoría")
    print("5. 🔙 Volver al menú principal")
    print(Fore.CYAN + "--------------------------\n")

def mostrar_menu_modificar_producto():
    """Muestra las opciones para modificar un producto.
        Permite al usuario elegir qué aspecto del producto desea cambiar:
        nombre, descripción, cantidad, precio o categoría.      
        Args: no tiene
        Returns: no tiene  """
    
    print(Fore.CYAN + "\n--- ¿Qué desea modificar? ---")
    print("1. Nombre")
    print("2. Descripción")
    print("3. Cantidad en stock")
    print("4. Precio")
    print("5. Categoría")
    print("6. Finalizar modificación")
    print(Fore.CYAN + "----------------------------\n")

def obtener_input(mensaje_prompt):
    """Obtiene una entrada del usuario con un estilo consistente.
    Args : mensaje_prompt (str): El mensaje que se mostrará al usuario.
    Returns: str: La entrada del usuario, sin espacios al inicio o final.
     
 
    """
    return input(f"{Fore.CYAN}{mensaje_prompt}{Style.RESET_ALL}").strip()

def mostrar_lista_categorias(categorias):
    """Muestra una lista formateada de categorías.
    Args: categorias (list): Lista de tuplas con ID y nombre de categorías.
    Returns:un booleano: True si se mostraron categorías, False si la lista estaba vacía.

    """
    if not categorias:
        mostrar_mensaje_info("No hay categorías registradas.")
        return False
    print(Fore.MAGENTA + "\n--- Categorías Registradas ---")
    for id_cat, nombre in categorias:
        print(f"ID: {id_cat} | Nombre: {nombre}")
    print(Fore.MAGENTA + "----------------------------\n")
    return True

def mostrar_lista_seleccion_con_opcion_nueva(items, texto_opcion_nueva):
    """Muestra una lista de ítems numerada y añade una opción final.

    Args: items (list): Lista de tuplas con ID y nombre de ítems.
    texto_opcion_nueva (str): Texto para la opción de crear un nuevo ítem.
    Returns: no tiene
    """
    for i, item in enumerate(items):
        print(f"{Fore.YELLOW}{i + 1}.{Style.RESET_ALL} {item[1]}")
    print(f"{Fore.YELLOW}{len(items) + 1}.{Style.RESET_ALL} {texto_opcion_nueva}")

def mostrar_lista_productos(productos):
    """Muestra una lista formateada de productos con todos sus detalles.
    Args: productos (list): Lista de tuplas con detalles del producto.
    Formato de cada tupla: (id, nombre, descripcion, cantidad, precio, nombre_categoria).
    Returns: un booleano: True si se mostraron productos, False si la lista estaba vacía.   
    """
    if not productos:
        mostrar_mensaje_info(" No hay productos registrados.")
        return False
    print(Fore.MAGENTA + "\n--- Productos Registrados ---")
    for id_prod, nombre, desc, cant, precio, cat in productos:
        print(f"{Fore.YELLOW}ID: {Style.RESET_ALL}{id_prod} | "
              f"{Fore.YELLOW}Nombre: {Style.RESET_ALL}{nombre} | "
              f"{Fore.YELLOW}Descripción: {Style.RESET_ALL}{desc} | "
              f"{Fore.YELLOW}Cantidad: {Style.RESET_ALL}{cant} | "
              f"{Fore.YELLOW}Precio: {Style.RESET_ALL}${precio} | "
              f"{Fore.YELLOW}Categoría: {Style.RESET_ALL}{cat}")
    print(Fore.MAGENTA + "---------------------------\n")
    return True

def mostrar_reporte_stock(productos, limite):
    """Muestra un reporte formateado de productos con stock bajo.

    Args: productos (list): Lista de tuplas con detalles del producto.
    Formato de cada tupla: (id, nombre, descripcion, cantidad, precio, nombre_categoria).
    limite (int): El límite de cantidad para considerar un producto como "bajo stock".
    Returns: no tiene
    """
    if not productos:
        mostrar_mensaje_info(f"No hay productos con una cantidad igual o inferior a {limite}.")
        return
    print(Fore.RED + f"\n--- REPORTE: PRODUCTOS CON STOCK BAJO (<= {limite}) ---")
    for id_prod, nombre, desc, cant, precio, cat in productos:
         print(f"{Fore.YELLOW}Nombre: {Style.RESET_ALL}{nombre} | "
              f"{Back.RED}{Style.BRIGHT}Cantidad: {cant}{Style.RESET_ALL} | "
              f"{Fore.YELLOW}ID: {Style.RESET_ALL}{id_prod} | "
              f"{Fore.YELLOW}Categoría: {Style.RESET_ALL}{cat}")
    print(Fore.RED + "--------------------------------------------------\n")

def mostrar_mensaje_exito(mensaje):
    """Muestra un mensaje de éxito con formato.
    Args: mensaje (str): El texto del mensaje de éxito a mostrar.
    Returns: no tiene
    """
    print(Fore.GREEN + f"✅ {mensaje}")

def mostrar_mensaje_error(mensaje):
    """Muestra un mensaje de error resaltado.
    Args: mensaje (str): El texto del mensaje de error a mostrar.
    Returns: no tiene
    """
    print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}❌ {mensaje}{Style.RESET_ALL}")

def mostrar_mensaje_info(mensaje):
    """Muestra un mensaje informativo con formato.
    Args: mensaje (str): El texto del mensaje informativo a mostrar.
    Returns: no tiene
    """
    print(Fore.YELLOW + f"ℹ️ {mensaje}") 