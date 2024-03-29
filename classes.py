class Dog():
	def __init__(self, name, age):
		self.name=name
		self.age=age
	
	def intro(self):
		print("The dog's name is " + self.name.title() + ".")
		print(self.name.title() + " is " + str(self.age) + " years old.")
		
	def sit(self):
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		print(self.name.title() + " rolled over!")
		
# ~ my_dog = Dog('jack', 9)
# ~ your_dog = Dog('felix', 3)

# ~ my_dog.intro()
# ~ my_dog.sit()
# ~ my_dog.roll_over()

# ~ your_dog.intro()
# ~ your_dog.sit()
# ~ your_dog.roll_over()


class Car():
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles
			
			
# ~ my_new_car = Car('ford', 'explorer', 2019)
# ~ print(my_new_car.get_descriptive_name())
# ~ my_new_car.read_odometer()

# ~ my_new_car.update_odometer(23)
# ~ my_new_car.read_odometer()

# ~ my_new_car.update_odometer(22)
# ~ my_new_car.read_odometer

# ~ my_new_car.increment_odometer(1265)
# ~ my_new_car.read_odometer()


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank():
		print("This car doesn't need a gas tank!")
		
class Battery():
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kwh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
		
			
		
		
# ~ my_tesla = ElectricCar('tesla', 'model s', 2016)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()
# ~ my_tesla.battery.upgrade_battery()
# ~ my_tesla.battery.get_range()
