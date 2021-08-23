# nested loops : the inner loop will finish all its iterations
#        before finishing one iteration of the outer loop

rows = int(input('What is the no of rows?: '))
columns = int(input('What is the no of columns?: '))
symbol = input('What is the symbol to use?: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()

