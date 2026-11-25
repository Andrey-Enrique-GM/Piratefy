from werkzeug.security import check_password_hash

from entities.usuario import Usuario
from persistence.db import get_db_connection


def consultar_uno(sql, params):
    """Ejecuta una consulta en la base real y regresa la primera fila"""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql, params)
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row


def test_save_guarda_al_usuario(email_prueba):
    """save registra al usuario en la tabla usuarios"""
    assert Usuario.save("Rosa", email_prueba, "secreta123") is True

    row = consultar_uno("SELECT nombre, email FROM usuarios WHERE email = %s", (email_prueba,))
    assert row["nombre"] == "Rosa"
    assert row["email"] == email_prueba


def test_save_guarda_password_hasheada(email_prueba):
    """La contraseña se guarda como hash, nunca tal cual"""
    Usuario.save("Rosa", email_prueba, "secreta123")

    row = consultar_uno("SELECT password FROM usuarios WHERE email = %s", (email_prueba,))
    assert row["password"] != "secreta123"
    assert check_password_hash(row["password"], "secreta123")


def test_save_crea_mis_favoritos(email_prueba):
    """Al registrarse, el usuario recibe su playlist 'Mis Favoritos'"""
    Usuario.save("Rosa", email_prueba, "secreta123")

    row = consultar_uno(
        """SELECT p.nombre FROM playlists p
           INNER JOIN usuarios u ON p.usuario_id = u.id
           WHERE u.email = %s""",
        (email_prueba,),
    )
    assert row["nombre"] == "Mis Favoritos"


def test_save_rechaza_email_repetido(email_prueba):
    """No se puede registrar dos veces el mismo correo"""
    assert Usuario.save("Rosa", email_prueba, "secreta123") is True
    assert Usuario.save("Otra Rosa", email_prueba, "otra-clave") is False