import json
import os
from typing import Any


class JSONDatabase:
    """Módulo de persistencia simple basado en un archivo JSON."""

    def __init__(self, filepath: str = "data/estudiantes.json") -> None:
        self._filepath = filepath
        self._ensure_file()

    def _ensure_file(self) -> None:
        """Crea el archivo y los directorios necesarios si no existen."""
        os.makedirs(os.path.dirname(self._filepath), exist_ok=True)
        if not os.path.exists(self._filepath):
            self._write({"estudiantes": []})

    def _read(self) -> dict:
        with open(self._filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: dict) -> None:
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def guardar_estudiante(self, estudiante_dict: dict[str, Any]) -> None:
        """Agrega un estudiante al archivo JSON."""
        data = self._read()
        data["estudiantes"].append(estudiante_dict)
        self._write(data)

    def obtener_todos(self) -> list[dict[str, Any]]:
        """Retorna la lista de todos los estudiantes almacenados."""
        return self._read().get("estudiantes", [])

    def total_registros(self) -> int:
        """Retorna el número total de estudiantes almacenados."""
        return len(self.obtener_todos())

    def limpiar(self) -> None:
        """Elimina todos los registros (útil para pruebas)."""
        self._write({"estudiantes": []})
