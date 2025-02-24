print('Welcome to semicolon Expense Tracker App')
print('===========================================')

expense = []

print('1. Add on expense')
print('2. View all expense')
print('3. Calculate Total Expense')
print('4. Exit')

while True:
    try:
        value = int(input('Enter your choice: '))

        if value not in range(1, 5) or value is type(str):

            raise ValueError("Invalid input, please choose a valid option.")

        break

    except ValueError as e:

        print(e)

while True:

    if value == 1:

        while True:

            try:

                date = input('Enter date (yyyy-mm-dd): ')

                if len(date) != 10 or date[4] != '-' or date[7] != '-':

                    raise ValueError("Invalid date format. Please enter date in yyyy-mm-dd format.")
                break
            except ValueError as e:
                print(e)

        description = input('Enter description: ')

        while True:
            try:
                amount = input('Enter amount: ')
                amount = float(amount)
                if amount < 0:
                    raise ValueError("Amount must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input for amount: {e}")

        expense.append({'date': date, 'description': description, 'amount': amount})

        print('Expenses added')

        print('1. Add on expense')
        print('2. View all expense')
        print('3. Calculate Total Expense')
        print('4. Exit')

        while True:
            try:
                value = int(input('Enter your choice: '))
                if value not in range(1, 5):
                    raise ValueError("Invalid input, please choose a valid option.")
                break
            except ValueError as e:
                print(e)

    elif value == 2:
        if not expense:
            print("No expenses recorded yet.")
        else:
            for expenses in expense:
                print(f"Date: {expenses['date']}, Description: {expenses['description']}, Amount: {expenses['amount']}")

        print('1. Add on expense')
        print('2. View all expense')
        print('3. Calculate Total Expense')
        print('4. Exit')

        while True:
            try:
                value = int(input('Enter your choice: '))
                if value not in range(1, 5):
                    raise ValueError("Invalid input, please choose a valid option.")
                break
            except ValueError as e:
                print(e)

    elif value == 3:
        total = 0
        for amount in expense:
            total += amount['amount']
        print(f"Total Expenses : {total}")

        print('1. Add on expense')
        print('2. View all expense')
        print('3. Calculate Total Expense')
        print('4. Exit')

        while True:
            try:
                value = int(input('Enter your choice: '))
                if value not in range(1, 5):
                    raise ValueError("Invalid input, please choose a valid option.")
                break
            except ValueError as e:
                print(e)

    elif value == 4:
        print('Exiting the App, Goodbye')
        break
