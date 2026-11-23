import pymysql
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from persistence.db import get_db_connection



class Usuario(UserMixin):
    def __init__(self, nombre:str, email:str, password: str, id:int =None):
        self.id= id
        self.nombre = nombre
        self.email = email
        self.password = password


    @staticmethod
    def check_email_exists(email) -> bool:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        sql = "SELECT email FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()
        return row is not None
    
    @staticmethod
    def save(nombre: str, email: str, password: str):
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
            connection.close()
            return True
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")
            return False