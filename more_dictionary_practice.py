# ~ person_0 = {
	# ~ 'first_name': 'phil',
	# ~ 'last_name': 'mckraken',
	# ~ 'age': 99,
	# ~ 'city': 'atlanta'
# ~ }

# ~ person_1 = {
	# ~ 'first_name': 'ben',
	# ~ 'last_name': 'dover',
	# ~ 'age': 74,
	# ~ 'city': 'london'
# ~ }

# ~ person_2 = {
	# ~ 'first_name': 'shirley',
	# ~ 'last_name': 'notcalled',
	# ~ 'age': 46,
	# ~ 'city': 'new york city'
# ~ }

# ~ people = [person_0, person_1, person_2]

# ~ for person in people:
	# ~ print("His name is " + person['first_name'].title() + " " + person[
	# ~ 'last_name'].title() + ".")
	# ~ print("He is " + str(person['age']) + " years old.")
	# ~ print("He lives in " + person['city'].title() + ".\n")

# ~ tom = {
	# ~ 'name': 'tom',
	# ~ 'type': 'cat',
	# ~ 'owner': 'alice',
	# ~ 'fav_food': 'mice'
# ~ }

# ~ jerry = {
	# ~ 'name': 'jerry',
	# ~ 'type': 'mouse',
	# ~ 'owner': 'bruce',
	# ~ 'fav_food': 'cheese'
# ~ }

# ~ spike = {
	# ~ 'name': 'spike',
	# ~ 'type': 'dog',
	# ~ 'owner': 'charles',
	# ~ 'fav_food': 'meat'
# ~ }

# ~ doc = {
	# ~ 'name': 'doc',
	# ~ 'type': 'rabbit',
	# ~ 'owner': 'denise',
	# ~ 'fav_food': 'carrots'
# ~ }

# ~ hawk = {
	# ~ 'name': 'hawk',
	# ~ 'type': 'bird',
	# ~ 'owner': 'ellen',
	# ~ 'fav_food': 'seeds'
# ~ }

# ~ pets = [tom, jerry, spike, doc, hawk]

# ~ for pet in pets:
	# ~ print("I'd like to introduce " + pet['name'].title() + ". " + 
	# ~ pet['name'].title() + " is a " + pet['type'] + ". " + pet['name'].title()+ 
	# ~ " is owned by " + pet['owner'].title() + ". " + pet['name'].title() 
	# ~ + " really loves to eat " + pet['fav_food'] + ".") 

# ~ favorite_places = {
	# ~ 'huey': ['dunkin\' donuts', 'erehwon', 'france'],
	# ~ 'dewey': ['baker street', 'camelot'],
	# ~ 'louie': ['aladin\'s castle']
# ~ }

# ~ for name, places in favorite_places.items():
	# ~ print("This is " + name.title() + ". " + name.title() + " loves:")
	# ~ for place in places:
		# ~ print("\t" + place.title())


# ~ fav_nums = {
	# ~ 'monica': [5],
	# ~ 'erica': [4, 9],
	# ~ 'jessica': [3, 8, 12],
	# ~ 'lisa': [2, 7, 11, 14],
	# ~ 'becca': [1, 6 , 10, 13, 15]
# ~ }

# ~ print("\nMonica's favorite number(s) is/are " + str(fav_nums['monica']) + ".")
# ~ print("Erica's favorite number(s) is/are " + str(fav_nums['erica']) + ".")
# ~ print("Jessica's favorite number(s) is/are " + str(fav_nums['jessica']) + ".")
# ~ print("Lisa's favorite number(s) is/are " + str(fav_nums['lisa']) + ".")
# ~ print("Becca's favorite number(s) is/are " + str(fav_nums['becca']) + ".")

# ~ for name, nums in fav_nums.items():
	# ~ print(name.title() + "'s favorite number(s) is are:")
	# ~ for num in nums:
		# ~ print("\t" + str(num))

cities = {
	'washington d.c.': {
		'country': 'the united states of america',
		'population': 633427,
		'fact': "It used to be a swamp.",
	},
	
	'seoul': {
		'country': 'the republic of korea',
		'population': 9776000,
		'fact': "It is obsessed with modernity.",
	},
	
	'bangkok': {
		'country': 'the kingdom of thailand',
		'population': 8281000,
		'fact': "The king is a little off.",
	}
}

for city, info in cities.items():
	print("I'd like to introduce you to one of my favorite cities. I love to visit " 
	+ city.title() + ". " + city.title() + " is located in " + 
	info['country'].title() + ". It has a population of " + str(info['population']) 
	+ ". One interested thing someone told me about " + city.title() + "is: \n\t" 
	+ info['fact'] + "\n")
