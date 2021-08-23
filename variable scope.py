# scope == region in which a variable is recognized.
#           only recognized in the region in which it is created
#           Local & global

name = 'Shirley'  # Globally defined, available inside and outside
                    # functions

def show_name():
    name = "Mwombe" #  locally defined
    print(name)

show_name()
print(name)  # global