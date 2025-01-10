def pizza_wahala():

    print(f"{'pizza type':<15}{'Number of slice':<20}{'price per box':<20}")

    print(f"{'sapa size':<15}{4:<20}{2500:<20}")

    print(f"{'small money':<15}{6:<20}{2900:<20}")

    print(f"{'Big boys':<15}{8:<20}{4000:<20}")

    print(f"{'Odogwu':<15}{12:<20}{5200:<20}")

    number_of_guests = int(input("\nHow many guests are you receiving? "))
    
    while number_of_guests < 0:

        print("Please enter a valid number of guests")

        number_of_guests = int(input("How many guests are you receiving? "))
    
    pizza_type = input("\nWhat type of pizza do you want? ").lower()
    
    while pizza_type != "sapa size" and pizza_type != "small money" and pizza_type != "big boys" and pizza_type != "odogwu":
       
        print("Please enter a valid pizza type to purchase.")

        pizza_type = input("\nWhat type of pizza do you want? ").lower()

    if pizza_type == "sapa size":

        number_of_boxes = int(input("How many boxes of pizza do you want to buy? "))

        slices = 4

        price_per_box = 2500

        total_slices = number_of_boxes * slices

        remaining_slices = total_slices - number_of_guests
	
        amount = price_per_box * number_of_boxes

        print(f"The remaining slices of pizza that will be left are: {remaining_slices}")

        print(f"You are paying: {amount}")

    elif pizza_type == "small money":

        number_of_boxes = int(input("How many boxes of pizza do you want to buy? "))

        slices = 6

        price_per_box = 2900

        total_slices = number_of_boxes * slices

        remaining_slices = total_slices - number_of_guests

        amount = price_per_box * number_of_boxes

        print(f"The remaining slices of pizza that will be left are: {remaining_slices}")

        print(f"You are paying: {amount}")

    elif pizza_type == "big boys":

        number_of_boxes = int(input("How many boxes of pizza do you want to buy? "))

        slices = 8

        price_per_box = 4000

        total_slices = number_of_boxes * slices

        remaining_slices = total_slices - number_of_guests

        amount = price_per_box * number_of_boxes

        print(f"The remaining slices of pizza that will be left are: {remaining_slices}")

        print(f"You are paying: {amount}")

    elif pizza_type == "odogwu":

        number_of_boxes = int(input("How many boxes of pizza do you want to buy? "))

        slices = 12

        price_per_box = 5200

        total_slices = number_of_boxes * slices

        remaining_slices = total_slices - number_of_guests

        amount = price_per_box * number_of_boxes

        print(f"The remaining slices of pizza that will be left are: {remaining_slices}")

        print(f"You are paying: {amount}")

    

pizza_wahala()
