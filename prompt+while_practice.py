

# ~ while True:
	# ~ toppings = []
	# ~ if toppings == False:
		# ~ prompt = "\nWhat topping would you like on your pizza?\t"
		# ~ toppings.append(input(prompt))
	# ~ else:
		# ~ print("You want a pizza with:"
		# ~ for to in toppings:
			# ~ print(to)
		# ~ prompt = "Would you like anything else on that?\t"
			# ~ if input(prompt) = 'no':
				# ~ break
			# ~ else:
				# ~ toppings.append(input(prompt))
				
# ~ prompt = "\nWhat topping would you like on your pizza?"
# ~ prompt += "\nEnter 'quit' when you are finished. "

# ~ while True:
	# ~ topping = input(prompt)
	# ~ if topping != 'quit':
		# ~ print(" Okay! That'll be a pizza with " + topping + ".")
	# ~ else:
		# ~ break
		
# ~ active = True 
# ~ while active:
	# ~ topping = input(prompt)
	
	# ~ if topping == 'quit':
		# ~ active = False
	# ~ else:
		# ~ print(" Okay! That'll be a pizza with " + topping + ".")

# ~ while True:
	# ~ topping = input(prompt)
	
	# ~ if topping == 'quit':
		# ~ break
	# ~ else:
		# ~ print(" Okay! That'll be a pizza with " + topping + ".")

# ~ prompt = "Welcome to our movie house!"
# ~ prompt += "\nLet us know how old you are so we can charge you the right price."
# ~ prompt += "\nHow old are you?"
# ~ prompt += "\nEnter 'done' when you are done:\t"

# ~ while True:
	# ~ age = input(prompt)
	# ~ if age == 'done':
		# ~ break
	# ~ age = int(age)
	
	# ~ if age < 3:
		# ~ print("You're a cute " + str(age) + "-year old. You get in for free")
	# ~ elif age < 13:
		# ~ print("You're only " + str(age) + "! You can get in for $10.")
	# ~ else:
		# ~ print("We'll give you the " + str(age) + "-year old price. It's just $15!")

while True:
	x = 1
	x += 1
	if x < 0:
		break
	else:
		print(x)
