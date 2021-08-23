# Dictionaries : changeable unordered collection of unique key-value
#                   pairs. Allow to quickly access a value

capitals = {'Kenya':'Nairobi',
            'South Africa':'Joburg',
            'Nigeria':'Abuja',
            'Ghana':'Accra'}

#print(capitals['Ghana'])  # Use key to output value
#for x in capitals:
 #   print(x)   # keys

#print(capitals.get('Egypt'))  # Check if key is in dictionary
#print(capitals.keys())  # all keys
#print(capitals.values())  # all values
#print(capitals.items())  # all key-pairs

capitals.update({'Zambia':'Maputo'})
capitals.update({'Kenya':'Mombasa'})
capitals.pop('Ghana')   # removes the pair, only use key

for key,value in capitals.items():
    print(key,value)  # lists key-value pairs
