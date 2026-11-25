import pytest
from entities.artista import Artista

def test_get_all_artista():

    artistas = Artista.get_all()

    assert isinstance(artistas, list)