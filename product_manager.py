from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Total inventory value: {total}")
        return total

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed product: {product_name}")
                return
        print(f"Product not found: {product_name}")