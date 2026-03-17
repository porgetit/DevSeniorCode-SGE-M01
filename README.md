# Sistema de Gestión de Estudiantes 🎓

Pequeño sistema de gestión académica desarrollado en **Python puro**, sin librerías externas, ejecutado completamente desde la terminal.

---

## Autor

- [Kevin Esgurra Cardona](mailto:kevin.esguerra@utp.edu.co)

---

## Problema

Una universidad necesita un programa que permita:

- Registrar estudiantes con sus datos básicos y tres notas.
- Calcular automáticamente el promedio y el estado académico.
- Persistir los datos entre sesiones. (`requisito personal`)
- Mostrar un resumen estadístico del grupo al finalizar.

---

## Solución propuesta

Se aplica **Programación Orientada a Objetos** dividiendo responsabilidades en capas independientes:

```
student_system/
├── main.py                  # Punto de entrada y menú principal
├── models/
│   └── student.py           # Dataclass Estudiante (modelo de datos)
├── db/
│   └── json_db.py           # Módulo de persistencia JSON (base de datos)
├── services/
│   └── student_service.py   # Lógica de negocio y reportes
├── utils/
│   └── validations.py       # Funciones de entrada validada
└── data/
    └── estudiantes.json     # Archivo generado automáticamente (DB)
```

### Decisiones de diseño

| Aspecto | Decisión |
|---|---|
| Modelo de datos | `@dataclass` con anotaciones de tipo. El promedio y el estado se calculan en `__post_init__`. |
| Persistencia | Archivo `JSON` gestionado por `JSONDatabase`. No requiere ningún motor de base de datos. |
| Validación | Funciones puras en `utils/validations.py` que repiten la entrada hasta recibir datos válidos. |
| Separación de capas | `main.py` solo orquesta el menú; `EstudianteService` contiene toda la lógica; `JSONDatabase` abstrae el almacenamiento. |
| Sin librerías externas | Solo módulos de la biblioteca estándar (`json`, `os`, `dataclasses`, `typing`). |

---

## Reglas del sistema

| Promedio | Estado académico |
|---|---|
| >= 4.0 | ✅ Aprobado |
| >= 3.0 y < 4.0 | ⚠️ En recuperación |
| < 3.0 | ❌ Reprobado |

**Validaciones:**
- Notas: deben estar entre **0.0** y **5.0**.
- Edad: debe ser un entero **mayor que 0**.
- Nombre: no puede estar vacío.

---

## Cómo ejecutar

```bash
# Desde la carpeta raíz del proyecto
python main.py
```

No se requiere instalar ningún paquete adicional.

---

## Ejemplo de sesión

```
╔══════════════════════════════════════╗
║    SISTEMA DE GESTIÓN DE ESTUDIANTES ║
╠══════════════════════════════════════╣
║  1. Registrar estudiante             ║
║  2. Ver todos los estudiantes        ║
║  3. Salir                            ║
╚══════════════════════════════════════╝
  Seleccione una opción: 1

  ── Datos del estudiante ──
  Nombre          : Ana
  Edad            : 20
  Nota 1 (0-5)    : 4.5
  Nota 2 (0-5)    : 3.8
  Nota 3 (0-5)    : 4.2

  ┌─────────────────────────────────────┐
  │  Nombre   : Ana                     │
  │  Edad     : 20                      │
  │  Notas    : 4.5 · 3.8 · 4.2        │
  │  Promedio : 4.17                    │
  │  Estado   : ✅ Aprobado             │
  └─────────────────────────────────────┘

...

         RESUMEN FINAL DEL GRUPO
═══════════════════════════════════════════════
  Total de estudiantes registrados : 3
  Promedio general del grupo       : 3.61
  ✅ Aprobados                     : 1
  ⚠️  En recuperación               : 1
  ❌ Reprobados                    : 1
═══════════════════════════════════════════════
```

---

## Estructura del JSON generado

```json
{
    "estudiantes": [
        {
            "nombre": "Ana",
            "edad": 20,
            "nota1": 4.5,
            "nota2": 3.8,
            "nota3": 4.2,
            "promedio": 4.17,
            "estado": "Aprobado"
        }
    ]
}
```
