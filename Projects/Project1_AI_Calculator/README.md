# 🧮 AI Calculator

A command-line calculator application built with Python.

This was my first Python project in my AI Learning Journey. The project focuses on practicing Python fundamentals, functions, modules, file handling, input validation, and exception handling.

## 🚀 Features

- Addition of multiple numbers
- Subtraction of multiple numbers
- Multiplication of multiple numbers
- Division
- Power calculation
- Square root calculation
- Percentage calculation
- Calculation history
- Timestamped history records
- Input validation
- Divide-by-zero protection
- Negative-number validation for square root
- Graceful `KeyboardInterrupt` handling
- Menu-driven CLI interface

## 📁 Project Structure

``` text
AI-Calculator/
│
├── main.py
├── calculator.py
├── operations.py
├── helpers.py
├── history.py
└── history.txt
```

## 🛠️ Technologies Used

- Python
- math
- datetime
- File I/O
- Exception handling
- Python modules

## ▶️ How to Run

Make sure Python is installed on your system.

**Run: python main.py**

The application will display the main menu:

``` text
======= Welcome to AI Calculator =======

===============
Choose Action
===============

1. Start Calculation
2. Exit
```

Choose Start Calculation to access the calculator operations.

## 📋 Calculator Operations

The calculator provides the following operations:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Percentage
8. History
9. Exit

### Addition

Allows the user to enter two or more numbers and calculate their sum.

### Subtraction

Allows the user to enter two or more numbers and subtract them sequentially.

### Multiplication

Allows the user to enter two or more numbers and calculate their product.

### Division

Takes a numerator and denominator.

Division by zero is prevented by validating the denominator before performing the calculation.

### Power

Calculates a number raised to a given exponent.

### Square Root

Calculates the square root of a number.

Negative values are rejected because the calculator uses math.sqrt() for this operation.

### Percentage

Calculates what percentage one value represents of another.

**For example:**

``` text
Part value: 23
Total value: 50

Percentage: 46.0
```

## 📝 Calculation History

The calculator stores completed calculations in history.txt.

Each entry includes a timestamp, operation, input values, and result.

**Example:**

Timestamp: 2026-08-07 13:07 -> Percentage Done on 23, 50 and The result is: 46.0

The history can be viewed from the calculator menu.

### 🛡️ Error Handling

The project includes handling for several common errors:

- Non-numeric input
- Invalid menu choices
- Invalid number of operands
- Division by zero
- Invalid square-root input
- Missing history file
- Keyboard interruption using Ctrl + C

When Ctrl + C is pressed, the application exits the current operation gracefully instead of displaying a Python traceback.

## 🧩 Project Architecture

The project is divided into separate modules to keep responsibilities organized.

**main.py**

Provides the main application entry point and the initial menu.

**calculator.py**

Controls the calculator menu and connects user choices to the appropriate operations.

**operations.py**

Contains the actual calculator operations:

- add()
- sub()
- multiply()
- divide()
- power()
- square_root()
- percentage()

**helpers.py**

Contains reusable functions for:

- User input
- Number validation
- Menu validation
- Positive integer validation
- Continue-operation prompts
- Error messages

**history.py**

Handles:

- Saving calculation history
- Adding timestamps
- Reading and displaying history
- history.txt

Stores the calculator's persistent calculation history.

## 📚 What I Learned

Through this project, I practiced:

- Python variables and data types
- if statements
- while loops
- Functions
- Modules and imports
- Lists
- String formatting
- try / except
- ValueError
- FileNotFoundError
- KeyboardInterrupt
- File reading
- File writing
- File appending
- math module
- datetime
- Building a multi-file Python project
- Designing a menu-driven CLI application

## 🔄 Development Improvements

During development, the project was improved incrementally.

### Initial Version

The calculator supported the basic operations and stored calculation history.

### Improvements

- Fixed percentage history labeling
- Improved square-root prompts
- Added timestamps to calculation history
- Added graceful KeyboardInterrupt handling
- Added a clearer exit message
- Added consistent interruption handling across calculator operations

## 🎯 Project Status

**Completed ✅**

This project is part of my AI Learning Journey and represents my first completed Python project.
