from persistence.db import get_db_connection



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
                    INNER JOIN  artistas a ON c.artista_id = a.id
                    WHERE c.nombre LIKE %s""", 
                    (f"%{texto}%",)
                )
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conexion.close()

    @staticmethod
    def by_artist(texto):
        if not texto or not texto.strip():
            return []
        conexion = get_db_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT a.id, a.nombre, COUNT(c.id) AS total_cancines 
                    FROM artistas a
                    LEFT JOIN canciones c ON a.id = c.artista_id
                    WHERE a.nombre LIKE %s
                    GROUP BY a.id, a.nombre
                    ORDER BY total_cancines DESC
                    LIMIT 10
                """, (f"%{texto}%",))
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conexion.close()