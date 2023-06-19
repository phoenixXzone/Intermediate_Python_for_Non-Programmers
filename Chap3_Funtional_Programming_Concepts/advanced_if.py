age = 0
height = 121

# and
if age >= 8 and height >= 135:
    print("You can ride the ride!")

# or
if age >= 17 or height >= 160:
    print("You can ride the superride!")

# elif (else if)
if height < 120: 
    print("You cannot ride any rides :( ")
elif height < 135:
    print("You can ride the level 1 rides!")
elif height < 200:
    print("You can ride any rides!")
else:
    print("You are too tall to ride any of the rides :( ")

#create an if statement with both and & or 

if age % 2 == 0 and age > 100 or age == 0:
    print("You have an interesting age! ")

 