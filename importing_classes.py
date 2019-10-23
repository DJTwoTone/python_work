# ~ from classes import Car

# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())

# ~ my_new_car.odometer_reading = 23
# ~ my_new_car.read_odometer()


# ~ from classes import ElectricCar

# ~ my_tesla = ElectricCar('tesla', 'model s', 2016)

# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()


# ~ from classes import Car, ElectricCar

# ~ my_beetle = Car('volkswagen', 'beetle', 1964)
# ~ print(my_beetle.get_descriptive_name())

# ~ my_tesla = ElectricCar('tesla', 'roadster', 2018)
# ~ print(my_tesla.get_descriptive_name())

# ~ import classes

# ~ my_beetle = classes.Car('volkswagen', 'beetle', 1964)
# ~ print(my_beetle.get_descriptive_name())

# ~ my_tesla = classes.ElectricCar('tesla', 'roadster', 2018)
# ~ print(my_tesla.get_descriptive_name())

# ~ from classes_practice import Restaurant

# ~ steak_bar = Restaurant('steak bar', 'meat')
# ~ steak_bar.intro()

from classes_practice import User, Privileges, Admin

doug = Admin('douglas', 'dowd', 'double d', 'drinking')

doug.privileges.show_privileges()
