from unittest.mock import MagicMock, patch

from entities.busqueda import Busqueda


def _conexion_falsa(filas):
    cursor = MagicMock()
    cursor.fetchall.return_value = filas
    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor
    return conexion

def test_by_artist_devuelve_resultados():
    filas = [{"id": 1, "nombre": "Bad Bunny", "total_canciones": 3}]
    conexion = _conexion_falsa(filas)
    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.by_artist("bad") == filas
    conexion.close.assert_called_once()


def test_by_artist_usa_el_texto_en_la_consulta():
    conexion = _conexion_falsa([])
    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        Busqueda.by_artist("bad")
    cursor = conexion.cursor.return_value.__enter__.return_value
    assert cursor.execute.call_args[0][1] == ("%bad%",)


def test_by_artist_texto_vacio():
    assert Busqueda.by_artist("   ") == []


def test_by_artist_error_en_bd_devuelve_lista_vacia():
    conexion = _conexion_falsa([])
    cursor = conexion.cursor.return_value.__enter__.return_value
    cursor.execute.side_effect = Exception("fallo")
    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.by_artist("bad") == []
    conexion.close.assert_called_once()