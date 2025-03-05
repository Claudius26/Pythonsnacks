list_of_movies = {"names_of_movies": {}}

def add_movie(name):


	list_of_movies["names_of_movies"][name] = {"movie": name}

	return list_of_movies["names_of_movies"][name]