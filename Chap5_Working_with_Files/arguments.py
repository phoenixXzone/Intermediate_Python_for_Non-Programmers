import sys

#Make a script that multiples all the number arguments passed into it

total = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = float(argument)
        total *= number
    except Exception as e:
        print(e) 
        print("Only number can be provided please")
        sys.exit(1)

print(total)
