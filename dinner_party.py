guests = ['abraham lincoln', 'ben franklin', 'clarence carter', 'dennis rodman']
invitation = "You are cordially invited to dine with me on July 4th, "

print("I've invited " + str(len(guests)) + " people to dinner.")
print(invitation + guests[0].title() + ".")
print(invitation + guests[1].title() + ".")
print(invitation + guests[2].title() + ".")
print(invitation + guests[3].title() + ".")

douchebag = guests.pop()

rejection = "\nI'm very sorry to hear you can't make it, " + douchebag.title() + ". Maybe next time."
print(rejection)

guests.append('elvis presley')

print("I've invited " + str(len(guests)) + " people to dinner.")
print(invitation + guests[0].title() + ".")
print(invitation + guests[1].title() + ".")
print(invitation + guests[2].title() + ".")
print(invitation + guests[3].title() + ".")

print("\n Good news! More room means more guests. The more the merrier!")

guests.insert(0, 'ford fairlain')
guests.insert(3, 'gorgeous george')
guests.append('harry houdini')

print("I've invited " + str(len(guests)) + " people to dinner.")
print("We have some extra space. " + invitation + guests[0].title() + ".")
print(invitation + guests[1].title() + ".")
print(invitation + guests[2].title() + ".")
print("We have some extra space. " + invitation + guests[3].title() + ".")
print(invitation + guests[4].title() + ".")
print(invitation + guests[5].title() + ".")
print("We have some extra space. " + invitation + guests[6].title() + ".")

print("\nThere was a fire! I only have 3 places left...")

rejected = guests.pop()
apology = "I'm sorry, " + rejected.title() + ". We'll have to do dinner another time."
print(apology)

rejected = guests.pop()
apology = "I'm sorry, " + rejected.title() + ". We'll have to do dinner another time."
print(apology)

rejected = guests.pop()
apology = "I'm sorry, " + rejected.title() + ". We'll have to do dinner another time."
print(apology)

rejected = guests.pop()
apology = "I'm sorry, " + rejected.title() + ". We'll have to do dinner another time."
print(apology)

rejected = guests.pop()
apology = "I'm sorry, " + rejected.title() + ". We'll have to do dinner another time."
print(apology)

print("I've invited " + str(len(guests)) + " people to dinner.")
secret = "Good news! I still have room for you. Come on over, "

print(secret + guests[0].title() + ".")
print(secret + guests[1].title() + ".")
