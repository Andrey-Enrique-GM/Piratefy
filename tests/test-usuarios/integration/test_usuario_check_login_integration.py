from entities.usuario import Usuario


def test_login_correcto(email_prueba):
    """Con el correo y la contraseña correctos regresa al usuario"""
    Usuario.save("Rosa", email_prueba, "secreta123")

    usuario = Usuario.check_login(email_prueba, "secreta123")

    assert usuario is not None
    assert usuario.nombre == "Rosa"
    assert usuario.email == email_prueba


def test_login_password_incorrecta(email_prueba):
    """Con una contraseña equivocada no deja entrar"""
    Usuario.save("Rosa", email_prueba, "secreta123")

    assert Usuario.check_login(email_prueba, "otra-clave") is None


def test_login_email_inexistente(email_prueba):
    """Con un correo que no está registrado no deja entrar"""
    assert Usuario.check_login(email_prueba, "secreta123") is None