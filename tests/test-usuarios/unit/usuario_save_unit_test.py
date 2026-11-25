from werkzeug.security import check_password_hash
from entities.usuario import Usuario


def test_usuario_save(database_connection):
    """Test the save method of the Usuario class"""
    connection, cursor = database_connection(lastrowid=7)

    result = Usuario.save("Rosa", "rosa@mail.com", "secreta123")

    assert result is True
    assert cursor.executed_queries[0] == (
        "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
    )
    assert cursor.executed_params[0][0] == "Rosa"
    assert cursor.executed_params[0][1] == "rosa@mail.com"
    assert connection.committed
    assert cursor.closed
    assert connection.closed


def test_usuario_save_hashes_password(database_connection):
    """Test that save stores the password hashed, never in plain text"""
    connection, cursor = database_connection(lastrowid=7)

    Usuario.save("Rosa", "rosa@mail.com", "secreta123")

    saved_password = cursor.executed_params[0][2]
    assert saved_password != "secreta123"
    assert check_password_hash(saved_password, "secreta123")


def test_usuario_save_creates_mis_favoritos(database_connection):
    """Test that save creates the 'Mis Favoritos' playlist for the new user"""
    connection, cursor = database_connection(lastrowid=7)

    Usuario.save("Rosa", "rosa@mail.com", "secreta123")

    assert cursor.executed_queries[1] == (
        "INSERT INTO playlists (nombre, usuario_id) VALUES (%s, %s)"
    )
    assert cursor.executed_params[1] == ("Mis Favoritos", 7)


def test_usuario_save_error(database_connection):
    """Test that save returns False and does not commit if the database fails"""
    connection, cursor = database_connection(error=Exception("MySQL no responde"))

    result = Usuario.save("Rosa", "rosa@mail.com", "secreta123")

    assert result is False
    assert not connection.committed