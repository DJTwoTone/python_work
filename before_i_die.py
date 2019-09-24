before_i_die = ['the transsiberian railway', 'the camino de santiago', 'the appalachian trail', 'the panamerican highway', 'the silk road']
print("The Original")
print(before_i_die)

print("\nSorted")
print(sorted(before_i_die))

print("\nThe Original")
print(before_i_die)

print("\nReverse Sorted")
print(sorted(before_i_die, reverse=True))

print("\nReversed")
before_i_die.reverse()
print(before_i_die)

print("\nThe Original")
before_i_die.reverse()
print(before_i_die)

print("\nA Hard Sort")
before_i_die.sort()
print(before_i_die)

print("\nA Hard Reverse")
before_i_die.sort(reverse=True)
print(before_i_die)
