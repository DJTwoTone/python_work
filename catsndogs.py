file_names = ['cats.txt', 'hotcakes.txt', 'dogs.txt', 'birds.txt']

for file in file_names:
	try:
		with open(file) as f_obj:
			lines = f_obj.readlines()
			for line in lines:
				print(line)
	except FileNotFoundError:
		# ~ msg = "Sorry. Can't find " + file + " ."
		# ~ print(msg)
		pass
