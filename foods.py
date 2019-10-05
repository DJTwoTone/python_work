#list of favorite foods
my_foods = ['pizza', 'falafel', 'carrot cake']
#copy the list
friend_foods = my_foods[:]

#add a food to prove it is a different list
my_foods.append('canoli')

#print out favorite foods list
print("My favorite foods are:")
#print(my_foods)
for food in my_foods:
	print(food)
#add a food to prove it is a different list
friend_foods.append('ice cream')

#print friends favorite food list
print("\nMy friend's favorite foods are:")
#print(friend_foods)
for food in friend_foods:
	print(food)

