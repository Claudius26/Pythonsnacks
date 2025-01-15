def get_sum_of_digit(number):

	if type(number) == str or number < 0 or number > 1000:

		answer = 'Invalid input'

		return answer

	total = 0

	while number > 0:

		digit = number % 10

		total += digit

		number //= 10

	return total