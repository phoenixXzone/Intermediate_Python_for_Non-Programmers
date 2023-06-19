print("Before")

try:
    4 / 0
    #print(age)
#except NameError as e:
    print("This was a name issue")
    print(e)
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e: 
    print("oops, something went wrong")

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("Error101: The word has to have atleast one letter!")
    return word.upper()

#print(upper_fun(""))

print("After")


#Find something to break and put it in a try,except


try:
    '2' + 2
except TypeError as e: 
    print(e)

