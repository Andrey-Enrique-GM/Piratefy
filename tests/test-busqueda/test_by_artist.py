import os
import sys
from unittest.mock import MagicMock, patch

# Agrega la carpeta entities al path (../../entities)
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "..", "entities")
)

# Simula el módulo de base de datos para no usar una conexión real
sys.modules["persistence"] = MagicMock()
sys.modules["persistence.db"] = MagicMock()

from busqueda import Busqueda


def test_by_artist():
    filas = [
        (2, "Queen", 15),
        (5, "Soda Stereo", 10)
    ]

    cursor = MagicMock()
    cursor.fetchall.return_value = filas

    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor

    with patch("busqueda.get_db_connection", return_value=conexion):
        resultado = Busqueda.by_artist("Queen")
        assert resultado == filas

    conexion.close.assert_called_once()

    artista_mayor = max(filas, key=lambda artista: artista[2])
    print(f"El artista con más discos es: {artista_mayor[1]} con {artista_mayor[2]} discos")