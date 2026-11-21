from dataclasses import dataclass
from typing import Optional



@dataclass
class Artista:
    nombre: str
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "Artista":
        return cls(
            id=row.get("id"),
            nombre=row["nombre"],
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
    