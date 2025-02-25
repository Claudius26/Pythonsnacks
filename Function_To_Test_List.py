import unittest

import to_do_list

class Function_To_Test_List(unittest.TestCase):

	def test_that_menu_choice_exist(self):

		to_do_list.enter_choice(1)

	def test_that_menu_choice_returns_invalid_input_when_number_less_than_one_is_inputted(self):

		result = to_do_list.enter_choice(0)

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_menu_choice_returns_invalid_input_when_number_greater_than_five_is_inputted(self):

		result = to_do_list.enter_choice(6)

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_menu_choice_returns_invalid_input_when_float_is_inputted(self):

		result = to_do_list.enter_choice(6.1)

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_menu_choice_returns_invalid_input_when_string_is_inputted(self):

		result = to_do_list.enter_choice("funny")

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_menu_choice_returns_invalid_input_when_space_character_is_inputted(self):

		result = to_do_list.enter_choice(" ")

		expected = "invalid input"

		self.assertEqual(result, expected)

class Function_To_Verify_First_Choice(unittest.TestCase):

	def test_that_add_task_exist(self):

		to_do_list.add_task("Read Book")

	def test_that_add_task_returns_invalid_inputs_when_space_character_is_inputted(self):

		result = to_do_list.add_task(" ")

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_add_task_returns_invalid_inputs_when_number_is_inputted(self):

		result = to_do_list.add_task(7)

		expected = "invalid input"

		self.assertEqual(result, expected)

	def test_that_add_task_returns_invalid_inputs_when_float_is_inputted(self):

		result = to_do_list.add_task(7.0)

		expected = "invalid input"

		self.assertEqual(result, expected)



	
