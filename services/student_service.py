from models.student import Estudiante
from db.json_db import JSONDatabase
from utils.validations import pedir_texto, pedir_entero_positivo, pedir_nota


class EstudianteService:
    """Capa de servicio: orquesta el registro, persistencia y reporte de estudiantes."""

    def __init__(self, db: JSONDatabase) -> None:
        self._db = db

    # ------------------------------------------------------------------ #
    #  Registro                                                            #
    # ------------------------------------------------------------------ #

    def registrar_estudiante(self) -> Estudiante:
        """Solicita datos al usuario, construye y persiste un Estudiante."""
        print("\n  ── Datos del estudiante ──")
        nombre = pedir_texto("  Nombre          : ")
        edad   = pedir_entero_positivo("  Edad            : ")
        nota1  = pedir_nota("  Nota 1 (0-5)    : ")
        nota2  = pedir_nota("  Nota 2 (0-5)    : ")
        nota3  = pedir_nota("  Nota 3 (0-5)    : ")

        estudiante = Estudiante(nombre, edad, nota1, nota2, nota3)
        self._db.guardar_estudiante(estudiante.to_dict())
        return estudiante

    # ------------------------------------------------------------------ #
    #  Reporte                                                             #
    # ------------------------------------------------------------------ #

    def mostrar_ficha(self, estudiante: Estudiante) -> None:
        """Imprime la ficha individual del estudiante registrado."""
        estado_icon = {"Aprobado": "✅", "En recuperación": "⚠️ ", "Reprobado": "❌"}
        icon = estado_icon.get(estudiante.estado, "")
        print(f"""
  ┌─────────────────────────────────────┐
  │  Nombre   : {estudiante.nombre:<24} │
  │  Edad     : {estudiante.edad:<24} │
  │  Notas    : {estudiante.nota1} · {estudiante.nota2} · {estudiante.nota3:<16} │
  │  Promedio : {estudiante.promedio:<24} │
  │  Estado   : {icon} {estudiante.estado:<21} │
  └─────────────────────────────────────┘""")

    def mostrar_resumen_final(self) -> None:
        """Lee la DB y muestra el resumen del grupo completo."""
        registros = self._db.obtener_todos()
        total = len(registros)

        print("\n" + "=" * 45)
        print("         RESUMEN FINAL DEL GRUPO")
        print("=" * 45)

        if total == 0:
            print("  No se registraron estudiantes en esta sesión.")
            return

        promedio_general = sum(r["promedio"] for r in registros) / total
        aprobados        = sum(1 for r in registros if r["estado"] == "Aprobado")
        recuperacion     = sum(1 for r in registros if r["estado"] == "En recuperación")
        reprobados       = sum(1 for r in registros if r["estado"] == "Reprobado")

        print(f"  Total de estudiantes registrados : {total}")
        print(f"  Promedio general del grupo       : {promedio_general:.2f}")
        print(f"  ✅ Aprobados                     : {aprobados}")
        print(f"  ⚠️  En recuperación               : {recuperacion}")
        print(f"  ❌ Reprobados                    : {reprobados}")
        print("=" * 45)
