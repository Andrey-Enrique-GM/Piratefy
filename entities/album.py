from dataclasses import dataclass
from typing import Optional
from persistence import get_db_connection



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


    @staticmethod
    def save(nombre: str, artista_id: int, portada_url: Optional[str] = None):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = "INSERT INTO albumes (nombre, artista_id, portada_url) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, artista_id, portada_url or None))
                nuevo_id = cursor.lastrowid
                connection.commit()
                return nuevo_id
            except Exception:
                connection.rollback()
                return None
            finally:
                cursor.close()
        finally:
            connection.close()


    @staticmethod
    def get_all():
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = """
                    SELECT al.id, al.nombre, al.artista_id, al.portada_url, a.nombre AS artista_nombre
                    FROM albumes al
                    INNER JOIN artistas a ON al.artista_id = a.id
                    ORDER BY al.nombre ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
            finally:
                cursor.close()
        finally:
            connection.close()
