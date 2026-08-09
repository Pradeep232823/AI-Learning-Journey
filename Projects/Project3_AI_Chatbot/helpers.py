from datetime import datetime

def get_user_input(prompt):
    while True:
        print()
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print()
            print("Input can't be empty..")

def validate_date(prompt):
    while True:
        print()
        date = input(prompt)

        try:
            date = datetime.strptime(date, "%Y_%m_%d").date()
            return date.strftime("%Y_%m_%d")
        except ValueError:
            print()
            print("Invalid date.")