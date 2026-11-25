from entities.usuario import Usuario


def test_get_by_id_found(database_connection):
    """Test get_by_id returns the Usuario when the id exists"""
    row = {"id": 3, "nombre": "Rosa", "email": "rosa@mail.com"}
    connection, cursor = database_connection(result=row)

    result = Usuario.get_by_id(3)

    assert result is not None
    assert result.id == 3
    assert result.nombre == "Rosa"
    assert cursor.executed_queries[0] == (
        "SELECT id, nombre, email FROM usuarios WHERE id = %s"
    )
    assert cursor.executed_params[0] == (3,)
    assert cursor.closed
    assert connection.closed


def test_get_by_id_not_found(database_connection):
    """Test get_by_id returns None when the id does not exist"""
    connection, cursor = database_connection(result=None)

    result = Usuario.get_by_id(999)

    assert result is None


def test_get_by_id_database_error(database_connection):
    """Test get_by_id returns None if the database fails"""
    connection, cursor = database_connection(error=Exception("MySQL no responde"))

    result = Usuario.get_by_id(3)

    assert result is None