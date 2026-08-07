import helpers
import history
import math

def add():
    while True:
        try:
            n = helpers.is_positiveInt("How many numbers you want to add: ")

            if n < 2:
                print()
                print("Need 2 or more numbers to perform addition..")
                continue

            nums = []
            total = 0

            while n > 0:
                number = helpers.get_wholeNnum("Enter the number: ")
                nums.append(number)
                total += number
                if n > 1:
                    print()
                    print(f"Current Result: {total}")
                n -= 1

            print()
            print(f"Final Result: {total}")

            history.add_history("Addition", nums, total)
            
            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break

def sub():
    while True:
        try:
            n = helpers.is_positiveInt("How many numbers you want to subtract: ")

            if n < 2:
                print()
                print("Need 2 or more numbers to perform subtraction..")
                continue
            total = 0

            nums = []

            while n > 0:
                number = helpers.get_wholeNnum("Enter the number: ")
                nums.append(number)
                if total == 0:
                    total += number
                else:
                    total -= number
                if n > 1:
                    print()
                    print(f"Current Result: {total}")
                n -= 1

            print()
            print(f"Final Result: {total}")

            history.add_history("Subtraction", nums, total)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break
def multiply():
    while True:
        try:
            n = helpers.is_positiveInt("How many numbers you want to multiply: ")

            if n < 2:
                print()
                print("Need 2 or more numbers to perform multiplication..")
                continue

            total = 1

            nums = []

            while n > 0:
                number = helpers.get_wholeNnum("Enter the number: ")
                nums.append(number)
                total *= number
                if n > 1:
                    print()
                    print(f"Current Result: {total}")
                n -= 1

            print()
            print(f"Final Result: {total}")

            history.add_history("Multiplication", nums, total)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break

def divide():
    while True:
        try:
            numerator = helpers.get_wholeNnum("Enter value for Numerator: ")

            while True:
                denominator = helpers.get_wholeNnum("Enter value for Denominator: ")

                if denominator  == 0:
                    print()
                    print("Can't divide by 0..")
                    continue
                break

            result = (numerator) / (denominator)

            print(f"Result: {result}")

            history.add_history("Division", [numerator, denominator], result)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break

def power():
    while True:
        try:
            num = helpers.get_wholeNnum("Enter the number: ")
            exponent = helpers.get_wholeNnum("Enter the exponent value: ")

            result = (num) ** (exponent)

            print()
            print(f"Result: {result}")

            history.add_history("Power", [num, exponent], result)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break

def square_root():
    while True:
        try:
            num = helpers.get_wholeNnum("Enter number to check square root: ")

            if num < 0:
                print()
                print("Enter only positive numbers to check square root..")
                continue

            result = math.sqrt(num)

            print()
            print(f"Result: {result}")

            history.add_history("Square root", [num], result)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break

def percentage():
    while True:
        try:
            part_value = helpers.get_wholeNnum("Enter the part value: ")

            while True:
                total_value = helpers.get_wholeNnum("Enter the total value: ")
                if total_value == 0:
                    print()
                    print("Can't use 0 as total value")
                    continue
                break

            percentage = ((part_value) / (total_value) ) * (100)

            print()
            print(f"Percentage: {percentage}")

            history.add_history("Percentage", [part_value, total_value], percentage)

            if helpers.continue_operation():
                continue
            break
        except KeyboardInterrupt:
            print()
            print("User stopped code execution through keyboard interruption..\n")
            break