first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

max_number = first_number

second_max = first_number

lowest = first_number

if second_number > max_number:

	max_number = second_number

elif third_number > max_number:

	max_number = third_number

if second_number > second_max and second_number < max_number:

	second_max = second_number

elif third_number > second_max and third_number < max_number:

	second_max = third_number

if second_number < lowest:

	lowest = second_number

elif third_number < lowest:

	lowest = third_number 

print(lowest, second_max, max_number)