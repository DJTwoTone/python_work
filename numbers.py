#loop 1-4
for value in range(1,5):
	print(value)

#loop 1-5
for value in range(1,6):
	print(value)

#make a list of 1-5
numbers = list(range(1,6))
print(numbers)

#make a list of even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#make a list of squares of number2 1-10
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)

#squares list again, more concisely
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#one more time; even shorter
squares = [value**2 for value in range(1,11)]
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
dmin = min(digits)
print(dmin)
dmax = max(digits)
print(dmax)
dsum = sum(digits)
print(dsum)
