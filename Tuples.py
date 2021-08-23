# tuples : ordered and unchangeable, used to group related data

student=('Mike','male','22')

#print(student.index('22'))
#print(student.count('Mike'))

for x in student:
    print(x) #outputs all elements in a list form
if 'Mike' in student:
    print('Mike is available') # prints if Mike is tuple