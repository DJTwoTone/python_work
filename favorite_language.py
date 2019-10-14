favorite_language = {
	'jen': ['python', 'ruby'],
	'sarah': 'c',
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskel']
}

#names = ['jamie', 'jen', 'sam', 'sarah', 'elizabeth', 'edward', 'phyllis', 'phil']

#for name in names:
#	if name in favorite_language.keys():
#		print("Thank you, " + name.title() + " for taking our poll.")
#	else:
#		print("Please, " + name.title() + ". When you have a free moment, take our poll.")	

for name, languages in favorite_language.items():
	print("\n" + name.title() + "'s favorite language(s) are:")
	for language in languages:
		print("\t" + language.title())
