from collections import OrderedDict

# ~ favorite_languages = OrderedDict()

# ~ favorite_languages['jen'] = 'python'
# ~ favorite_languages['sarah'] = 'c'
# ~ favorite_languages['edward'] = 'ruby'
# ~ favorite_languages['phil'] = 'python'

# ~ for name, language in favorite_languages.items():
	# ~ print(name.title() + "'s favorite language is " + language.title() +".") 

# ~ my_glossary = OrderedDict()

# ~ my_glossary['dictionary'] = 'a grouping of key-value pairs'
# ~ my_glossary['loop'] = 'a statement that will run multiple times'
# ~ my_glossary['list'] = 'a grouping of values'
# ~ my_glossary['variable'] = 'a nickname of something else'
# ~ my_glossary['tuple'] = 'like a list but you cannot change it'
# ~ my_glossary['key'] = 'the first part of a key-value pair'
# ~ my_glossary['value'] = 'the second part of a key-value pair'
# ~ my_glossary['sorted'] = 'wrap this around a list or dictionary you want alphabetized'
# ~ my_glossary['.title'] = 'append this to something you want capitalized'
# ~ my_glossary['.items()'] = 'append this to access everything in a dictionary (keys then values)'
# ~ my_glossary['.keys()'] = 'append this to access the keys in a dictionary'
# ~ my_glossary['.values()'] = 'append this to access the values in a dictionary'



# ~ print("\nMy Glossary\n")

# ~ for entry, define in my_glossary.items():
	# ~ print(entry + ":\n\t" + define)

from random import randint

class Die():
	
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1, self.sides)
		print(x)
		
	def ten_rolls(self):
		count = 0
		while (count < 10):
			count += 1
			self.roll_die()

roll = Die(100)

roll.ten_rolls()

