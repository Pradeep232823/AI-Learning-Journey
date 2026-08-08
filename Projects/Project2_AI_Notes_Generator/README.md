# AI Notes Generator

A command-line application that generates simple summarized notes from text using an **offline, rule-based extractive summarization algorithm**.

The project does not use any paid AI API or external LLM. It processes the text locally using Python.

## Features

- Paste notes directly into the terminal
- Load notes from a `.txt` file
- Display text statistics
  - Character count
  - Word count
  - Line count
- Clean and preprocess text
- Split text into sentences
- Calculate word frequency
- Remove common stop words
- Score sentences based on word frequency
- Generate a summary by selecting the highest-scoring sentences
- Preserve the original order of selected sentences
- Save summaries as `.txt` files
- Validate summary filenames
- Handle existing summary files
- Ask before overwriting an existing summary
- Handle common file and input errors
- Handle `KeyboardInterrupt` gracefully

## How It Works

The application uses a simple extractive summarization approach.

```text
User Input
    │
    ├── Paste Text
    │
    └── Load Text File
          │
          ▼
     Clean Text
          │
          ▼
    Split Sentences
          │
          ▼
    Calculate Word Frequency
          │
          ▼
     Score Sentences
          │
          ▼
   Select Top 30% Sentences
          │
          ▼
 Restore Original Sentence Order
          │
          ▼
      Generate Summary
          │
          ▼
       Display Summary
          │
          ▼
       Save Summary
```

## Sentence Scoring

The summarizer counts the frequency of meaningful words while ignoring common stop words.

Sentences containing more frequently occurring meaningful words receive higher scores.

The highest-scoring sentences are selected for the summary.

The selected sentences are then placed back into their original order so that the summary remains readable.

Project Structure

``` text
AI_Notes_Generator/
│
├── main.py
├── summarizer.py
├── file_handler.py
├── helpers.py
├── utils.py
├── rough.py
├── summaries/
├── sample_texts/
│   ├── article.txt
│   ├── article1.txt
│   ├── article2.txt
│   └── article3.txt
│
├── README.md
└── .gitignore
```
**rough.py** is used for experimentation and is excluded from the main project workflow.

## Modules

**main.py**

Controls the main CLI application.

Responsibilities:

- Display the menu
- Accept user choices
- Handle pasted text
- Handle text-file input
- Display statistics
- Generate summaries
- Ask whether the user wants to save a summary

**summarizer.py**

Contains the core summarization logic.

Responsibilities:

- Clean text
- Split text into sentences
- Calculate word frequency
- Score sentences
- Generate the final summary

**file_handler.py**

Handles file operations.

Responsibilities:

- Load .txt files
- Save summaries
- Handle existing summary files
- Handle overwrite confirmation
- Handle file-related errors

**helpers.py**

Contains reusable input and validation functions.

Responsibilities:

- Validate menu input
- Handle non-numeric input
- Accept pasted text
- Validate summary filenames
- Remove punctuation

**utils.py**

Contains text statistics functions.

Responsibilities:

- Count characters
- Count words
- Count lines
- Display statistics

## Requirements

- Python 3.10 or newer

The project uses Python's standard library and does not require paid APIs.

## How to Run

Open a terminal in the project directory and run:

``` text
python main.py
```

## Usage
After starting the application:

``` text
1. Paste Text
2. Load Text File
3. Exit
``` 

### Option 1 — Paste Text

Select:

``` text
1
```
Enter your notes line by line.

Press **Enter on an empty line** to finish entering the text.

The application will then:

- Display statistics
- Generate a summary
- Display the summary
- Ask whether to save it

### Option 2 — Load Text File

Select:

``` text
2
```
Enter the filename or path to a **.txt** file.

**Example:**

``` text
sample_texts/article2.txt
```
The application loads the file and processes it in the same way as pasted text.

### Option 3 — Exit

Select:

``` text
3
```
to exit the application.

**Example**

## Input

``` text
AI is transforming many industries.
AI systems can analyze large amounts of data and automate repetitive tasks.
Businesses use AI for customer support, healthcare, finance, and transportation.
Learning AI requires understanding programming, mathematics, and problem-solving.
```

## Generated Summary

``` text
AI systems can analyze large amounts of data and automate repetitive tasks.
```
The exact summary depends on the frequency of meaningful words in the input.

## Summary Saving
When a summary is generated, the application asks:

``` text
Do you want to save this summary (Y / N):
```
If Y is selected, the application asks for a filename.

**For example:**

``` text
Enter the file name to save the summary: article_summary
```
The application automatically adds the .txt extension:

``` text
summaries/article_summary.txt
```
If the file already exists, the application asks:

``` text
File already exists..
Do you want to overwrite (Y/N):
```

## Filename Validation

The application validates summary filenames by checking:

- Filename is not empty
- Filename is not longer than 100 characters
- Filename does not contain invalid characters
- .txt is added automatically when it is not provided

Invalid filename characters include:

``` text
\ / : * ? " < > |
```

## Error Handling

The application handles common errors including:

- Invalid menu input
- Invalid filename
- File not found
- Permission denied
- Empty input
- Empty text files
- Invalid Y/N choices
- Keyboard interruption

## Technologies and Concepts Used

- Python
- Functions
- Modules
- Lists
- Sets
- Dictionaries
- Loops
- Conditional statements
- String processing
- File handling
- Exception handling
- Sorting
- Dictionary frequency counting
- Input validation
- Modular programming
- Basic text-processing algorithms

## Limitations

This project uses a rule-based extractive summarization algorithm rather than an LLM.

Therefore, it does not:

- Understand the meaning of text like an LLM
- Generate new sentences
- Rewrite information in its own words
- Understand context deeply
- Guarantee that every generated summary is semantically ideal

Instead, it identifies sentences that contain frequently occurring meaningful words and selects the highest-scoring sentences.

## What I Learned

Through this project, I practiced building a multi-module Python CLI application.

Key learning areas included:

- Working with multiple Python modules
- Reading and writing text files
- Validating user input
- Handling exceptions
- Processing strings
- Using dictionaries for frequency analysis
- Sorting dictionary data
- Designing a simple text-ranking algorithm
- Separating application responsibilities across modules
- Building a complete CLI workflow
- Testing normal and edge-case scenarios

## Project Status

**Core functionality completed.**

The application supports:

- Text input
- File input
- Text statistics
- Rule-based summarization
- Summary display
- Summary saving
- Filename validation
- Overwrite handling
- Error handling