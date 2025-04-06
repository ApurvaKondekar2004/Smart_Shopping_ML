class CustomerAgent:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, location, region, gender):
        self.customers[customer_id] = {
            'Location': location,
            'Region': region,
            'Gender': gender
        }
