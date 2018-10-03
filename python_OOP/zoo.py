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

class Dog(Animal):
    def __init__(self, name, health = 150):
        super().__init__(name, health)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super().__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon!")
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name):
        self.animals.append( Dog(name) )
        return self
    def addDragon(self, name):
        self.animals.append( Dragon(name) )
        return self
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.displayHealth()
        return self

zoo1 = Zoo("pikapew's peek-a-zoo")
zoo1.addDog("Mella")
zoo1.addDog("Doggy")
zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()