import unittest

import movie_rating

from datetime import datetime

class TestMovieRatingFunction(unittest.TestCase):

	def test_that_movie_rating_can_add_movie(self):

		actual = movie_rating.add_movie({"movie": "merlin"})

		expected = {"movie": "merlin" }

		self.assertEqual(actual, expected)

