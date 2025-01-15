number = int(input("Enter a number between 0-1000: "))

while number < 0 or number > 1000:

	print('Invalid number')

	number = int(input("Enter a number between 0-1000: "))

total = 0

while number > 0:

	digit_number = number % 10

	total += digit_number

	number //= 10

print(total)

