"""
Sistema de Gestión de Stock — Célula 05
Actividad Práctica de la Semana 5: "La Célula en Acción"
"""

from interfaz import mostrar_menu, pedir_datos_producto
from validaciones import validar_producto
from salidas import listar_productos, mostrar_alertas

# Constante compartida por toda la célula
STOCK_MINIMO = 5


def main() -> None:
    """Bucle principal del sistema."""
    productos = []

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_producto()
            errores = validar_producto(datos)
            if errores:
                for error in errores:
                    print(f"✘ {error}")
            else:
                productos.append(datos)
                print("✔ Producto registrado.")

        elif opcion == "2":
            listar_productos(productos)

        elif opcion == "3":
            mostrar_alertas(productos, STOCK_MINIMO)

        elif opcion == "4":
            print("👋 Hasta luego.")
            break

        else:
            print("✘ Opción inválida. Elegí 1-4.")


if __name__ == "__main__":
    main()
