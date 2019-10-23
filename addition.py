print("Tell me two numbers and I'll add them together for you")
print("Enter 'q' to quit")

while True:
	first_number = input("Your first number:  ")
	if first_number == 'q':
		break
	second_number = input("Your second number:  ")
	if second_number == 'q':
		break
		
	try:
		sum = int(first_number) + int(second_number)
	except ValueError:
		print("Looks like you didn't enter two numbers. Kindly, try again.")
	else:
		print(
			"The sum of " + str(first_number) + " and " + str(second_number) 
			+ " is " + str(sum) + ".") 
