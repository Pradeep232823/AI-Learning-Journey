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

def remove_punctuation(text):
    characters = []
    punctuations = {
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    }
    for ch in text:
        if ch not in punctuations:
            characters.append(ch)

    return "".join(characters)

def get_filename():
    while True:
        print()
        filename = input("Enter the file name to save the summary: ").strip()

        if not filename:
            print()
            print("Filename can't be empty..")
            continue

        if len(filename) > 100:
            print()
            print("Filename is too long..")
            continue
        invalid_characters = {'\\', '/', ':', '*', '?', '"', '<', '>', '|'}

        is_valid = True
        for ch in filename:
            if ch in invalid_characters:
                is_valid = False
                break
        if not is_valid:
            print()
            print("Filename contains invalid characters")
            continue
        
        if filename[-4:] != ".txt":
            filename += ".txt"

        return filename
