usernames = ['admin', 'beastman', 'catlady', 'donutdude', 'eraserhead']

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Greetings Admin, Would you like to see what's up?")
		else:
			print("Hi " + username.title() + ", good to see you again!")
else:
	print("We need to find some users!")	
		 
current_users = ['facetime', 'ghost', 'hophead', 'imnotyourmom', 'juicer']

new_users = ['imnotyourmom', 'juicer', 'killerkyle', 'mechamike', 'noone']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("I'm sorry. That name is already taken.")
	elif new_user.lower() not in current_users:
		print("That name is available. Welcome, " + new_user + "!")
		
