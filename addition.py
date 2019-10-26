print("Tell me two numbers and I'll add them together for you")
print("Enter 'q' to quit")

while True:
	try:
		spam = input("\nYour first number:  ")
		if spam == 'q':
			break
			
		spam = int(spam)
		
		egg = input("\nYour second number:  ")
		if egg == 'q':
			break
		
		egg = int(egg)
	
	except ValueError:
		print("Looks like you didn't enter two numbers. Kindly, try again.")
	
	else:
		sum = spam + egg
		
		print(
			"The sum of " + str(spam) + " and " + str(egg) + " is " + str(sum) + ".") 
