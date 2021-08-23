# kwargs == paraemter that will pack all arguments into a dictionary
#           Useful so that a function can accept a varying amt of keyword arguments

def hello(**kwargs):
    #print('Hello '+kwargs['first']+' '+kwargs['last'])
    print('Hello ',end=' ')
    for key,value in kwargs.items(): # iterates through each value in the arguments
        print(value,end=' ')  # iterates through each value in the arguments

hello(last='Mwombe',first='Shirley',middle='Makonjio')


