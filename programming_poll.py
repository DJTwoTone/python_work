filename = 'programming_poll_results.txt'

with open(filename, 'a') as file_object:
	
	prompt = "\nCould you tell use why you like programming?"
	prompt += "\nWrite 'no' if you don't want to answer.\t"
	
	active = True
	
	while active:
		response = input(prompt)
		
		if response == 'no':
			active = False
			
		else:
			file_object.write(response + '\n')
			print("Thank you for your respose.")
