import pytest

#def test_example():
#    assert 10 == 1, 'Lo sentimos, prueba no ha pasado'

class TestExample():
    
    @classmethod
    def setup_class(cls):
        print('>>> setup_class se ejecuta antes de todas las pruebas')
    
    @classmethod
    def teardown_class(cls):
        print('>>> teardown_class se ejecuta despues de todas las pruebas')

    
    def setup_method(self):
        #print('>>> El metodo setup se ejecuta antes de cada prueba')
        self.numero_uno = 10
        self.numero_dos = 20
        
    
    def teardown_method(self):
        print('>>> El metodo teardown se ejecuta despues de cada prueba')
    
    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 30, 'Lo sentimos, la suma no es correcta.'
        
    def test_resta_dos_numeros(self):
        assert self.numero_uno - self.numero_dos == -10, 'Lo sentimos, la resta no es correcta.'

class TestExample2():

    def test_multipplicacion_dos_numeros(self):
        assert 2 * 10 == 20