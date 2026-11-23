from persistance.db import get_db_connection

class Busqueda:
    @staticmethod

    def by_name(texto):
        if not texto or not texto.strip():
            return []
        conexion = get_db_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT c.id, c.nombre, a.nombre AS artista FROM canciones c
                    INNER JOIN  artista a ON c.artista_id = a.id
                    WHERE c.nombre LIKE %s""", 
                    (f"%{texto}%",)
                )
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conexion.close()