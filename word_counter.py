tobecounted = 'moby_dick.txt'

prompt = "Pick a word to be counted in " + tobecounted + ":   "
word = input(prompt)
with open(tobecounted , encoding="utf-8") as counting:
	contents = counting.read()
	num = contents.lower().count(word)
	print("There are " + str(num) + " instances of the word '" + word + "' in " 
	+ tobecounted + ".") 
