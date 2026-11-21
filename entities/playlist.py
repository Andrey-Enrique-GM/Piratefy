from dataclasses import dataclass
from typing import Optional



@dataclass
class Playlist:
    nombre: str
    usuario_id: int
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "Playlist":
        return cls(
            id=row.get("id"),
            nombre=row["nombre"],
            usuario_id=row["usuario_id"],
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario_id": self.usuario_id,
        }
    