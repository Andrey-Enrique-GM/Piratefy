from dataclasses import dataclass
from typing import Optional
from persistence import get_db_connection



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


    @staticmethod
    def get_all():
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = """
                    SELECT 
                        p.id,
                        p.nombre,
                        u.nombre AS creador,
                        COUNT(pc.cancion_id) AS total_canciones
                    FROM playlists p
                    INNER JOIN usuarios u ON p.usuario_id = u.id
                    LEFT JOIN playlist_canciones pc ON p.id = pc.playlist_id
                    GROUP BY p.id, p.nombre, u.nombre
                    ORDER BY p.id ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
            finally:
                cursor.close()
        finally:
            connection.close()
