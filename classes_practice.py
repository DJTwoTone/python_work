class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
		
	def intro(self):
		print("Welcome to " + self.restaurant_name.title() + "; the greatest "
		 + self.cuisine_type.title() + " restaurant in the world!")
	
	def open(self):
		print(
			self.restaurant_name.title() 
			+ " is open for business. Come and try our " 
			+ self.cuisine_type.title() + " cuisine.")
			
	def set_number_served(self, customers):
		self.number_served = customers
		
	def increment_number_served(self, inandout):
		self.number_served += inandout

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		super().__init__(restaurant_name, cuisine_type, number_served)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']
		
	def our_flavors(self):
		print("We have the following flavors:\n")
		for flavor in self.flavors:
			print("- " + flavor)
	

# ~ chez_louis = Restaurant('chez louis', 'french')
# ~ south_of_the_border = Restaurant('south of the border', 'mexican')
# ~ morning_calm = Restaurant('morning calm', 'korean')
# ~ restaurant = Restaurant('test1', 'test2')
# ~ chocohaus = IceCreamStand('a', 'b')

# ~ chocohaus.our_flavors()


# ~ print(restaurant.number_served)
# ~ restaurant.set_number_served(34)
# ~ print(restaurant.number_served)
# ~ restaurant.increment_number_served(55)
# ~ print(restaurant.number_served)

# ~ chez_louis.intro()
# ~ chez_louis.open()

# ~ south_of_the_border.intro()
# ~ south_of_the_border.open()

# ~ morning_calm.intro()
# ~ morning_calm.open()

class User():
	
	def __init__(self, first_name, last_name, ident, hobby, login_attempts=0):
		self.first_name = first_name
		self.last_name = last_name
		self.ident = ident
		self.hobby = hobby
		self.login_attempts = login_attempts
	
	def describe_user(self):
		print(
			"This is " + self.first_name.title() + " " + self.last_name.title()
			 + ". You can call " + self.first_name.title() + " " 
			 + self.last_name.title() + " " +  self.ident.title() + ". " 
			 + self.ident.title() + "'s hobby is " + self.hobby + ".")
		
	def greet_user(self):
		print("Greetings and salutations, " + self.first_name.title() + " " + self.last_name.title() + ".")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	
	def __init__(self, first_name, last_name, ident, hobby, login_attempts=0):
		super().__init__(first_name, last_name, ident, hobby, login_attempts)
		self.privileges = Privileges()


class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = ['can add posts', 'can edit posts', 'can delete posts', 'can boot users']
		
		
	def show_privileges(self):
		message = "This user is an admin.\n" 
		message += "This user has the following privileges:\n"
		print(message)
		for privilege in self.privileges:
			print(privilege.title())
	
	
	
# ~ adam = User('adam', 'ant', 'ace', 'archery')
# ~ bob = User('robert', 'reeses', 'bob', 'boxing')
# ~ dave = User('david', 'down', 'dave', 'darts')
# ~ testy = Admin("a", "b", "c", "d")

# ~ testy.privileges.show_privileges()

# ~ print(testy.login_attempts)
# ~ testy.increment_login_attempts()
# ~ print(testy.login_attempts)
# ~ testy.increment_login_attempts()
# ~ testy.increment_login_attempts()
# ~ testy.increment_login_attempts()
# ~ testy.increment_login_attempts()
# ~ testy.increment_login_attempts()
# ~ print(testy.login_attempts)
# ~ testy.reset_login_attempts()
# ~ print(testy.login_attempts)

# ~ adam.describe_user()
# ~ adam.greet_user()

# ~ bob.describe_user()
# ~ bob.greet_user()

# ~ dave.describe_user()
# ~ dave.greet_user()
