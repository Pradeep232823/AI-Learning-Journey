import helpers
import operations
from history import show_history

def main_menu():
    while True:
        try:
            print("""
=================
Choose Operation
=================

1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Percentage
8. History
9. Exit
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue
            match choice:
                case 1:
                    operations.add()
                case 2:
                    operations.sub()
                case 3:
                    operations.multiply()
                case 4:
                    operations.divide()
                case 5:
                    operations.power()
                case 6:
                    operations.square_root()
                case 7:
                    operations.percentage()
                case 8:
                    show_history()
                case 9:
                    break
                case _:
                    helpers.invalid_choice()
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break