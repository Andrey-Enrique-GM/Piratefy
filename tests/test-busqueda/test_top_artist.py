
from unittest.mock import MagicMock, patch

from entities.busqueda import Busqueda


def _conexion_falsa(filas):
    cursor = MagicMock()
    cursor.fetchall.return_value = filas
    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor
    return conexion


def test_top_artists_devuelve_resultados():
    filas = [
        {"id": 1, "nombre": "Bad Bunny", "total_canciones": 10},
        {"id": 2, "nombre": "Wos", "total_canciones": 8}
    ]
    conexion = _conexion_falsa(filas)

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.top_artists(2) == filas

    conexion.close.assert_called_once()


def test_top_artists_usa_el_limite_en_consulta():
    conexion = _conexion_falsa([])

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        Busqueda.top_artists(3)

    cursor = conexion.cursor.return_value.__enter__.return_value
    assert cursor.execute.call_args[0][1] == (3,)


def test_top_artists_limite_invalido():
    assert Busqueda.top_artists(0) == []
    assert Busqueda.top_artists(-1) == []
    assert Busqueda.top_artists("5") == []


def test_top_artists_error_en_bd_devuelve_lista_vacia():
    conexion = _conexion_falsa([])
    cursor = conexion.cursor.return_value.__enter__.return_value
    cursor.execute.side_effect = Exception("fallo")

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.top_artists(5) == []

    conexion.close.assert_called_once()
