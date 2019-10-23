# ~ def make_shirt(size='large', message='I love Python'):
	# ~ print("You ordered a " + size + "-sized T-shirt with the message: \""
	 # ~ + message + ".\"")
	 
# ~ make_shirt('large', 'Kiss my ass')
# ~ make_shirt(message='Blow me', size='small')
# ~ make_shirt()
# ~ make_shirt('medium',)
# ~ make_shirt('small', 'Whaddup?')


# ~ def describe_city(name, country='america'):
	# ~ print(name.title() + " is a city in " + country.title() + ".")
	
# ~ describe_city('boston',)
# ~ describe_city('new york',)
# ~ describe_city('seoul', 'south korea')

# ~ def city_country(city, country):
	# ~ return("______________________________________________________________" + 
	# ~ '\n"' + city.title() + ', ' + country.title() + '"' + 
	# ~ "\n______________________________________________________________")
	
# ~ pair = city_country('mexico city', 'mexico')
# ~ print(pair)

# ~ pair = city_country('beruit', 'lebannon')
# ~ print(pair)

# ~ pair = city_country('panama city', 'panama')
# ~ print(pair)

def make_album(artist_name, album_title, track_number=''):
	if track_number:
		album = {'artist': artist_name, 'album': album_title, 'tracks': track_number}
		return(album)
	else:
		album = {'artist': artist_name, 'album': album_title}
		return(album)
	
# ~ album = make_album('micheal jackson','bad')
# ~ print(album)

# ~ album = make_album('sting','an englishman in new york', 7)
# ~ print(album)

# ~ album = make_album('snoop dogg','the dogg pound')
# ~ print(album)

# ~ album = make_album('weezer', 'pinkerton', 9)
# ~ print(album)

# ~ while True:
	# ~ print("Let's catalog some albums!")
	# ~ print("(enter 'q' any time to quit)")
	
	# ~ artist = input("Who is the artist? ")
	# ~ if artist == 'q':
		# ~ break
	
	# ~ title = input("What album is it? ")
	# ~ if title == 'q':
		# ~ break
		
	# ~ tracks = input("How many tracks are there?\mHit 'enter' if you don't know. ")
	# ~ if tracks == 'q':
		# ~ break
		
	# ~ album = make_album(artist, title, tracks)
	# ~ print(album)

# ~ def build_profile(first, last, **user_info):
	# ~ profile = {}
	# ~ profile['first_name'] = first
	# ~ profile['last_name'] = last
	# ~ for key, value in user_info.items():
		# ~ profile[key] = value
	# ~ return profile
	
# ~ user_profile = build_profile('benjamin', 'slater', middle_name='william', spouse='jung miyeong', location='ulsan')

# ~ print(user_profile)

def car_maker(make, model, **options):
	car_info = {}
	car_info['maunfacturer'] = make
	car_info['model'] = model
	for key, value in options.items():
		car_info[key] = value
	return car_info
	
car = car_maker('ford', 'fairlaine', color='maroon', convertable=True, mileage=345298)

print(car)
