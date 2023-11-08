from product import Product
class ShoppingCart:
    
    def __init__(self) -> None:
        #self.__products = list()
        self.__products: List[Product] =[]
    
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
    
    def empty(self) -> bool:
        return len(self.__products) == 0 
    
    def has_products(self):
        return not self.empty()