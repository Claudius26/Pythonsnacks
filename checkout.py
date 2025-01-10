import datetime

customersname = input("Enter customer's name: ")

response = input("Add more items? (yes/no): ")

items = []
price = []
quantity = []
total = []

current = datetime.datetime.now()

totalpriceofallitems = 0

while response != "yes" and response != "no":
	print("Please enter yes or no")
	response = input("Add more items?")

while response == "yes" and response != "no":

	item = input("What did the user buy? ")

	items.append(item)

	priceofitem = int(input(f"Price of {item}: "))

	while priceofitem <= 0:

		print("price of item must be greater than 0")

		priceofitem = int(input(f"Price of {item}: "))

	price.append(priceofitem)

	quantityofitem = int(input("How many items was bought: "))

	while quantityofitem <= 0:

		print("quantity must be more than 0: ")

		quantityofitem = int(input("How many items was bought: "))

	quantity.append(quantityofitem)

	def calculate_total(priceofitem, quantityofitem):

		return priceofitem * quantityofitem

	total.append(calculate_total(priceofitem, quantityofitem))

	totalpriceofallitems += calculate_total(priceofitem, quantityofitem)

	response = input("Add more items: ")

cashiersname = input("Enter name of cashier: ")

discount = int(input("Enter discount if there is any: ")) / 100

while discount < 0:

	print("Enter valid a discount or zero(0) for no discount")

	discount = int(input("Enter discount if there is any: ")) / 100

vat = (17.5 / 100) * totalpriceofallitems

bills = totalpriceofallitems - discount + vat

print("\n")

print("\nSEMICOLON STORES.")

print("\nMAIN BRANCH")

print("\nLOCATION: 312, HERBERT MACAULAY WAY, SABO, YABA, LAGOS, NIGERIA.")

print("\nTEL: +234789063532")

print("\nDATE:",current)

print("CASHIER'S NAME:",cashiersname)

print("\nCUSTOMER'S NAME:",customersname)

print("================================================================")

print(f'{"ITEMS"}\t\t{"PRICE"}\t\t{"QUANTITY"}\t{"TOTAL(NGN)"}')

for count in range (len(items)):
	print(f'{items[count]}\t\t{price[count]}\t\t{quantity[count]}\t\t{total[count]}')

print("================================================================")

print("\t\t\t\t SUB TOTAL:",totalpriceofallitems)

print("\t\t\t\t DISCOUNT:",discount)


print("\t\t\t\t VAT @ 17.5%:",vat)

print("================================================================")

print("\t\t\t\t Bill total", bills)

print("================================================================")

print("This is not a receipt,kindly pay",bills)

pay = int(input("How much did the customer give you? "))

while pay < bills:

	print("Please pay in full")

	pay = int(input("How much did the customer give you? "))

balance = pay - bills


print("\n")

print("\nSEMICOLON STORES.")

print("\nMAIN BRANCH")

print("\nLOCATION: 312, HERBERT MACAULAY WAY, SABO, YABA, LAGOS, NIGERIA.")

print("\nTEL: +234789063532")

print("\nDATE:",current)

print("CASHIER'S NAME:",cashiersname)

print("\nCUSTOMER'S NAME:",customersname)

print("================================================================")

print(f'{"ITEMS"}\t\t{"PRICE"}\t\t{"QUANTITY"}\t{"TOTAL(NGN)"}')

for count in range (len(items)):
	print(f'{items[count]}\t\t{price[count]}\t\t{quantity[count]}\t\t{total[count]}')

print("================================================================")

print("\t\t\t\t SUB TOTAL:",totalpriceofallitems)

print("\t\t\t\t DISCOUNT:",discount)


print("\t\t\t\t VAT @ 17.5%:",vat)

print("================================================================")

print("\t\t\t\t Bill total:", bills)

print("\t\t\t\t amount paid:", pay)

print("\t\t\t\t Remaining Balance:", balance)

print("================================================================")

print("Thank you for your patronage")















		



	

	




	


	 