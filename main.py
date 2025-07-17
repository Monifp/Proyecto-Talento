 # main.py
"""
Módulo principal y punto de entrada para la aplicación de gestión. 🚀
"""
from colorama import init
import database as db
import ui
import productos
import categorias
import inventario

def main():
    """
    Ejecuta el ciclo de vida principal de la aplicación.
    Args: no tiene
    Returns: no tiene
    Descripción: Inicializa la base de datos, muestra el menú principal y
    gestiona las interacciones del usuario hasta que decida salir.
    """
    init(autoreset=True)
    db.inicializar_db()

    while True:
        ui.mostrar_menu_principal()
        opcion = ui.obtener_input(" Seleccione una opción: ")

        if opcion == '1':
            productos.gestionar_productos()
        elif opcion == '2':
            categorias.gestionar_categorias()
        elif opcion == '3':
            inventario.generar_reporte_stock_bajo()
        elif opcion == '4':
            ui.mostrar_mensaje_exito("Saliendo del programa. ¡Gracias!")
            break
        else:
            ui.mostrar_mensaje_error("Opción inválida.")

if __name__ == "__main__":
    main()