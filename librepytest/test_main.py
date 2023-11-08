import pytest

#def test_example():
#    assert 10 == 1, 'Lo sentimos, prueba no ha pasado'

class TestExample():
    
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Lo sentimos, la suma no es correcta.'
        
    def test_resta_dos_numeros(self):
        assert 10 - 10 == 0, 'Lo sentimos, la resta no es correcta.'

class TestExample2():

    def test_multipplicacion_dos_numeros(self):
        assert 2 * 10 == 20