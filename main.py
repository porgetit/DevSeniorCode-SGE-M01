"""
main.py — Punto de entrada del Sistema de Gestión de Estudiantes.
Ejecutar desde la carpeta raíz del proyecto:  python main.py
"""

import sys
import os

# Asegura que los módulos del proyecto sean encontrados
sys.path.insert(0, os.path.dirname(__file__))

from db.json_db import JSONDatabase
from services.student_service import EstudianteService
from utils.validations import pedir_opcion_menu


MENU = """
╔══════════════════════════════════════╗
║    SISTEMA DE GESTIÓN DE ESTUDIANTES ║
╠══════════════════════════════════════╣
║  1. Registrar estudiante             ║
║  2. Ver todos los estudiantes        ║
║  3. Salir                            ║
╚══════════════════════════════════════╝"""


def mostrar_todos(service: EstudianteService, db: JSONDatabase) -> None:
    registros = db.obtener_todos()
    if not registros:
        print("\n  No hay estudiantes registrados aún.")
        return
    print(f"\n  {'#':<4} {'Nombre':<20} {'Promedio':<10} Estado")
    print("  " + "-" * 48)
    for i, r in enumerate(registros, 1):
        print(f"  {i:<4} {r['nombre']:<20} {r['promedio']:<10} {r['estado']}")


def main() -> None:
    db      = JSONDatabase(filepath="data/estudiantes.json")
    service = EstudianteService(db)

    while True:
        print(MENU)
        opcion = pedir_opcion_menu(["1", "2", "3"])

        if opcion == "1":
            estudiante = service.registrar_estudiante()
            service.mostrar_ficha(estudiante)

        elif opcion == "2":
            mostrar_todos(service, db)

        elif opcion == "3":
            service.mostrar_resumen_final()
            print("\n  ¡Hasta luego!\n")
            break


if __name__ == "__main__":
    main()
