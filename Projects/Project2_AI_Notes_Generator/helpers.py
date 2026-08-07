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