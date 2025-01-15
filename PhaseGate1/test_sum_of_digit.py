import function_sum_of_digit

import unittest

class TestSumOfDigitFunction(unittest.TestCase):

	def test_that_unit_function_sum_of_digit_exist(self):

		function_sum_of_digit.get_sum_of_digit(986)

	def test_that_unit_function_sum_of_digit_adds_digit(self):

		actual = function_sum_of_digit.get_sum_of_digit(986)

		self.assertEqual(actual, 23)

	def test_that_unit_function_sum_of_digit_returns_invalid_result_when_negative_number_is_inputted(self):

		actual = function_sum_of_digit.get_sum_of_digit(-986)

		self.assertEqual(actual, 'Invalid input')

	def test_that_unit_function_sum_of_digit_returns_invalid_result_when_number_greater_than_onethousand_is_inputted(self):

		actual = function_sum_of_digit.get_sum_of_digit(1038)

		self.assertEqual(actual, 'Invalid input')

	def test_that_unit_function_sum_of_digit_returns_invalid_result_when_string_value_is_inputted(self):

		actual = function_sum_of_digit.get_sum_of_digit('b')

		self.assertEqual(actual, 'Invalid input')


