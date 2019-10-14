# ~ message = input("Tell me something an I will reoeat it backto you:")
# ~ print(message);

# ~ name = input("Please enter your name: ")
# ~ print("Hello " + name + "!")

# ~ prompt = "If you tell us who you are, we can personalize the message you see."
# ~ prompt += "\nWhat is your first name?"

# ~ name = input(prompt)
# ~ print("Hello, " + name + "!")

# ~ age = input("How old are you? ")
# ~ print(age)
# ~ age = int(age)
# ~ age <= 32

# ~ height = input("How tall are you in inches?  ")
# ~ height = int(height)

# ~ if height >= 36:
	# ~ print("\nYou're tall enough to ride this ride.")
# ~ else:
	# ~ print("\nYou'll be able to ride this ride when you are older.")

# ~ number = input("Enter a number, and I'll tell you if it's odd or even:  ")
# ~ number = int(number)

# ~ if number % 2 == 0:
	# ~ print("\nThe number " + str(number) + " is even!")
# ~ else:
	# ~ print("\nThe number " + str(number) + " is odd!")

# ~ rental_car = input("Which kind of rental car would you like? ")
# ~ print("Let me see if I can find you a(n) " + rental_car + ".")

# ~ dinner_party = input("How many people are in your party this evening? ")
# ~ dinner_party = int(dinner_party)

# ~ if dinner_party >= 8:
	# ~ print("You will need to wait just a few moments.")
# ~ else:
	# ~ print("We have a table available right now. Please come this way.")

num = input("Let me test my math skills. Tell me any number... Any number you can think of: ")
num = int(num)

if num % 10 == 0:
	print(str(num) + " is a multiple of 10")
elif num % 9 == 0:
	print(str(num) + " is a multiple of 9")
elif num % 8 == 0:
	print(str(num) + " is a multiple of 8")
elif num % 7 == 0:
	print(str(num) + " is a multiple of 7")
elif num % 6 == 0:
	print(str(num) + " is a multiple of 6")
elif num % 5 == 0:
	print(str(num) + " is a multiple of 5")
elif num % 4 == 0:
	print(str(num) + " is a multiple of 4")
elif num % 3 == 0:
	print(str(num) + " is a multiple of 3.")
elif num % 2 == 0:
	print(str(num) + " is a multiple of 2.")
else:
	print(str(num) + " is a prime number.")
