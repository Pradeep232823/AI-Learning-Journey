import helpers
import utils
import file_handler
import summarizer

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
                    process_summary("notes",text)
                else:
                    print()
                    print("No data entered..")
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

                process_summary("file", content)

            case 3:
                print()
                print("Thank you for using AI Notes Generator..\n")
                break
            case _:
                helpers.invalid_choice()

def process_summary(case, text):
    summary = summarizer.generate_summary(text)
    print()
    print(f"====== Summary for your {case} ======")
    print()
    print(summary)

    while True:
        print()
        save_choice = input("Do you want to save this summary (Y / N): ").strip().lower()

        if save_choice == "y":
            file_handler.save_summary(summary)
            break
        elif save_choice == "n":
            print()
            print("Exiting without saving summary..")
            break
        else:
            helpers.invalid_choice()
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nProgram interrupted by user..\n")
    except Exception as e:
        print()
        print(f"Something went wrong: {e}")