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
    @staticmethod
    def formatear_duracion(segundos):
        """205 -> '3:25'"""
        if segundos < 0:
            raise ValueError("La duración no puede ser negativa")
        minutos, resto = divmod(int(segundos), 60)
        return f"{minutos}:{resto:02d}"

    @staticmethod
    def siguiente(total, indice, repetir=False):
        """Índice de la siguiente canción. Al llegar al final:
        vuelve a 0 si repetir, o None si no."""
        if total <= 0:
            return None
        if indice + 1 < total:
            return indice + 1
        return 0 if repetir else None

    @staticmethod
    def anterior(total, indice):
        """Índice de la canción anterior. En la primera se queda en 0."""
        if total <= 0:
            return None
        return max(indice - 1, 0)