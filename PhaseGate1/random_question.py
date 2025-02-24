import random

passes = 0

fail = 0

score = 0

number1 = random.randrange(0, 10)

number2 = random.randrange(0, 10)

result = number1 - number2

for number in range (1, 11):

	print(number1, '-', number2)

	answer = int(input('Enter the result from the question: '))

	if answer == result:

		print('correct')

		passes += 1

		score += 1

	else:

		print('incorrect')

		fail += 1


print('You passed', passes, 'times', 'and you failed', fail, 'times')

print('You scored ', score, '/', 10)








