import function_multiplication

import unittest

class TestMultiplyFunction(unittest.TestCase):

	def test_that_unit_function_multiplication_exist(self):

		actual = function_multiplication.getMultiplication(7, 4)


	def test_that_unit_function_multiplication_can_multiply_two_numbers(self):

		actual = function_multiplication.getMultiplication(7, 4)

		self.assertEqual(actual, 28)

	
	def test_that_unit_function_multiplication_can_multiply_one_negative_number_and_one_positive_number(self):

		actual = function_multiplication.getMultiplication(-7, 4)

		self.assertEqual(actual, -28)

	

