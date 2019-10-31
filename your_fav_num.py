import json

filename = 'favorite_number.json'

with open(filename) as f_obj:
	favnum = json.load(f_obj)
	print("Really? Is " + favnum + " still your favorite number?")
