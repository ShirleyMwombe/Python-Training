import random

x = random.randint(1,15)

print(x)  # prints random integer between 1 & 15

y = random.random() # generates random float numbers below 1
print(y)

mylist = ('nails','hair','scent')
z = random.choice(mylist)

print(z)

cards = [1,2,3,4,5,6,7,8,9,10,'J','A','K','Q'] # tuple

random.shuffle(cards) # shuffles the cards
print(cards)
