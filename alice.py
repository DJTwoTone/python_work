filename = 'alice.txt'

try:
	with open(filename, encoding="utf-8") as f_obj:
		contents = f_obj.read()
		
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)

else:
	words = contents.split()
	num_words = len(words)
	print(num_words)
