import helpers

def load_text(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            content = file.read()
        if content:
            return content
        print()
        print("No data in file..")
        
    except FileNotFoundError:
        print()
        print("File not found..")
        return None
    except PermissionError:
        print()
        print("File permission denied..")
        return None
    except Exception as e:
        print()
        print(f"Something went wrong while reading the file: {e}..")
        return None

def save_summary(summary):
    while True:
        try:
            filename = helpers.get_filename()
            path = f"summaries/{filename}"
            try:
                with open(path, "r"):
                    is_exist = True
            except FileNotFoundError:
                is_exist = False

            if is_exist:
                while True:
                    print()
                    choice = input("File already exists.. \nDo you want to overwrite (Y/N): ").strip().lower()

                    if choice == "y":
                        with open(path, "w") as file:
                            file.write(summary)
                        print()
                        print("File overwritten successfully..")
                        return
                    elif choice == "n":
                        print()
                        print("Enter another filename..")
                        break
                    else:
                        helpers.invalid_choice()
            else:
                with open(path, "w") as file:
                    file.write(summary)
                print()
                print("Summary saved successfully..")
                return
            
        except PermissionError:
            print()
            print("Permission denied..")
            return
        except Exception as e:
            print()
            print(f"Something went wrong: {e}")
            return