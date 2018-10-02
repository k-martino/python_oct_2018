class Product:
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = round(self.price * (1 + tax), 2)
        return self
    
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price *= 0.8
        else:
            print(f"\n{reason_for_return} is invalid. Please enter one of the following: 'defective', 'like_new', or 'opened'")
        return self
    
    def display_info(self):
        print(f"\nPrice: ${self.price} \nItem Name: {self.name} \nWeight: {self.weight} \nBrand: {self.brand} \nStatus: {self.status} \n")
        return self

Product1 = Product(10000, "Sofa", "50lbs", "Knoll")
Product1.add_tax(0.08).sell().return_item("opened").display_info()
