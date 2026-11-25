from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from persistence.db import get_db_connection



class Usuario(UserMixin):
    def __init__(self, nombre: str, email: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.email = email


    @staticmethod
    def check_email_exists(email: str) -> bool:
        connection = get_db_connection()
        cursor = connection.cursor()

        sql = "SELECT email FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()
        return row is not None

    @staticmethod
    def save(nombre: str, email: str, password: str) -> bool:
        connection = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            hash_password = generate_password_hash(password)

            sql = "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, email, hash_password))
            usuario_id = cursor.lastrowid

            sql = "INSERT INTO playlists (nombre, usuario_id) VALUES (%s, %s)"
            cursor.execute(sql, ("Mis Favoritos", usuario_id))

            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")
            return False
        finally:
            if connection:
                connection.close()

    @staticmethod
    def check_login(email: str, password: str):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            sql = "SELECT id, nombre, email, password FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email,))

            row = cursor.fetchone()

            cursor.close()
            connection.close()

            if row and check_password_hash(row["password"], password):
                return Usuario(nombre=row["nombre"], email=row["email"], id=row["id"])
            return None
        except Exception as e:
            print(f"Error al verificar el login: {e}")
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            sql = "SELECT id, nombre, email FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id,))

            row = cursor.fetchone()

            cursor.close()
            connection.close()

            if row:
                return Usuario(nombre=row["nombre"], email=row["email"], id=row["id"])
            return None
        except Exception as e:
            print(f"Error al obtener el usuario por ID: {e}")
            return None