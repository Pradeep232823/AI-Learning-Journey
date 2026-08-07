def non_numeric():
    print()
    print("Entered a non-numeric value. Please enter a valid number.")

def invalid_choice():
    print()
    print("Invalid choice. Please try again.")

def get_choice(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        non_numeric()
        return None

def paste_text():
    while True:
        try:
            print()
            print("Enter your notes here..\nPress Enter on a new line to finish..\n")

            lines = []

            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            return "\n".join(lines)

        except KeyboardInterrupt:
            print()
            print("Program interrupted by user..\n")
            return ""