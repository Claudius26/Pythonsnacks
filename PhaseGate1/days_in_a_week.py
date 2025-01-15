days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

first_day = int(input("Enter todays day: "))

while first_day < 0 or first_day > (len(days_of_the_week) - 1):

	print('Invalid input')

	first_day = int(input("Enter todays day: "))

future_day = int(input("Enter the number of days elapsed since today: "))

while future_day < 0 or future_day > (len(days_of_the_week) - 1):

	print('Invalid input')

	future_day = int(input("Enter the number of days elapsed since today: "))

sum_future_days = first_day + future_day

if sum_future_days > len(days_of_the_week):

	difference = sum_future_days % 7

	sum_future_days = difference	

print('Today is ', days_of_the_week[first_day], 'and the future day is ', days_of_the_week[sum_future_days])


