def back_to_sender_logistics():

	base_pay = 5000;

	successful_deliveries = int(input("Enter successful deliveries: "))

	while successful_deliveries < 0:

		print("\nINVALID INPUT, PLEASE TRY AGAIN")

		successful_deliveries = int(input("Enter successful deliveries: "))

	rate = 0

	if successful_deliveries < 50:

		rate = 160

	elif successful_deliveries >= 50 and successful_deliveries <= 59:

		rate = 250

	elif successful_deliveries >= 60 and successful_deliveries <= 69:

		rate = 400

	elif successful_deliveries >= 70:

		rate = 500

	total_wage = (successful_deliveries * rate) + base_pay

	return total_wage

print("Wage for the day is:",back_to_sender_logistics())


		