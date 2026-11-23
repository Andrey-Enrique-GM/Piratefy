import os
import sys
from unittest.mock import MagicMock, patch

# Agrega la carpeta entities al path (../../entities)
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "..", "entities")
)

# Simula el módulo de base de datos para no usar una conexión real
sys.modules["persistance"] = MagicMock()
sys.modules["persistance.db"] = MagicMock()

from busqueda import Busqueda


def test_texto_vacio_devuelve_lista_vacia():
    assert Busqueda.by_name("") == []


def test_devuelve_resultados():
    filas = [(1, "Despacito", "Luis Fonsi")]

    cursor = MagicMock()
    cursor.fetchall.return_value = filas
    conexion = MagicMock()
    conexion.cursor.return_value.__enter__.return_value = cursor

    with patch("busqueda.get_db_connection", return_value=conexion):
        assert Busqueda.by_name("desp") == filas