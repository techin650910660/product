import uuid

class Product:
    def __init__(self, name, description, price, online_shop):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__online_shop = online_shop

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def online_shop(self):
        return self.__online_shop


class Customer:
    def __init__(self, name, email, address):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__cart = []
        self.__past_orders = []

    @property
    def name(self):
        return self.__name

    @property
    def cart(self):
        return self.__cart

    @property
    def past_orders(self):
        return self.__past_orders

    def add_to_cart(self, product, quantity):
        self.__cart.append({"product": product, "quantity": quantity})

    def clear_cart(self):
        self.__cart.clear()

    def add_order(self, order):
        self.__past_orders.append(order)


class OnlineShop:
    def __init__(self, name, url):
        self.__name = name
        self.__url = url
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def addingItemsToCart(self, customer, product, quantity):
        customer.add_to_cart(product, quantity)
        print(f"เพิ่ม {product.name} x{quantity} ลงตะกร้าของ {customer.name} แล้ว")

    def checkOut(self, customer):
        if not customer.cart:
            print("ตะกร้าว่าง ไม่สามารถชำระเงินได้")
            return

        total_price = sum(item["product"].price * item["quantity"] for item in customer.cart)
        order_id = str(uuid.uuid4())[:8]
        order = {
            "order_id": order_id,
            "items": [{"name": item["product"].name, "quantity": item["quantity"], "price": item["product"].price}
                      for item in customer.cart],
            "total": total_price
        }
        customer.add_order(order)
        customer.clear_cart()
        print(f"ชำระเงินสำเร็จ! รหัสคำสั่งซื้อ: {order_id} ยอดรวม: {total_price:.2f} บาท")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print("พบคำสั่งซื้อ:")
                print(f"รหัส: {order['order_id']}")
                for item in order["items"]:
                    print(f"- {item['name']} x{item['quantity']} @ {item['price']} บาท")
                print(f"รวมทั้งหมด: {order['total']:.2f} บาท")
                return
        print("ไม่พบคำสั่งซื้อที่ต้องการ")


shop = OnlineShop("Gadget World", "www.gadgetworld.com")

p1 = Product("Gaming Mouse Pro X", "เมาส์เกมมิ่งความเร็วสูง", 1200, shop)
p2 = Product("Mechanical Keyboard Z", "คีย์บอร์ดกลไกไฟ RGB", 2500, shop)

shop.add_product(p1)
shop.add_product(p2)

customer1 = Customer("สมชาย ใจดี", "somchai@email.com", "123 ถนนสุขใจ กรุงเทพฯ")

shop.addingItemsToCart(customer1, p1, 2)
shop.addingItemsToCart(customer1, p2, 1)

shop.checkOut(customer1)

order_id_test = customer1.past_orders[0]["order_id"]
shop.orderTracking(customer1, order_id_test)
