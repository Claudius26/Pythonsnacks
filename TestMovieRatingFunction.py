import unittest

import movie_rating

from datetime import datetime

class TestMovieRatingFunction(unittest.TestCase):

	def test_that_movie_rating_can_add_movie(self):

		actual = movie_rating.add_movie("merlin")

		expected = {"movie": "merlin", "Date Added": actual["Date Added"], "rating": "no rating" }

		self.assertEqual(actual, expected)

	def test_that_movie_rating_can_add_correct_date_and_time(self):

		actual = movie_rating.add_movie("merlin")

		expected = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		self.assertEqual(actual["Date Added"], expected)

	def test_that_movie_rating_can_add_movie_returns_invalid_input_when_wrong_data_is_inputed(self):

		actual = movie_rating.add_movie(1)

		expected = "Invalid input"

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_returns_invalid_rating_if_rating_is_out_of_range(self):

		actual = movie_rating.is_rating_validated(5.1)

		expected = False

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_returns_invalid_False_if_wrong_input(self):

		actual = movie_rating.is_rating_validated("s")

		expected = False

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_returns_movie_does_not_exist_if_movie_name_not_found(self):

		actual = movie_rating.add_ratings("avatar", 4.5)

		expected = "Movie does not exist"

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_returns_rating(self):

		movie_name = "merlin"

		rating = 4.5

		movie_rating.add_movie(movie_name)

		actual = movie_rating.add_ratings("merlin", rating)

		expected =  rating

		self.assertEqual(actual, expected)
