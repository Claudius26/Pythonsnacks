def get_numbers_greater_or_equal_75(numbers : list) -> list:

	for number in numbers:

		if type(number) == str:

			return "Invalid inputs"

	return [number for number in numbers if 75 <= number < 100]

	



	 

	