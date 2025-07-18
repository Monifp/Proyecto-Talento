 # database.py
"""Módulo de Acceso a Datos (Data Access Layer).

Este módulo centraliza todas las interacciones con la base de datos SQLite,
'inventario.db'. Abstrae la lógica SQL del resto de la aplicación,
permitiendo un acceso más limpio y organizado a las operaciones CRUD
(Create, Read, Update, Delete) sobre las tablas 'categorias' y 'productos'.
Incluye funciones para inicializar la base de datos y manejar las conexiones,
asegurando que las claves foráneas estén habilitadas para mantener la integridad referencial. 
"""
import sqlite3

DB_NAME = "inventario.db"

def obtener_conexion():
    """Establece y retorna una conexión a la base de datos.

    Activa el soporte para claves foráneas (`PRAGMA foreign_keys = ON`)
    para garantizar la integridad referencial en cada conexión.
    Args: no tiene
    Returns: sqlite3.Connection: Un objeto de conexión a la base de datos.
     
    """
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_db():
    """Crea el esquema de la base de datos si las tablas no existen.
    Define y crea las tablas 'categorias' y 'productos'.
    args: no tiene
    Returns: no tiene  
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE RESTRICT
        )
    """)
    conn.commit()
    conn.close()

def contar_categorias_db():
    """Cuenta el número total de categorías en la base de datos.
    Args: no tiene
    return: El número total de categorías.
    
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM categorias")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def obtener_categorias_db():
    """Recupera todas las categorías de la base de datos, ordenadas por Id.
    args: no tiene
    return: Una lista de tuplas, donde cada tupla es (id, nombre).
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM categorias ORDER BY id")
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def agregar_categoria_db(nombre):
    """Agrega una nueva categoría a la base de datos.
    Valida que el nombre no esté vacío y no exista ya en la base de datos.
    Si la categoría se agrega correctamente, retorna el ID de la nueva categoría.
    
    Args: 
    nombre (str): El nombre de la nueva categoría.
    
    Levanta un error sqlite3.IntegrityError: Si el nombre ya existe en la base de datos.     
    
    return: El ID de la categoría recién creada.
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
    nuevo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return nuevo_id

def modificar_categoria_db(id_cat, nuevo_nombre):
    """Modifica el nombre de una categoría existente.
    
    Valida que el ID sea correcto y que el nuevo nombre no esté vacío.
    Si la modificación es exitosa, actualiza la base de datos.
    
    Args: 
    id_cat (int): El ID de la categoría a modificar.
    nuevo_nombre (str): El nuevo nombre para la categoría.
    
    return: no tiene
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE categorias SET nombre = ? WHERE id = ?", (nuevo_nombre, id_cat))
    conn.commit()
    conn.close()

def contar_productos_en_categoria_db(id_cat):
    """Cuenta el número de productos asociados a una categoría específica.
    
    Args: id_cat (int): El ID de la categoría a consultar.
    
    return: El número de productos en la categoría.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE categoria_id = ?", (id_cat,))
    total = cursor.fetchone()[0]
    conn.close()
    return total

def eliminar_categoria_db(id_cat):
    """Elimina una categoría por su ID.
    Valida que la categoría no tenga productos asociados antes de eliminarla.
    args: id_cat (int): El ID de la categoría a eliminar.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (id_cat,))
    conn.commit()
    conn.close()

def obtener_productos_db():
    """Recupera todos los productos con sus detalles y nombre de categoría.
    args: no tiene
    return: Lista de tuplas. Formato de cada tupla:
    (id, nombre, descripcion, cantidad, precio, nombre_categoria).
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        SELECT p.id, p.nombre, p.descripcion, p.cantidad, p.precio, c.nombre
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        ORDER BY p.nombre
    """
    cursor.execute(sql)
    productos = cursor.fetchall()
    conn.close()
    return productos

def agregar_producto_db(nombre, descripcion, cantidad, precio, cat_id):
    """Agrega un nuevo producto a la base de datos.
    Valida que el nombre no esté vacío y que la categoría exista.
    Si el producto se agrega correctamente, retorna el ID del nuevo producto.
    
    Args: 
    nombre (str): El nombre del producto.
    descripcion (str): La descripción del producto.    
    cantidad (int): La cantidad en stock.
    precio (int)
    cat_id (int): El ID de la categoría a la que pertenece.
    
    Levanta un error sqlite3.IntegrityError: Si el nombre del producto ya existe.
    
    return: no tiene      
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria_id) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, cat_id)
    )
    conn.commit()
    conn.close()

def obtener_producto_por_id_db(id_prod):
    """Recupera un único producto por su ID.
    Args: 
    id_prod (int): El ID del producto a buscar.
    
    return: Una tupla con los datos del producto, o None si no se encuentra.
    Formato: (id, nombre, desc, cant, precio, nombre_cat).
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        SELECT p.id, p.nombre, p.descripcion, p.cantidad, p.precio, c.nombre
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        WHERE p.id = ?
    """
    cursor.execute(sql, (id_prod,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def eliminar_producto_db(id_prod):
    """Elimina un producto por su ID.
    
    Args: 
    id_prod (int): El ID del producto a eliminar.
    
    Levanta un error sqlite3.IntegrityError: Si el producto no existe.
    
    return: no tiene
     
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conn.commit()
    conn.close()

def modificar_producto_db(id_prod, campo_a_modificar, nuevo_valor):
    """Modifica un campo específico de un producto. 
    Permite cambiar el nombre, descripción, cantidad, precio o categoría.
    Args: 
    id_prod (int): El ID del producto a modificar.
    campo_a_modificar (str): La columna a cambiar (ej: 'nombre', 'cantidad').
    nuevo_valor (any): El nuevo valor para el campo.

    Levanta un error ValueError: Si 'campo_a_modificar' no está en la lista permitida.

    return: no tiene
    """
    campos_permitidos = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria_id']
    if campo_a_modificar not in campos_permitidos:
        raise ValueError("Campo no válido para modificar")

    sql = f"UPDATE productos SET {campo_a_modificar} = ? WHERE id = ?"
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql, (nuevo_valor, id_prod))
    conn.commit()
    conn.close()

def obtener_productos_por_stock_db(limite):
    """Recupera productos cuya cantidad sea menor o igual a un límite.
    Args: limite: El número máximo de stock para el filtro.
 
    return: Lista de productos con stock bajo. 
    Formato de cada tupla:(id, nombre, descripcion, cantidad, precio, nombre_categoria).
        
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        SELECT p.id, p.nombre, p.descripcion, p.cantidad, p.precio, c.nombre
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        WHERE p.cantidad <= ?
        ORDER BY p.cantidad ASC
    """
    cursor.execute(sql, (limite,))
    productos = cursor.fetchall()
    conn.close()
    return productos