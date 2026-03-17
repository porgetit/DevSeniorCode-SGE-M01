from dataclasses import dataclass, field
from typing import Literal

EstadoAcademico = Literal["Aprobado", "En recuperación", "Reprobado"]


@dataclass
class Estudiante:
    """Representa un estudiante con sus datos académicos."""

    nombre: str
    edad: int
    nota1: float
    nota2: float
    nota3: float
    promedio: float = field(init=False)
    estado: EstadoAcademico = field(init=False)

    def __post_init__(self) -> None:
        self.promedio = round((self.nota1 + self.nota2 + self.nota3) / 3, 2)
        self.estado = self._evaluar_estado()

    def _evaluar_estado(self) -> EstadoAcademico:
        if self.promedio >= 4.0:
            return "Aprobado"
        elif self.promedio >= 3.0:
            return "En recuperación"
        return "Reprobado"

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "nota1": self.nota1,
            "nota2": self.nota2,
            "nota3": self.nota3,
            "promedio": self.promedio,
            "estado": self.estado,
        }

    @staticmethod
    def from_dict(data: dict) -> "Estudiante":
        return Estudiante(
            nombre=data["nombre"],
            edad=data["edad"],
            nota1=data["nota1"],
            nota2=data["nota2"],
            nota3=data["nota3"],
        )
