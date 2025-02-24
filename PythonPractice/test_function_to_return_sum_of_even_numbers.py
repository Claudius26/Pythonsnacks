import function_to_sum_even_numbers

import unittest

class TestToReturnSumOfEvenFunction(unittest.TestCase):

	def test_that_function_to_return_sum_of_even_numbers_exist(self):

		function_to_sum_even_numbers.sum_even_numbers([2, 7, 5, 11, 7, 19, 2, 8, 10])

	def test_that_function_to_return_sum_of_even_numbers_returns_sum(self):

		actual = function_to_sum_even_numbers.sum_even_numbers([2, 7, 5, 11, 7, 19, 2, 8, 10])

		self.assertEqual(actual, 22)

	def test_that_function_to_return_sum_of_even_numbers_returns_invalid_inputs(self):

		actual = function_to_sum_even_numbers.sum_even_numbers("s ")

		self.assertEqual(actual, "Invalid input")

	def test_that_function_to_return_sum_of_even_numbers_returns_invalid_inputs_when_integer_is_entered(self):

		actual = function_to_sum_even_numbers.sum_even_numbers(8)

		self.assertEqual(actual, "Invalid input")

	def test_that_function_to_return_sum_of_even_numbers_returns_invalid_inputs_when_floatingnumber_is_entered(self):

		actual = function_to_sum_even_numbers.sum_even_numbers(8.6)

		self.assertEqual(actual, "Invalid input")

	def test_that_function_to_return_sum_of_even_numbers_returns_invalid_inputs_when_space_is_entered(self):

		actual = function_to_sum_even_numbers.sum_even_numbers(" ")

		self.assertEqual(actual, "Invalid input")

	def test_that_function_to_return_sum_of_even_numbers_returns_mismatch(self):

		actual = function_to_sum_even_numbers.sum_even_numbers([2, 7, 5, "g", 7, 19, 2, 8, 10])

		self.assertEqual(actual, "number mismatch")

	def test_that_function_to_return_sum_of_even_numbers_returns_mismatch_when_string_is_entered(self):

		actual = function_to_sum_even_numbers.sum_even_numbers(["name", "food", "baby"])

		self.assertEqual(actual, "number mismatch")

	def test_that_function_to_return_sum_of_even_numbers_returns_mismatch_when_float_is_entered(self):

		actual = function_to_sum_even_numbers.sum_even_numbers([8.8, 8.6, 7.6])

		self.assertEqual(actual, "number mismatch")





if __name__ == "__main__":
	unittest.main()


