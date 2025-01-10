principal = float(input("Enter initial investment: "))

while principal < 0:

	print("\nINVALID INPUT")

	principal = float(input("Enter initial investment: "))

monthly_contribution = float(input("Enter amount to be added monthly: "))

while monthly_contribution < 0:

	print("\nINVALID INPUT")

	monthly_contribution = float(input("Enter amount to be added monthly: "))

years = int(input("Enter number of years for investment return: "))

while years <= 0:

	print("\nINVALID INPUT")

	years = int(input("Enter number of years for investment return: "))

rate = float(input("Enter interest rate: ")) / 100

while rate < 0:

	print("\nINVALID INPUT")

	rate = float(input("Enter interest rate: ")) / 100

variance_range = int(input("Enter varaince range: ")) / 100

while variance_range < 0:

	print("\nVariance range cant be less than 0")

	varaince_range = int(input("Enter varaince range: "))

compound_frequency = input("Enter compounding frequency: ").lower()

while compound_frequency != "daily" and compound_frequency != "weekly" and compound_frequency != "monthly" and compound_frequency != "quarterly" and compound_frequency != "semianually" and compound_frequency != "annually":

	print("\nINVALID INPUT")

	compound_frequency = input("Enter compounding frequency: ")

amount = principal

match(compound_frequency):
	
	case "daily":

		daily_rate = rate / 365
	
		for _ in range (years * 365):

			amount += amount * daily_rate

			if _ % 30 == 0:

				amount += monthly_contribution

		

		print(f'{amount:.2f}')

	case "weekly":

		weekly_rate = rate / 52
	
		for _ in range (years * 52):

			amount += amount * weekly_rate

			if _ % 4 == 0:

				amount += monthly_contribution

		

		print(f'{amount:.2f}')

	case "monthly":

		monthly_rate = rate / 12
	
		for _ in range (years * 12):

			amount += amount * monthly_rate

			amount += monthly_contribution

		

		print(f'{amount:.2f}')

	case "quarterly":

		quarterly_rate = rate / 4
	
		for _ in range (years * 4):

			amount += amount * quarterly_rate

			amount += monthly_contribution * 3

		print(f'{amount:.2f}')

	case "semiannuallyly":

		semiannually_rate = rate / 2
	
		for _ in range (years * 2):

			amount += amount * semiannually_rate

			amount += monthly_contribution * 6

		print(f'{amount:.2f}')


	case "annually":

	
		for _ in range (years):

			amount += amount * rate

			amount += monthly_contribution * 12

		print(f'{amount:.2f}')



	




				







	


	
