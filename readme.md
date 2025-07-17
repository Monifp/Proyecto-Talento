# Proyecto Talento

Sistema de Gestión de Inventario 📦

Este es un sistema de gestión de inventario que se ejecuta desde la consola.
Permite a los usuarios administrar productos y sus categorías, con una interfaz interactiva y coloreada para una mejor experiencia de usuario.

✨ Características Principales
Gestión Completa de Productos: Creá, modificá, visualizá, buscá y eliminá productos.

Gestión Completa de Categorías: Administrá las categorías de tus productos.

Creación de Categorías sobre la marcha: Si al agregar un producto necesitás una nueva categoría, podés crearla en el momento sin interrumpir el flujo.

Búsqueda y Eliminación por ID: Operaciones utilizando el ID único del producto.

Validación de Datos: Asegura que los datos ingresados sean correctos (ej: precios no negativos, cantidades positivas, descripciones no vacías).

Reporte de Stock Bajo: Generá un reporte de los productos cuya cantidad en stock sea igual o inferior a un límite que vos definas.

Interfaz de Usuario Amigable: Menús claros y mensajes con colores que guían al usuario en todo momento.

Integridad de Datos: Utiliza claves foráneas para asegurar que no se puedan eliminar categorías que tengan productos asociados.

📋 Requisitos
Python 3.x

Librería colorama

⚙️ Instalación

Cloná el repositorio desde Github (o descargá los archivos en una carpeta):

https://github.com/Monifp/Proyecto-Talento.git

 
Instalá las dependencias usando pip:

Bash

pip install colorama


🚀 Uso

Para iniciar la aplicación principal, ejecutá el siguiente comando en tu terminal:

Bash

python main.py


Para ver una descripción de cómo está estructurado el proyecto y qué hace cada módulo, podés ejecutar el archivo de ayuda:

Bash

python ayuda.py


📂 Estructura del Proyecto

El proyecto está dividido en módulos, cada uno con una responsabilidad única para mantener el código organizado y escalable.

main.py: 🧠 Orquestador Principal. Inicia la aplicación y ejecuta el bucle del menú principal, delegando las tareas a los otros módulos.

ui.py: 🎨 Interfaz de Usuario. El único módulo responsable de toda la interacción con el usuario (mostrar menús, mensajes y recibir datos).

database.py: 🗃️ Capa de Datos. Gestiona toda la comunicación con la base de datos inventario.db. Contiene todas las sentencias SQL.

productos.py: 📦 Lógica de Productos. Contiene las reglas de negocio para todas las operaciones relacionadas con los productos.

categorias.py: 📋 Lógica de Categorías. Contiene las reglas de negocio para la gestión de las categorías.

inventario.py: 📊 Lógica de Inventario. Contiene la funcionalidad para generar reportes y análisis sobre el stock.

inventario.db: El archivo de base de datos SQLite que se crea automáticamente al ejecutar la aplicación por primera vez.


