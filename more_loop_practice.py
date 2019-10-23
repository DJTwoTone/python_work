sandwich_orders = ['bacon sandwich', 'pastrami', 'baloney sandwich', 'beef on wick', 
'BLT', 'pastrami', 'seafood salad sandwich', 'cuban sandwich', 'pastrami', 'croque-monsieur' 'french dip']

finished_sanwiches = []

print("We're sorry, we're all out of pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	making = sandwich_orders.pop()
	
	print("We're making a " + making + ".")
	finished_sanwiches.append(making)

print("\nWe've made the following sandwiches:")
for sandy in finished_sanwiches:
	print("a " + sandy)
