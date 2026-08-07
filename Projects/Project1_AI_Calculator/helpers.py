def non_numeric():
    print()
    print("Entered a non-numeric value. Please enter a valid number.")

def invalid_choice():
    print()
    print("Invalid choice. Please try again.")

def get_choice(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            non_numeric()
            return None

def get_wholeNnum(prompt):
    while True:
        print()
        num = input(prompt)
        try:
            num = float(num)

            if num.is_integer():
                return int(num)
            else:
                return num
        except ValueError:
            print()
            print("Entered value is not a number or float value..")
            continue

def is_positiveInt(prompt):
    while True:
        print()
        num = input(prompt)

        try:
            num = int(num)
            if num < 0:
                print()
                print("Entered value is not positive..")
                continue
            return num
        except ValueError:
            print()
            print("Entered value is not an integer..")
            continue

def continue_operation():
    while True:
        print()
        choice = input("Do you want to continue this operation (Y / N): ").lower()

        if choice == "y":
            return True
        elif choice == "n":
            print()
            print("Going back to main menu..")
            return False
        print()
        print("Please enter Y or N")