import helpers

def display_menu():
    print("""
====================
AI Notes Generator
====================

1. Paste Text
2. Load Text File
3. Exit
""")

def main():
    while True:
        display_menu()
        choice = helpers.get_choice("Enter the number according to your choice: ")
        if choice is None:
            continue

        match choice:
            case 1:
                print()
                print("Paste Text selected..")
            case 2:
                print()
                print("Load Text File selected")
            case 3:
                print()
                print("Thank you for using AI Notes Generator..\n")
                break
            case _:
                helpers.invalid_choice()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nProgram interrupted by user..\n")
    except Exception as e:
        print()
        print(f"Something went wrong: {e}")