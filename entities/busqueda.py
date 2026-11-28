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
                    SELECT c.id, c.nombre, c.archivo_audio, a.nombre AS artista, al.portada_url
                    FROM canciones c
                    INNER JOIN  artistas a ON c.artista_id = a.id
                    LEFT JOIN albumes al ON c.album_id = al.id
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
    
    @staticmethod
    def top_artists(limite=5):
        if not isinstance(limite, int) or limite < 1:
            return []
        conexion = get_db_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT a.id, a.nombre, COUNT(c.id) AS total_canciones
                    FROM artistas a
                    LEFT JOIN canciones c ON a.id = c.artista_id
                    GROUP BY a.id, a.nombre
                    ORDER BY total_canciones DESC, a.nombre ASC
                    LIMIT %s
                """, (limite,))
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conexion.close()

    @staticmethod
    def random_song():
        conexion = get_db_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT c.id, c.nombre, c.archivo_audio, a.nombre AS artista, al.portada_url
                    FROM canciones c
                    INNER JOIN artistas a ON c.artista_id = a.id
                    LEFT JOIN albumes al ON c.album_id = al.id
                    ORDER BY RAND()
                    LIMIT 1
                """)
                return cursor.fetchone()
        except Exception:
            return None
        finally:
            conexion.close()