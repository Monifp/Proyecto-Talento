# Sistema de Gestión de Inventario 📦

Este es un sistema de gestión de inventario que se ejecuta desde la consola. Permite a los usuarios administrar productos y sus categorías, con una interfaz interactiva y coloreada para una mejor experiencia de usuario.

-----

## ✨ Características Principales

  * **Gestión Completa de Productos:** Creá, modificá, visualizá, buscá y eliminá productos.
  * **Gestión Completa de Categorías:** Administrá las categorías de tus productos.
  * **Creación de Categorías sobre la marcha:** Si necesitás una nueva categoría al agregar un producto, podés crearla en el momento sin interrumpir el flujo.
  * **Búsqueda y Eliminación por ID:** Operaciones precisas utilizando el ID único del producto.
  * **Validación de Datos:** Asegura que los datos ingresados sean correctos (ej: precios no negativos, cantidades positivas, descripciones no vacías).
  * **Reporte de Stock Bajo:** Generá un reporte de los productos cuya cantidad en stock sea igual o inferior a un límite que vos definas.
  * **Interfaz de Usuario Amigable:** Menús claros y mensajes con colores que guían al usuario en todo momento.
  * **Integridad de Datos:** Utiliza claves foráneas para asegurar que no se puedan eliminar categorías que tengan productos asociados.

-----

## 📋 Requisitos

  * Python 3.8 o superior
  * Librería `colorama`
  * SQLite (incluido en Python estándar)
  * Sphinx (opcional, para documentación)

-----

## ⚙️ Instalación

1.  **Cloná el repositorio** desde GitHub:

    ```bash
    git clone https://github.com/Monifp/Proyecto-Talento.git
    cd Proyecto-Talento
    ```

2.  **Instalá las dependencias** usando pip:

    ```bash
    pip install colorama
    ```

-----

## 🚀 Uso

  * Para **iniciar la aplicación principal**, ejecutá el siguiente comando en tu terminal:

    ```bash
    python main.py
    ```


-----

## 📂 Estructura del Proyecto

El proyecto está dividido en módulos, cada uno con una responsabilidad única para mantener el código organizado y escalable.

| Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | 🧠 **Orquestador Principal:** Inicia la aplicación y ejecuta el bucle del menú principal. |
| `ui.py` | 🎨 **Interfaz de Usuario:** Maneja toda la interacción con el usuario (menús, mensajes, etc.). |
| `database.py`| 🗃️ **Capa de Datos:** Gestiona toda la comunicación con la base de datos `inventario.db`. |
| `productos.py`| 📦 **Lógica de Productos:** Contiene las reglas de negocio para las operaciones de productos. |
| `categorias.py`| 📋 **Lógica de Categorías:** Contiene las reglas de negocio para la gestión de las categorías. |
| `inventario.py`| 📊 **Lógica de Inventario:** Contiene la funcionalidad para generar reportes y análisis. |
| `inventario.db`| 💾 **Base de Datos:** Archivo SQLite que se crea automáticamente para almacenar los datos. |


## 📖 Documentacion

  * Para **ver la documentacion**, segui el siguiente link:

    https://monifp.github.io/Proyecto-Talento/

    
## 🧑‍💻 Copyright

**Monica Ferreiro Pose**
-----
