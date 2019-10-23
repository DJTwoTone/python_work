filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming\n")
	file_object.write("I love creating new games\n")

#Don't forget: If you want new lines you need to make them. Using write will overwrite any file.
