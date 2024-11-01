food_list = []
price_list = []
total = 0

while True:
    food_item = input('Enter food to buy (q to quit):  🍒🍇🍎')
    if food_item.lower() == 'q':
        break
    else:
        price = int(input(f'Enter price of {food_item}:  shs.'))
        food_list.append(food_item) #adding the food the customer wants to buy to the list of foods
        price_list.append(price) #adding the price of the food the customer wants to buy to the list

print('🚀 Your cart 🚀 ')
for food_item in food_list:
  print(food_list, end='')

print()
for price in price_list:
   total += price


print(f'Your total is shs. {total} 💸')
