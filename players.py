#a list of players
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
#print the first to third players
print(players[0:3])
#print the second to fourth players
print(players[1:4])
#print the beginning to fourth players
print(players[:4])
#print the third to last players
print(players[2:])
#print the third to last to last players
print(players[-3:])

#a loop of players
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
	
