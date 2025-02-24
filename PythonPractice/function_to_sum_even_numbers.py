def sum_even_numbers(numbers: list) -> int:

	total = 0

	if type(numbers) == str or type(numbers) == int or type(numbers) == float:
		
		return "Invalid input"

	for count in numbers:

		if type(count) == str or type(count) == float:

			return "number mismatch"

		if count % 2 == 0:

			total += count


	return total