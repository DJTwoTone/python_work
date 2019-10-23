# ~ unconfirmed_users = ['alice', 'brian', 'candice']

# ~ confirmed_users = []

# ~ while unconfirmed_users:
	# ~ current_user = unconfirmed_users.pop()
	
	# ~ print("Verifying user: " + current_user.title())
	# ~ confirmed_users.append(current_user)

# ~ print("\nThe following users have been confirmed:")
# ~ for confirmed_user in confirmed_users:
	# ~ print(confirmed_user.title())

# ~ pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ~ print(pets)

# ~ while 'cat' in pets:
	# ~ pets.remove('cat')
	
# ~ print(pets)

# ~ responces = {}

# ~ polling_active = True

# ~ while polling_active:
	# ~ name = input("\nWhat is your name? ")
	# ~ responce = input("\nWhat mountain would you like to climb someday? ")
	
	# ~ responces[name] = responce
	
	# ~ repeat = input("Would you like to let another person respond? (yes/no) ")
	# ~ if repeat == 'no':
		# ~ polling_active = False

# ~ print("\n--- Polling Results ---")
# ~ for name, responce in responces.items():
	# ~ print(name.title() + " would like to climb " + responce.title())
	
# ~ print(responces)
