# Logical Operators

temp = int(input('What is the temperature today?: '))

if temp >= 18 and temp <= 30:
    print("The weather is great today")
    print('Go outside')
elif not (temp > 0):
    print('The weather is not so bad today')
    print('You can go outside')
elif temp < 18 or temp > 30:
    print('The weather is not good today')
    print('Stay inside!')



