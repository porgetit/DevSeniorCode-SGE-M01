NOTA_MIN: float = 0.0
NOTA_MAX: float = 5.0


def pedir_texto(mensaje: str) -> str:
    """Solicita una cadena de texto no vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ⚠ El valor no puede estar vacío. Intente de nuevo.")


def pedir_entero_positivo(mensaje: str) -> int:
    """Solicita un entero estrictamente mayor que 0."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  ⚠ El valor debe ser mayor que 0.")
        except ValueError:
            print("  ⚠ Ingrese un número entero válido.")


def pedir_nota(mensaje: str) -> float:
    """Solicita una nota dentro del rango [NOTA_MIN, NOTA_MAX]."""
    while True:
        try:
            valor = float(input(mensaje))
            if NOTA_MIN <= valor <= NOTA_MAX:
                return valor
            print(f"  ⚠ La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}.")
        except ValueError:
            print("  ⚠ Ingrese un número válido (use punto como decimal).")


def pedir_opcion_menu(opciones: list[str]) -> str:
    """Solicita una opción válida del menú."""
    while True:
        valor = input("  Seleccione una opción: ").strip()
        if valor in opciones:
            return valor
        print(f"  ⚠ Opción inválida. Elija entre: {', '.join(opciones)}")
