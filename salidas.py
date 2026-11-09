"""
Módulo de salidas: formateo de resultados y reportes.
Responsable: [Nombre 3]
"""


def listar_productos(productos: list[dict]) -> None:
    """Muestra todos los productos registrados en formato de tabla."""
    if not productos:
        print("ℹ No hay productos registrados.")
        return

    print("\n--- LISTADO DE PRODUCTOS ---")
    print(f"{'N°':<4}{'Nombre':<20}{'Precio':>10}{'Cantidad':>10}")
    print("-" * 44)

    for i, p in enumerate(productos, start=1):
        nombre = p["nombre"][:18]
        precio = float(p["precio"])
        cantidad = int(p["cantidad"])
        print(f"{i:<4}{nombre:<20}{precio:>10.2f}{cantidad:>10}")


def mostrar_alertas(productos: list[dict], stock_minimo: int) -> None:
    """Muestra los productos cuyo stock está por debajo del mínimo."""
    if not productos:
        print("ℹ No hay productos registrados.")
        return

    alertas = [p for p in productos if int(p["cantidad"]) < stock_minimo]

    if not alertas:
        print(f"✔ Todos los productos tienen stock ≥ {stock_minimo}.")
        return

    print(f"\n⚠ ALERTAS — Productos con stock menor a {stock_minimo}:")
    for p in alertas:
        print(f"  • {p['nombre']} → stock actual: {p['cantidad']}")


def mostrar_resumen(productos: list[dict]) -> None:
    """Muestra un resumen general del inventario."""
    if not productos:
        print("ℹ No hay productos registrados.")
        return

    total_unidades = sum(int(p["cantidad"]) for p in productos)
    valor_total = sum(float(p["precio"]) * int(p["cantidad"]) for p in productos)

    print("\n--- RESUMEN DEL INVENTARIO ---")
    print(f"Productos distintos : {len(productos)}")
    print(f"Unidades totales    : {total_unidades}")
    print(f"Valor total         : ${valor_total:.2f}")