some_person = {
	'first_name': 'phil',
	'last_name': 'mckraken',
	'age': 99,
	'city': 'atlanta'
}

print("His name is " + some_person['first_name'].title() + " " + some_person[
'last_name'].title() + ".")
print("He is " + str(some_person['age']) + " years old.")
print("He lives in " + some_person['city'].title() + ".")


fav_nums = {
	'monica': 5,
	'erica': 4,
	'jessica': 3,
	'lisa': 2,
	'becca': 1
}

print("\nMonica's favorite number is " + str(fav_nums['monica']) + ".")
print("Erica's favorite number is " + str(fav_nums['erica']) + ".")
print("Jessica's favorite number is " + str(fav_nums['jessica']) + ".")
print("Lisa's favorite number is " + str(fav_nums['lisa']) + ".")
print("Becca's favorite number is " + str(fav_nums['becca']) + ".")

glossary = {
	'dictionary': 'a grouping of key-value pairs',
	'loop': 'a statement that will run multiple times',
	'list': 'a grouping of values',
	'variable': 'a nickname of something else',
	'tuple': 'like a list but you cannot change it'
}
print("\nMy Glossary\n")
#print("Dictionary:\n\t" + glossary['dictionary'])
#print("Loop:\n\t" + glossary['loop'])
#print("List:\n\t" + glossary['list'])
#print("Variable:\n\t" + glossary['variable'])
#print("Tuple:\n\t" + glossary['tuple'])
for entry, define in sorted(glossary.items()):
	print(entry + ":\n\t" + define)

glossary['key'] = 'the first part of a key-value pair'
glossary['value'] = 'the second part of a key-value pair'
glossary['sorted'] = 'wrap this around a list or dictionary you want alphabetized'
glossary['.title'] = 'append this to something you want capitalized'
glossary['.items()'] = 'append this to access everything in a dictionary (keys then values)'
glossary['.keys()'] = 'append this to access the keys in a dictionary'
glossary['.values()'] = 'append this to access the values in a dictionary'

print("\nMy Updated Glossary\n")
for entry, define in sorted(glossary.items()):
	print(entry + ":\n\t" + define + ".")

rolling = {
	'nile': "egypt",
	'mississippi': 'the u s a',
	'han': 'south korea',
	'mekong': 'vietnam',
	'amazon': 'brazil'
}

for river in rolling.keys():
	print("The " + river.title() + " is a river.")
	
for country in rolling.values():
	print(country.title() + " is a country.")
	
for river, country in rolling.items():
	print("The " + river.title() + " River is a river in the country, " + 
	country.title() + ".")
