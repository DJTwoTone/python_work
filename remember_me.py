import json

def get_stored_username():
	
	filename = 'username.json'

	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)

	except FileNotFoundError:
		return None
		
	else:
		return username
		
		
def get_new_username():
	username = input("What's yo name?  ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	
	username = get_stored_username()
	
	
	if username:
		check_user()
		
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

def check_user():
	
	username = input("I don't recognize you face. What's yo name?   ")
	
	if username != get_stored_username():
		print("GET AWAY FOUL DEMON!")
	else:
		print("Welcome back, " + username + "!")
	
	
greet_user()
