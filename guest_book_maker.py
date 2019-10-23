
file_name = "guest_book.txt"

with open(file_name, 'a') as file_object:
	prompt = "\nCould you tells us your names for our guestbook?"
	prompt += "\nEnter 'done' when you have entered your entire party.\t"
	
	while True:
		name = input(prompt)
		
		if name == 'done':
			break
		else:
			file_object.write(name + '\n')
			print("Welcome to our hotel, " + name.title() + "!")
