from datetime import datetime

list_of_movies = {"names_of_movies": {}}

def add_movie(name):

	if type(name) != str:

		return "Invalid input"

	time_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	list_of_movies["names_of_movies"][name] = {"movie": name, "Date Added": time_added, "rating": "no rating"}

	return list_of_movies["names_of_movies"][name]

def view_rating():

	print(list_of_movies["names_of_movies"][name])

def add_ratings(name, rating):

	if name not in list_of_movies["names_of_movies"]:

		return "Movie does not exist"

	if is_rating_validated(rating):

		list_of_movies["names_of_movies"][name]["rating"] = rating
	
		for key in list_of_movies["names_of_movies"][name]:

			if key == "rating":

				return list_of_movies["names_of_movies"][name][key]
		
def is_rating_validated(rating):

	if type(rating) == str or rating < 1 or rating > 5:

		return False

	return True









