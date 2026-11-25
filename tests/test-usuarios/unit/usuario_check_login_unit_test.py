from werkzeug.security import generate_password_hash
from entities.usuario import Usuario


def test_check_login_correct_password(database_connection):
    """Test check_login with the right email and password"""
    row = {"id": 3, "nombre": "Rosa", "email": "rosa@mail.com",
           "password": generate_password_hash("secreta123")}
    connection, cursor = database_connection(result=row)

    result = Usuario.check_login("rosa@mail.com", "secreta123")

    assert result is not None
    assert result.id == 3
    assert result.nombre == "Rosa"
    assert result.email == "rosa@mail.com"
    assert cursor.executed_queries[0] == (
        "SELECT id, nombre, email, password FROM usuarios WHERE email = %s"
    )
    assert cursor.executed_params[0] == ("rosa@mail.com",)
    assert cursor.closed
    assert connection.closed


def test_check_login_wrong_password(database_connection):
    """Test check_login returns None when the password is wrong"""
    row = {"id": 3, "nombre": "Rosa", "email": "rosa@mail.com",
           "password": generate_password_hash("secreta123")}
    connection, cursor = database_connection(result=row)

    result = Usuario.check_login("rosa@mail.com", "otra-clave")

    assert result is None


def test_check_login_email_not_found(database_connection):
    """Test check_login returns None when the email does not exist"""
    connection, cursor = database_connection(result=None)

    result = Usuario.check_login("nadie@mail.com", "secreta123")

    assert result is None


def test_check_login_database_error(database_connection):
    """Test check_login returns None if the database fails"""
    connection, cursor = database_connection(error=Exception("MySQL no responde"))

    result = Usuario.check_login("rosa@mail.com", "secreta123")

    assert result is None