# if statements : execute if the condition is true

age = int(input('How old are you?: '))

if age == 100:
    print("You are a century old")
elif age in range(13, 17):
    print('You are a teenager')
elif age >= 18:
    print("You are an adult")
elif age <= 0:
    print('You are not born yet')
else:
    print('You are a child')
