# *args == parameter that will pack all arguments into a tuple
#           useful so that the function can accept varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5))

# changing one of the values in the tuple after packing the arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)  # cast tuple as list; tuples are unchangeable
    stuff[0] = 2  # modify the value, lists are changeable
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5))