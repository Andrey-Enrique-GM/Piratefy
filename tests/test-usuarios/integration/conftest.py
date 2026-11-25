import uuid

import pytest

from persistence.db import get_db_connection


@pytest.fixture
def email_prueba():
    """Genera un correo único para la prueba y, al terminar, borra al usuario de la base.
    Su playlist 'Mis Favoritos' se borra sola por el ON DELETE CASCADE."""
    email = f"prueba_{uuid.uuid4().hex[:8]}@piratefy.test"
    yield email

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE email = %s", (email,))
    connection.commit()
    cursor.close()
    connection.close()