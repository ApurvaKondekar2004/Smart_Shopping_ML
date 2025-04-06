class ProductAgent:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, category, subcategory, price):
        self.products[product_id] = {
            'Category': category,
            'Subcategory': subcategory,
            'Price': price
        }
