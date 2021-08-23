# exception == event detected during execution that interrupts the flow of a program

try:
    numerator = int(input('Enter number to be divided: '))
    denominator = int(input('Enter number to divide by: '))
    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print('You cannot divide by zero')
except ValueError as e:
    print(e)
    print('Numbers only please!')
except Exception as e:  # general, displays msg for any exception
    print(e)
    print('Something went wrong')
else:  # do something else if not exception, if there's exception handle it
    print(result)
finally: # block executes whether or not there is an exception
    print('Hooraay!!')