from entities.usuario import Usuario


def test_check_email_exists_true(database_connection):
    """Test check_email_exists when the email is already registered"""
    connection, cursor = database_connection(result={"email": "rosa@mail.com"})

    result = Usuario.check_email_exists("rosa@mail.com")

    assert result is True
    assert cursor.executed_queries[0] == (
        "SELECT email FROM usuarios WHERE email = %s"
    )
    assert cursor.executed_params[0] == ("rosa@mail.com",)
    assert cursor.closed
    assert connection.closed


def test_check_email_exists_false(database_connection):
    """Test check_email_exists when the email is not registered"""
    connection, cursor = database_connection(result=None)

    result = Usuario.check_email_exists("nuevo@mail.com")

    assert result is False
    assert cursor.executed_params[0] == ("nuevo@mail.com",)
    assert cursor.closed
    assert connection.closed