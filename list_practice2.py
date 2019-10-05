drinks = ['apple juice', 'beer', 'coffee', 'daquiri', 'egg nog', 'fresca', 'grog']

print("The first three items in my list are:")
for drink in drinks[:3]:
	print(drink)

print("Three items from the middle of the list are:")
for drink in drinks[2:5]:
	print(drink)

print("The last three items in my list are:")
for drink in drinks[-3:]:
	print(drink)

pizzas = ['cheese', 'pepperoni', 'meat lovers\'']
friend_pizzas = pizzas[:]

pizzas.append('sausage')
friend_pizzas.append('white')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
	
print("My friend\'s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
