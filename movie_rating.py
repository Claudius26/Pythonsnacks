from datetime import datetime
list_of_movies = {"names_of_movies": {}}

def add_movie(name):

	if type(name) != str:

		return "Invalid input"

	time_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	list_of_movies["names_of_movies"][name] = {"movie": name, "Date Added": time_added}

	return list_of_movies["names_of_movies"][name]

def add_ratings(rating):

	if rating < 1 or rating > 5:

		return "Invalid rating"

	return rating