import pytest
from entities.artista import Artista

def test_save_artista():

    nombre = "artista_test"
    nuevo_id = Artista.save(nombre)

    assert nuevo_id is not None