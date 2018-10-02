class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.mileage = 0

    def displayInfo(self):
        print(f"This bike costs ${self.price}, has a maximum speed of {self.max_speed}, and has {self.mileage} miles on it.")
        return self

    def ride(self):
        print("Riding!")
        self.mileage += 10
        return self
    
    def reverse(self):
        if self.mileage < 5:
            print("Can't reverse any further!")
            return self
        else:
            print("Reversing...")
            self.mileage -= 5
            return self


bike1 = Bike(200, "25mph")
bike2 = Bike(800, "40mph")
bike3 = Bike(50, "15mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()