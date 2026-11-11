"""
Módulo de validaciones: reglas de negocio y control de errores.
Responsable: [Silvina]
"""


def validar_nombre(nombre: str) -> str | None:
    """Devuelve un mensaje de error si el nombre es inválido."""
    if not nombre:
        return "El nombre no puede estar vacío."
    if len(nombre) > 50:
        return "El nombre no puede superar los 50 caracteres."
    return None


def validar_precio(precio: str) -> str | None:
    """Devuelve un mensaje de error si el precio es inválido."""
    try:
        valor = float(precio)
    except ValueError:
        return "El precio debe ser un número."
    if valor <= 0:
        return "El precio debe ser mayor que cero."
    return None


def validar_cantidad(cantidad: str) -> str | None:
    """Devuelve un mensaje de error si la cantidad es inválida."""
    try:
        valor = int(cantidad)
    except ValueError:
        return "La cantidad debe ser un número entero."
    if valor < 0:
        return "La cantidad no puede ser negativa."
    return None


def validar_producto(datos: dict) -> list[str]:
    """Valida un producto completo y devuelve la lista de errores encontrados."""
    errores = []

    error_nombre = validar_nombre(datos.get("nombre", ""))
    if error_nombre:
        errores.append(error_nombre)

    error_precio = validar_precio(datos.get("precio", ""))
    if error_precio:
        errores.append(error_precio)

    error_cantidad = validar_cantidad(datos.get("cantidad", ""))
    if error_cantidad:
        errores.append(error_cantidad)

    return errores
