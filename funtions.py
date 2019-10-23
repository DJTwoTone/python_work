# ~ def greet_user(username):
	# ~ print("Hello, " + username.title() + "!")
	
# ~ greet_user('frank')

# ~ def display_message():
	# ~ print("I'm learning about functions!")

# ~ display_message()

# ~ def favorite_book(title):
	# ~ print("One of my favorite books is " + title.title() + ".")
	
# ~ favorite_book('the price of freedom')

# ~ def describe_pet(animal_type='cat', pet_name='ninja nate'):
	# ~ print("\nI have a " + animal_type + ".")
	# ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
# ~ describe_pet('dog', 'harry')
# ~ describe_pet('horse', 'frankie poo')
# ~ describe_pet(pet_name='billie bob', animal_type='cougar')
# ~ describe_pet()


# ~ def get_formatted(first_name, last_name):
	# ~ full_name = first_name + " " + last_name
	# ~ return full_name.title()

# ~ musician = get_formatted('jimi', 'hendrix')
# ~ print(musician)

# ~ def get_formatted_name(first_name, last_name, middle_name=''):
	# ~ if middle_name:
		# ~ full_name = first_name + ' ' + middle_name + ' ' + last_name
	# ~ else:
		# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)

# ~ musician = get_formatted_name('john', 'hooker', 'lee')
# ~ print(musician)


# ~ def build_person(first_name, last_name, age=''):
	# ~ person = {'first': first_name, 'last': last_name}
	# ~ if age:
		# ~ person['age'] = age
	# ~ return person
	
# ~ musician = build_person('jimi', 'hendrix', 27)
# ~ print(musician)

# ~ def get_formatted_name(first_name, last_name):
	# ~ full_name = first_name + " " + last_name
	# ~ return full_name.title()

# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ print("(enter 'q' at any time to quit)")
	# ~ f_name = input("First name:")
	# ~ if f_name == 'q':
		# ~ break
	# ~ l_name = input("Last name:")
	# ~ if l_name == 'q':
		# ~ break
	
	# ~ formatted_name = get_formatted_name(f_name, l_name)
	# ~ print("\nHello, " +formatted_name + "!")
	
# ~ def greet_users(names):
	# ~ for name in names:
		# ~ msg = "Hello, " + name.title() + "!"
		# ~ print(msg)

# ~ usernames = ['hannah', 'ty', 'margot']
# ~ greet_users(usernames)


# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodechedron']
# ~ completed_models = []

# ~ while unprinted_designs:
	# ~ current_design = unprinted_designs.pop()
	# ~ print("Printing model: " + current_design)
	# ~ completed_models.append(current_design)
	
# ~ print("The following models have been printed:")
# ~ for completed_model in completed_models:
	# ~ print(completed_model)


# ~ def print_models(unprinted_designs, completed_models):
	# ~ while unprinted_designs:
		# ~ current_design = unprinted_designs.pop()
		# ~ print("Printing model: " + current_design)
		# ~ completed_models.append(current_design)
		
# ~ def show_completed_models(completed_models):
	# ~ print("The following models have been printed:")
	# ~ for completed_model in completed_models:
		# ~ print(completed_model)
		
# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodechedron']
# ~ completed_models = []

# ~ print_models(unprinted_designs, completed_models)
# ~ show_completed_models(completed_models)

# ~ def make_pizza(size, *toppings):
	# ~ print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("- " + topping)
	
	
# ~ make_pizza(12, 'pepperoni')
# ~ make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', 
location='princeton', field='physics')

print(user_profile)
