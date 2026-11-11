"""
Módulo de interfaz: menús y captura de datos.
Responsable: [Facundo]
"""


def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n=== GESTIÓN DE STOCK ===")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Ver alertas de stock bajo")
    print("4. Salir")


def pedir_datos_producto() -> dict:
    """Solicita al usuario los datos de un producto y los devuelve como dict."""
    nombre = input("Nombre: ").strip()
    precio = input("Precio: ").strip()
    cantidad = input("Cantidad: ").strip()

    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }