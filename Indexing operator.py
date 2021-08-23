# indexing operator - gives access to a sequence's element(str,tuples,lists)

name = 'Shirley Mwombe'

#if (name[0].isupper()):
 #   name = name.lower()
#print(name)

firstname = name[0:8].upper()
lastname = name[8:].lower()
lastcharacter = name[-2]

print(firstname)
print(lastname)
print(lastcharacter)