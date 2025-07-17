 # inventario.py
"""
Módulo para gestionar operaciones de inventario, como reportes de stock.
Responsable de generar reportes de productos con stock bajo,
permitiendo al usuario establecer un límite de cantidad.
"""
import database as db
import ui

def generar_reporte_stock_bajo():
    """
    Guía al usuario para generar un reporte de productos con stock bajo.
    Solicita un límite de cantidad y muestra los productos que cumplen con ese criterio.
    Si no hay productos con stock bajo, muestra un mensaje informativo. 
    Args: no tiene
    Returns: no tiene
    """
    ui.mostrar_mensaje_info("Se generará un reporte de productos con poco stock.")

    while True:
        try:
            limite_str = ui.obtener_input("Ingrese el límite de cantidad para el reporte: ")
            limite = int(limite_str)
            if limite >= 0:
                break
            else:
                ui.mostrar_mensaje_error("El límite no puede ser un número negativo.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un número entero válido.")

    productos_bajos_stock = db.obtener_productos_por_stock_db(limite)
    ui.mostrar_reporte_stock(productos_bajos_stock, limite)