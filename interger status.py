x = input('Enter first integer: ')
y = input('Enter second integer: ')
x = int(x)
y= int(y)
if(x >= 0 and y >= 0 ):
    print(f'{x} and {y} and positive number')
elif(x <= 0 and y <= 0):
    print(f'{x} and {y} are negative numbers')
elif(x >= 0 or y <= 0):
    print(f'{x} and {y} are non negative numbers')
else:
    print('Retry again')