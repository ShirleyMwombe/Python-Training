# Slicing - creating substring by extracting elements from other strings
# 		indexing[] or slice()
# 		[start:stop:step] slice uses ,

name = "Shirley Mwombe"
# first_name = name[0]
first_name = name[0:8]
short_name = name[0:8:3]  # step
reversed_name = name[::-1]  # outputs in reverse

print(first_name)
print(short_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
