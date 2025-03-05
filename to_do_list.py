tasks = []

def enter_choice(number):

	try:

		number = int(number)

		if number not in range(1, 6):

			return "invalid input"

		return number

	except ValueError:

		return "invalid input"

def add_task(task):

	if type(task) != str or task == " ":

		return "invalid input"

	task_item = {"status": "[]","task":task}

	tasks.append(task_item)

	return tasks

def display_all_task():

	if not tasks:

		print("No task added yet")

	else:

		for element in tasks:

			print(f"{element["status"]} {element["task"]}")

def mark_completed_task():

	if not tasks:

		print("No task added yet")

	else:

		try:

			number = int(input("Task number completed: "))

			while number not in range(1, len(tasks) + 1):

				print("\ninvalid input")

				number = int(input("\nTask number completed: "))

			if tasks[number - 1]["status"] == "[X]":

				print("Task already completed")

			else:

				tasks[number - 1]["status"] = "[X]" 

				print("Task completed")

		except ValueError:

			return "invalid input"

def delete_task():

	if not tasks:

		print("No task to be deleted.")

	else:

		try:

			number = int(input("Task number to be deleted: "))

			while number not in range(1, len(tasks) + 1):

				print("\ninvalid input")

				number = int(input("\nTask number to be deleted: "))

			removed_task = tasks.pop(number - 1)

			print(f"'{removed_task["task"]}' deleted successfully")

		except ValueError:

			return "invalid input"



while True:

	print("""

	1. Add a task

	2. View all tasks

	3. Mark a task as complete

	4. Delete a task

	5. Exit

	""")

	value = (input("Enter a choice: " ))
 
	choice = enter_choice(value)

	while choice == "invalid input":

		print(choice)

		value = (input("Enter a choice: " ))
 
		choice = enter_choice(value)

	if choice == 1:

		value = input("What are you adding? ")

		add_task(value)

		print("Task added!")

	elif choice == 2:

		display_all_task()

	elif choice == 3:

		mark_completed_task()

	elif choice == 4:

		delete_task()

	elif choice == 5:

		print("\nExiting application, Thank you...")

		break


