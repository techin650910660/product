class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)

    def show_products(self):
        if not self.__products:
            print("ไม่มีสินค้าในร้าน")
        else:
            for product in self.__products:
                print(f"สินค้า: {product.name}, จำนวน: {product.quantity}")


my_store = Store()
my_store.add_product("Laptop", 15)
my_store.add_product("Mouse", 50)
my_store.show_products()
