import function_return_numbers_greater_or_equal_75

import unittest

class TestToReturnNumbesGreaterThanOrEqualTo75Function(unittest.TestCase):

	def test_that_function_to_return_numbers_greater_or_equal_75_exist(self):

		function_return_numbers_greater_or_equal_75.get_numbers_greater_or_equal_75([2, 7, 5, 11, 7, 19, 2, 8, 10])


	def test_that_function_to_return_numbers_greater_or_equal_75_and_less_than_100_returns_numbers(self):

		numbers = [27, 75, 55, 11, 7, 90, 98, 8, 100,99, 358]

		result = function_return_numbers_greater_or_equal_75.get_numbers_greater_or_equal_75(numbers)

		expected = [75, 90, 98, 99]

		self.assertEqual(result, expected)

	def test_that_function_to_return_numbers_greater_or_equal_75_and_less_than_100_returns_invalid_inputs(self):

		numbers = [27, "s", 55, 11, 7, 90, 98, 8, 100,99, 358]

		result = function_return_numbers_greater_or_equal_75.get_numbers_greater_or_equal_75(numbers)

		expected = "Invalid inputs"

		self.assertEqual(result, expected)

	def test_that_function_to_return_numbers_greater_or_equal_75_and_less_than_100_returns_results_when_float_input(self):

		numbers = [27, 75, 85.9, 55, 11, 7, 90, 98, 8, 100,99, 358]

		result = function_return_numbers_greater_or_equal_75.get_numbers_greater_or_equal_75(numbers)

		expected = [75, 85.9, 90, 98, 99]

		self.assertEqual(result, expected)

	def test_that_function_to_return_numbers_greater_or_equal_75_and_less_than_100_returns_invalid_inputs_when_string_inputs(self):

		numbers = ["Baking", "love"]

		result = function_return_numbers_greater_or_equal_75.get_numbers_greater_or_equal_75(numbers)

		expected = "Invalid inputs"

		self.assertEqual(result, expected)





