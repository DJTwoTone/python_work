#print numbers from 1 - 20
for number in range(1,21):
	print(number)

#make a list of numbers from 1 to a million
a_lot = []
for value in range(1,1000001):
	a_lot.append(value)
print(a_lot)

#simple stats for the list
small_boat = min(a_lot)
print(small_boat)
large_boat = max(a_lot)
print(large_boat)
big_one = sum(a_lot)
print(big_one)

#list of odds 1-10
odd_list = []
for value in range(1,11,2):
	odd_list.append(value)
print(odd_list)

#list of multiples of three 3-30
threes_list = []
for value in range(3,31,3):
	threes_list.append(value)
print(threes_list)

#print and print list of cubes 1-10
for value in range(1,11):
	print(value**3)

cubes = [value**3 for value in range(1,11)]
print(cubes)
