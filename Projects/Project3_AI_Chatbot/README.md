````markdown
# AI Chatbot

A simple rule-based AI chatbot built with Python. This project is designed as a learning project to practice Python fundamentals, modular programming, file handling, user input validation, random responses, and basic session-based conversation history.

## Features

- Responds to greetings such as `hi`, `hello`, and `hey`
- Provides basic information about Python
- Provides basic information about FastAPI
- Responds to `what can you do`
- Provides randomized responses
- Handles unknown inputs
- Prevents empty user input
- Supports chatbot commands
- Stores conversation history in daily files
- Displays conversation history for any valid date
- Clears the current session's conversation history
- Saves the current session's conversation
- Tracks session start and session close times
- Handles `KeyboardInterrupt` gracefully
- Handles unexpected runtime errors

## Commands

| Command | Description |
|---|---|
| `help` | Show available commands |
| `history` | Show conversation history for a selected date |
| `clear` | Clear the current session's conversation |
| `save` | Save the current session's conversation |
| `save chat` | Save the current session's conversation |
| `save conversation` | Save the current session's conversation |
| `exit` | Exit the chatbot |
| `bye` | Exit the chatbot |
| `goodbye` | Exit the chatbot |
| `see you` | Exit the chatbot |

## Supported Chatbot Inputs

### Greetings

```text
hi
hello
hey
````

### Help

```text
what can you do
```

### Python

```text
python
what is python
tell me about python
```

### FastAPI

```text
fastapi
what is fastapi
tell me about fastapi
```

Other inputs receive a randomized unknown-response message.

## Project Structure

```text
Project3_AI_Chatbot/
│
├── main.py
├── chatbot.py
├── responses.py
├── helpers.py
├── history.py
├── README.md
│
├── chats/
│   ├── YYYY_MM_DD_chat.txt
│   │
│   └── saved/
│       └── YYYY_MM_DD_HH_MM_SS.txt
│
└── .gitignore
```

## File Responsibilities

### `main.py`

Controls the main application flow.

Responsibilities:

* Starts the chatbot
* Creates the current session
* Handles commands
* Gets user input
* Sends messages to the chatbot
* Displays responses
* Records session start and close
* Handles `KeyboardInterrupt`
* Handles unexpected errors

### `chatbot.py`

Contains the chatbot's basic input-matching logic.

It checks the normalized user input against predefined input lists and selects an appropriate response category.

### `responses.py`

Contains the predefined response collections used by the chatbot.

Response categories include:

* Greeting responses
* Unknown responses
* Goodbye responses
* Help responses
* Python responses
* FastAPI responses

Responses are selected randomly using Python's `random` module.

### `helpers.py`

Contains reusable helper functions for:

- Getting non-empty user input
- Validating dates in `YYYY_MM_DD` format

### `history.py`

Handles conversation history operations.

Functions include:

- `add_history()`
- `show_history()`
- `clear_history()`
- `save_chat()`

## Conversation History

Chat history is stored in a daily file using the following format:

```text
chats/YYYY_MM_DD_chat.txt
```

For example:

```text
chats/2026_08_09_chat.txt
```

A normal conversation is stored as:

```text
[19:21:31]
User: hello
Bot: Hi! How can I help you today?
```

Each application session also records:

```text
[19:21:26] Session Started
```

and when the session ends:

```text
[19:22:15] Session Closed
```

Multiple sessions on the same date are stored in the same daily history file.

## Viewing History

Use:

```text
history
```

The chatbot asks for a date:

```text
Enter the date to view history: 2026_08_09
```

The complete history for that date is then displayed.

The required date format is:

```text
YYYY_MM_DD
```

## Clearing History

Use:

```text
clear
```

The `clear` command clears the conversation belonging to the **current active session**.

Previous sessions stored in the same daily history file are preserved.

The current session's `Session Started` marker remains so the session can continue after clearing.

## Saving a Conversation

The following inputs can be used:

```text
save
save chat
save conversation
```

The current session is saved into:

```text
chats/saved/
```

The saved filename contains the date and session start time:

```text
YYYY_MM_DD_HH_MM_SS.txt
```

For example:

```text
chats/saved/2026_08_09_19_25_59.txt
```

Saving multiple times during the same session updates the saved copy of that session.

## Input Handling

User input is stripped of leading and trailing whitespace.

Empty input is rejected:

```text
Input can't be empty..
```

Command matching uses a normalized lowercase version of the input, while the original user message is preserved when writing conversation history.

For example:

```text
User input:
What Is Python
```

The program can use:

```text
what is python
```

for matching while preserving:

```text
What Is Python
```

in the conversation history.

## Error Handling

The application handles:

### Keyboard interruption

If the user presses `Ctrl+C`:

```text
Program interrupted by user..
```

The session is also recorded as closed.

### Unexpected errors

Unexpected runtime errors are caught and displayed instead of producing an unhandled traceback.

### Missing history files

If history does not exist for the requested date:

```text
No history found for YYYY_MM_DD.
```

## Technologies Used

- Python
- Python standard library
- File handling
- `datetime`
- `random`

No external Python packages are required.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

You should see:

```text
==== Welcome to AI Chatbot ====
```

Start entering messages to interact with the chatbot.

## Example

```text
==== Welcome to AI Chatbot ====

Hello sir/mam please start conversation or type exit to quit: hello

Hi! How can I help you today?

Hello sir/mam please start conversation or type exit to quit: python

Python is a high-level, interpreted, programming language known for readability.

Hello sir/mam please start conversation or type exit to quit: save

Chat saved successfully..

Hello sir/mam please start conversation or type exit to quit: exit

Goodbye! Have a great day.

Thanks for using AI Chatbot..
```

## Learning Goals

This project was built to practice:

- Python functions
- Modules and imports
- Lists and dictionaries
- Conditional statements
- `while` loops
- String methods
- User input handling
- Exception handling
- File reading and writing
- Append and overwrite file modes
- Working with timestamps
- Date validation
- Random selection
- Session management
- Modular project structure

## Future Improvements

Possible future improvements include:

- More chatbot intents
- More natural language matching
- More commands
- Better conversation context
- Improved history management
- More advanced chatbot responses
- Integration with an AI model or API

## Project Status

**Completed**

The current version implements the planned rule-based chatbot, command system, session history, history viewing, clearing, and saving functionality.