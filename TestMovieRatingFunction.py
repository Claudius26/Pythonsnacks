import unittest

import movie_rating

from datetime import datetime

class TestMovieRatingFunction(unittest.TestCase):

	def test_that_movie_rating_can_add_movie(self):

		actual = movie_rating.add_movie("merlin")

		expected = {"movie": "merlin", "Date Added": actual["Date Added"] }

		self.assertEqual(actual, expected)

	def test_that_movie_rating_can_add_correct_date_and_time(self):

		actual = movie_rating.add_movie("merlin")

		expected = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		self.assertEqual(actual["Date Added"], expected)

	def test_that_movie_rating_can_add_movie_returns_invalid_input_when_wrong_data_is_inputed(self):

		actual = movie_rating.add_movie(1)

		expected = "Invalid input"

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_movie(self):

		actual = movie_rating.add_ratings(2.0)

		expected = 2.0

		self.assertEqual(actual, expected)

	def test_that_function_can_rate_returns_invalid_rating_if_rating_is_out_of_range(self):

		actual = movie_rating.add_ratings(5.1)

		expected = "Invalid rating"

		self.assertEqual(actual, expected)