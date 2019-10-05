cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
		
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')
print('\n')

car = 'bmw'
print("Is car == 'bmw'? I predict true.")
print(car == 'bmw')

print("\nIs car == 'toyota'? I predict false")
print(car == 'toyota')
print('\n')

