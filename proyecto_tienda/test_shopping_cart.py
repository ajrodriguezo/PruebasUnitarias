import unittest

from product import Product
from product import ProductDiscountError
from shopping_car import ShoppingCart

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
        self.shopping_cart_1  = ShoppingCart()
        
        self.shopping_cart_2  = ShoppingCart()
        self.shopping_cart_2.add_product(self.smarthphone)
        
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
    
    def test_shopping_cart_empty (self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no se encientra vacío.')
        
    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())
    
    def test_product_in_shopping_cart(self):
                
        product = Product('Nuevo producto',10)
        self.shopping_cart_2.add_product(product)
        
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smarthphone, self.shopping_cart_2.products)
    
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smarthphone)
        self.lista = self.shopping_cart_2.products
        self.assertNotIn(self.smarthphone, self.lista)    
    
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name= 'Example', price= 10.0, discount= 11.0)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name= 'libro',price= 15.0 ))
        self.shopping_cart_1.add_product(Product(name= 'camara',price= 700, discount= 70 ))

        self.assertGreater(self.shopping_cart_1.totlal, 0) # nos permite evaluar x > algo
        self.assertLess(self.shopping_cart_1.totlal, 1000) # nos permite evualr x < algo 
        self.assertEqual(self.shopping_cart_1.totlal, 645.00)
        #assertGreatEqual mayor o igula
        #asserLessEqual Menor o igual 
        
    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.totlal, 0.0)
        

if __name__ == '__main__':
    unittest.main()