# str.format() == optional method that gives users more control when displaying
#                   output

animal = 'cat'
item = 'table'

#print('The {} jumped on the {}'.format(animal,item)) # empty braces displays in order
#print('The {} jumped on the {}'.format('cat','table')) # without defined variables
#print('The {1} jumped on the {0}'.format(animal,item)) # index to specify order;positional argument
#print('The {animal} jumped on the {item}'.format(animal='dog',item='bed')) # keyword aguments
 # can reuse ondex or keyword

text = 'The {} jumped on the {}'
print(text.format(animal,item)) # used to format string variables

# display with padding

name = 'Shirley'
age = 'Twenty Five'

print('My name is {:12}'.format(name)) # add amount of space(counts frm beginning)
print('My name is {:>12}'.format(name)) # right aligns it by 12 characters from last character
print('My name is {:<2}'.format(name)) # left aligns it
print('My name is {:^12}'.format(name)) # center aligns it
print('My name is {0:10}'.format(name,age)) # use with positional arguments
print('My name is {age:10}'.format(name='Siz',age='nine')) # with keyword arguments

# format numbers

number = 3.14159

print('The number pi is {:.2f}'.format(number)) # displays 2 decimal point w/ round off

time = 1000000

print('Time is {:,}'.format(time))  # adds comma at every thousand
print('Time is {:o}'.format(time))  # dispalys as octal number
print('Time is {:b}'.format(time))  # displays as binary number
print('Time is {:x}'.format(time))  # displays as hexadecimal w/ small letters
print('Time is {:X}'.format(time))  # displays as hexadecimal w/ capital letter
print('Time is {:E}'.format(time))  # in scientific notation, e for lower case
