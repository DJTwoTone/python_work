filename = 'guest.txt'


with open(filename, 'a') as file_object:
	guest = input("Please tell us your name for our records: ")
	file_object.write(guest + "\n")
