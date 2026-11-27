from unittest.mock import MagicMock, patch

from entities.busqueda import Busqueda


def _conexion_falsa(filas):
    cursor = MagicMock()
    cursor.fetchall.return_value = filas
    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor
    return conexion


def test_by_name_devuelve_resultados():
    filas = [{"id": 1, "nombre": "Querida", "artista": "X"}]
    conexion = _conexion_falsa(filas)
    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.by_name("quer") == filas
    conexion.close.assert_called_once()


def test_by_name_texto_vacio():
    assert Busqueda.by_name("   ") == []