from persistence import get_db_connection



class Artista:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    @staticmethod
    def save(nombre):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = "INSERT INTO artistas (nombre) VALUES (%s)"
                cursor.execute(sql, (nombre,))
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
                sql = "SELECT id, nombre FROM artistas ORDER BY nombre ASC"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [Artista(row["id"], row["nombre"]) for row in rows]
            finally:
                cursor.close()
        finally:
            connection.close()
