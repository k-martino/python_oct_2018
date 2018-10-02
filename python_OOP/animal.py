class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self    
    def displayHealth(self):
        print(f'Health ({self.name}): {self.health}')
        return self

tony = Animal("cat", 130)
tony.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name = "dog", health = 150):
        super().__init__(name, health)
    def pet(self):
        self.health += 5
        return self

carmella = Dog()
carmella.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
    def __init__(self, name = "dragon", health = 170):
        super().__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon!")
        return self

spike = Dragon()
spike.fly().fly().displayHealth()

polly = Animal("parrot", 100)
polly.displayHealth()

try:
    polly.pet()
except AttributeError as err:
    print(f"{err}")

try:
    polly.fly()
except AttributeError as err:
    print(f"{err}")

try:
    carmella.fly()
except AttributeError as err:
    print(f"{err}")