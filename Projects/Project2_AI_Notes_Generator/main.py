import helpers
import utils
import file_handler


def show_text(text, title):
    utils.display_statistics(text)
    print()
    print(title)
    print()
    print(text)

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
                text = helpers.paste_text()

                if text:
                    show_text(text,"You entered..")
            case 2:
                print()
                filename = input("Enter filename with path: ")
                content = file_handler.load_text(filename)
                if content is None:
                    continue
                if not content:
                    print()
                    print("No content in file..")
                    continue

                show_text(content,"Loaded text..")
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