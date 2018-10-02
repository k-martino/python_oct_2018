class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print(f"Price: ${self.price} \nSpeed: {self.speed} \nFuel: {self.fuel} \nMileage: {self.mileage} \nTax: {self.tax} \n\n")
        return self

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "Not Full", "105mpg")
car3 = Car(20000, "135mph", "Kind of Full", "5mpg")
car4 = Car(400000, "150mph", "Overflowing", "150mpg")
car5 = Car(2000, "45mph", "Empty", "25mpg")
car6 = Car(20000000, "35mph", "Meh", "15mpg")