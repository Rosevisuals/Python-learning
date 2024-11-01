'''movie = input('Enter your favourite movie: ')
while( movie == ''):
      print('Please enter your favourite movie')
      movie = input('Enter your favourite movie: ')
print(f'😱😱😱 I did not know {movie} existed')'''

'''age = int(input('Enter your age: '))
while age < 0:
    print('Please enter a valid age')
    age = int(input('Enter your age: '))

print(f'You are {age} years old 😏')   ''' 


food = input('Enter your favourite food (q to quit): ')
while not food  == 'q':
    print(f'You like {food}')
    food = input('Enter your favourite food (q to quit)')
    print('bye')