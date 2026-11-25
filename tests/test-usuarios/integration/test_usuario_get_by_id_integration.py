from entities.usuario import Usuario


def test_get_by_id_existente(email_prueba):
    """Encuentra al usuario por su id"""
    Usuario.save("Rosa", email_prueba, "secreta123")
    registrado = Usuario.check_login(email_prueba, "secreta123")

    usuario = Usuario.get_by_id(registrado.id)

    assert usuario is not None
    assert usuario.id == registrado.id
    assert usuario.email == email_prueba


def test_get_by_id_inexistente():
    """Con un id que no existe regresa None"""
    assert Usuario.get_by_id(999999999) is None