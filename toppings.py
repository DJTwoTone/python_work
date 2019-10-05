requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")
	
requested_toppings = ['mushrooms', 'onions', 'pineapple']

order = 'mushrooms'
if order in requested_toppings:
	print("You got it!")
else:
	print("No can do!")

available_toppings = [
		'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
		'extra cheese']

requested_toppings = [
		'mushrooms', 'french fries', 'extra cheese']
		
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
		
print("Making your pizza...")
