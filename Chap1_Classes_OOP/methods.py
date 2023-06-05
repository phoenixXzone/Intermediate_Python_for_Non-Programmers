import random
class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name
    
    def bark(self):
        print(f"Woof! My name is {self.name} and my lucky number is {self.lucky_number}")

dog1 = Dog("Fido")
dog2 = Dog("Sara")

dog1.bark()
dog2.bark()

#In your previous class, add a method
#that uses one of your instance variables 

print("\n")

class Furniture:
    chair = 3
    
    def __init__(self, wood):
        print("Furniture is available!")
        self.prod_number = random.randint(1,100)
        self.wood = wood
    
    def shipping(self):
        print(f"Please ship the {self.wood} wood with product number {self.prod_number} to the docks")

furn1 = Furniture("Rose")
furn2 = Furniture("Teek")

furn1.shipping()
furn2.shipping()


