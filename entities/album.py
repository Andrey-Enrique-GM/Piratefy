from dataclasses import dataclass
from typing import Optional



@dataclass
class Album:
    nombre: str
    artista_id: int
    portada_url: Optional[str] = None
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "Album":
        return cls(
            id=row.get("id"),
            nombre=row["nombre"],
            artista_id=row["artista_id"],
            portada_url=row.get("portada_url"),
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "artista_id": self.artista_id,
            "portada_url": self.portada_url,
        }
    