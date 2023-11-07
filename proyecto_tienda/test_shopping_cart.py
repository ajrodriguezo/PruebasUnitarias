import unittest

from product import Product

class TestShoppingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('>>> El metodo de clase setUpClass se ejecuta antes de todas las pruebas')
    
    @classmethod
    def tearDownClass(cls):
        print('>>> El metodo de clase tearDownClass se ejecuta despues de todas las pruebas')
    
    def setUp(self):
        #print('>>> el metodo setUp se ejecuta antes de cada una de las pruebas')
        self.name = 'iPhone'
        self.price = 500.00
        
        self.smarthphone = Product(self.name, self.price)
        
    def tearDown(self):
        #print('>>> el metodo TearDown se ejecuta despues de cada una de las pruebas')
        pass
    
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70
        
        product = Product(name,price)
        
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)
        #self.assertEqual(product.price, price, 'Lo sentimos, el precio no es el mismo')
    
    def test_product_name(self):
        self.assertEqual(self.smarthphone.name, self.name)
        
    def test_product_price(self):
        self.assertEqual(self.smarthphone.price, self.price)
            

if __name__ == '__main__':
    unittest.main()