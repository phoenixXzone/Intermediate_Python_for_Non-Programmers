import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name):
        print("An Animal is created")
        self.name = name

class Dog(Animal):
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        super().__init__(name)
        print("A Dog is created")
        self.lucky_number = random.randint(1,10)
        self.fur = ""
    
    def bark(self):
        print(f"Woof! My name is {self.name} and my lucky number is {self.lucky_number}")

class Bulldog(Dog):
    def __init__(self, name):
        super().__init__(name)
        print("Bulldog is created!")

dog1 = Bulldog("Fido")

#From your previous class, 
#Add a parent or child class 
print("\n")

class House():
    print("A House is created")

class Furniture(House):
    chair = 3
    
    def __init__(self, wood):
        super().__init__()
        print("Furniture is available!")
        self.wood = wood

furn1 = Furniture("Rose")




