import time
from datetime import datetime

def add_history(operation, values, result):
    try:
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M")

        with open("history.txt","a") as file:
            val_str = ", ".join(str(n) for n in values)
            file.write(f"\nTimestamp: {formatted_now} -> {operation} Done on {val_str} and The result is: {result}")
        print()
        print("History Updated Successfully")
    except Exception as e:
        print()
        print(f"Something went wrong while updating history: {e}")

def show_history():
    try:
        with open("history.txt","r") as file:
            content = file.read()
        print()
        print(content)
    except FileNotFoundError:
        print()
        print("No data found")
    except Exception as e:
        print()
        print(f"Something went wrong while reading the file: {e}")