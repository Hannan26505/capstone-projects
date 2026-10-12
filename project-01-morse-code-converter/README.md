# Text to Morse Code Converter

A Python project that converts text into Morse code using dots (`.`) and dashes (`-`).

## Features

- Converts uppercase and lowercase letters (A–Z).
- Supports digits (0–9).
- Separates words using `/`.
- Reports unsupported characters.
- Handles empty input.
- Includes automated tests for the conversion logic.

## Technologies Used

- Python 3
- Git and GitHub

## Project Structure

```text
project-01-morse-code-converter/
├── main.py
├── test_main.py
└── README.md
```

## How to Run

1. Install Python 3.
2. Open a terminal in this project directory.
3. Run the converter:

   ```bash
   python main.py
   ```

## Example

**Input**

```text
HELLO WORLD
```

**Output**

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## Run the Tests

Execute the automated tests using:

```bash
python test_main.py
```

Expected success message:

```text
All tests passed!
```

## What I Learned

- Using Python dictionaries for character mapping.
- Processing strings with loops and conditionals.
- Writing reusable functions.
- Handling unsupported input.
- Writing automated tests using assertions.
- Organizing a Python project for GitHub.

## Project Status

Completed — Project 1 of my capstone projects portfolio.