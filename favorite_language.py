favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

names = ['jamie', 'jen', 'sam', 'sarah', 'elizabeth', 'edward', 'phyllis', 'phil']

for name in names:
	if name in favorite_language.keys():
		print("Thank you, " + name.title() + " for taking our poll.")
	else:
		print("Please, " + name.title() + ". When you have a free moment, take our poll.")	
