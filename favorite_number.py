import json

def get_stored_num():
	
	filename = 'favorite_number.json'
	try:
		with open(filename) as f_obj:
			favnum = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favnum
	
def get_num():
	
	favnum = input("What's your favorite number?  ")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(favnum, f_obj)
	return favnum



def fav_num():
	
	favnum = get_stored_num()
	if favnum:
		print("Are you sure your favorite number is still " + str(favnum) + ".")
	else:
		favnum = get_num()
		print(
				"I guess we can remember that you like the number " 
				+ str(favnum) + "...") 

fav_num()
