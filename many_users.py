users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
	}
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull Name: " + full_name.title() + "\n\tLocation: " + 
	location.title())
