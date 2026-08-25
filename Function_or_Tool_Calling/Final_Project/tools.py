from datetime import datetime

def calculate(a, b, operation):
    if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
        return "Invalid values"
    
    operation = operation.lower()
    if operation in ["add", "addition"]:
        return a + b

    if operation in ["sub", "subtract"]:
        return a - b

    if operation in ["mul", "multiply"]:
        return a * b

    if operation in ["div", "divide"]:
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    return "Unsupported operation"

def temp_conversion(temp, conversion):
    if not isinstance(temp, (int, float)):
        return "Invalid value"
    
    conversion = conversion.lower()

    if conversion in ["celsius to fahrenheit", "celsius to farenheit"]:
        return (temp * 9 / 5) + 32

    if conversion in ["fahrenheit to celsius", "farenheit to celsius"]:
        return (temp - 32) * (5 / 9)

    return "Unsupported conversion"

def get_datetime(input):
    input = input.lower()

    now = datetime.now()

    date_and_time = now.strftime("%Y-%m-%d %H:%M:%S")

    date = now.strftime("%Y-%m-%d")

    time = now.strftime("%H:%M:%S")

    if input == "date":
        return date
    if input == "time":
        return time
    if input == "date and time":
        return date_and_time
    return "Invalid input"

def count_words(text):
    if not text:
        return "No text detected."
    return len(text.split())

available_tools = {
    "calculate": calculate,
    "temp_conversion": temp_conversion,
    "get_datetime": get_datetime,
    "count_words": count_words
}