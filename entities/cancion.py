from dataclasses import dataclass
from typing import Optional



@dataclass
class Cancion:
    nombre: str
    archivo_audio: str
    artista_id: int
    album_id: Optional[int] = None
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "Cancion":
        return cls(
            id=row.get("id"),
            nombre=row["nombre"],
            archivo_audio=row["archivo_audio"],
            artista_id=row["artista_id"],
            album_id=row.get("album_id"),
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "archivo_audio": self.archivo_audio,
            "artista_id": self.artista_id,
            "album_id": self.album_id,
        }
    