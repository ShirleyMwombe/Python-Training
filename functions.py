# function - block of code that is executed only when it's called
#  arguments - used to send a function some information (str,value etc)
#               requires matching no of parameters
# parameters -

def hello(name,first,pal):  # has parameters
    print('Hello!'+' '+name+' '+first)
    print('Hello '+pal)
    print('Have a great day!!')

#hello('Shirley')  # needs all positioal args to match parameters

# OR

#myname = 'Shirley'

#hello(myname)

hello('Shirley','Mwombe','Lyn')  # needs matching no of parameters