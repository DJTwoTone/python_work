#working with dictionaries
alien_0 = {'color': 'green', 'points': 5}

#accessing info from dicitionary key-value pairs
#print(alien_0['color'])
#print(alien_0['points'])

#using info from a key value pair
#new_points = alien_0['points']
#print("You've just earned " + str(new_points) + " points!")

#adding to a key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
#print(alien_0)

#print("The alien is " + alien_0['color'] + ".")
#alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color'] + ".")

#We gonna move an alien!
alien_0['speed'] = 'medium'

print("Original x-position: " + str(alien_0['x_position']))

#Move the alien to the right
#determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#for the fast aliens
	x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New position: " + str(alien_0['x_position']))

#faster
alien_0['speed'] = 'fast'
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Newer position: " + str(alien_0['x_position']))

#removing a key-value pair

print(alien_0)
del alien_0['points']
print(alien_0)


