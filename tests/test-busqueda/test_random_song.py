
from unittest.mock import MagicMock, patch

from entities.busqueda import Busqueda


def _conexion_falsa():
    cursor = MagicMock()
    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor
    return conexion


def test_random_song_devuelve_cancion():
    fila = {
        "id": 1,
        "nombre": "Querida",
        "archivo_audio": "querida.mp3",
        "artista": "Juan Gabriel",
        "portada_url": "portada.jpg"
    }

    conexion = _conexion_falsa()
    cursor = conexion.cursor.return_value.__enter__.return_value
    cursor.fetchone.return_value = fila

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.random_song() == fila

    conexion.close.assert_called_once()


def test_random_song_sin_resultados():
    conexion = _conexion_falsa()
    cursor = conexion.cursor.return_value.__enter__.return_value
    cursor.fetchone.return_value = None

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.random_song() is None

    conexion.close.assert_called_once()


def test_random_song_error_en_bd_devuelve_none():
    conexion = _conexion_falsa()
    cursor = conexion.cursor.return_value.__enter__.return_value
    cursor.execute.side_effect = Exception("fallo")

    with patch("entities.busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.random_song() is None

    conexion.close.assert_called_once()
