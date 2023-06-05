import random
class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

dog1 = Dog("Fido")
dog2 = Dog("Sara")

print(dog1.name)
print(dog2.name)

#Whatever your previous class was
#Make an instance of that class and add an instance variable/attritube to it

print("\n")

class Furniture:
    chair = 3
    
    def __init__(self, wood):
        print("Furniture is available!")
        self.wood = wood

furn1 = Furniture("Rose")
furn2 = Furniture("Teek")
furn1.colour = "Brown"

print(furn1.wood)
print(furn2.wood)
print(furn1.colour)

