from entities.usuario import Usuario


def test_email_no_registrado(email_prueba):
    """Un correo que nadie ha usado no existe"""
    assert Usuario.check_email_exists(email_prueba) is False


def test_email_registrado(email_prueba):
    """Después de registrar al usuario, su correo sí existe"""
    Usuario.save("Rosa", email_prueba, "secreta123")

    assert Usuario.check_email_exists(email_prueba) is True