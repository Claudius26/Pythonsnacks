import random

number1 = random.randrange(0, 100)

number2 = random.randrange(0, 100)

print(number1, number2)

def sum_two_random_numbers(first_number, second_number):

	add =  (first_number + second_number)

	return add

	
value = int(input("Enter the sum of both numbers displayed: "))

def check_for_correct_sum_of_random_numbers(value):

	return True if value == sum_two_random_numbers(number1, number2) else False

print(check_for_correct_sum_of_random_numbers(value))