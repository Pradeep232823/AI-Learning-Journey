import helpers
from calculator import main_menu as calc_main

def main_menu():
    while True:
        try:
            print("""
===============
Choose Action
===============

1. Start Calculation
2. Exit
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")

            if choice is None:
                continue

            match choice:
                case 1:
                    calc_main()
                case 2:
                    print()
                    print("Exiting the AI Calculator..\n")
                    break
                case _:
                    helpers.invalid_choice()
        except KeyboardInterrupt:
            print()
            print("\nUser stopped code execution through keyboard interruption..\n")
            break

if __name__ == "__main__":
    print()
    print("======= Welcome to AI Calculator =======")
    main_menu()