# 🧮 Python CLI Calculator

A simple, menu-driven **Command-Line Interface (CLI) Calculator** developed using Python. This calculator performs basic arithmetic operations on multiple numbers entered by the user.

The project uses Python functions, `*args`, loops, and `match-case` statements to perform calculations through an interactive terminal interface.

## ✨ Features

- ➕ **Addition:** Calculate the sum of multiple numbers.
- ➖ **Subtraction:** Subtract multiple numbers sequentially.
- ✖️ **Multiplication:** Calculate the product of multiple numbers.
- ➗ **Division:** Divide numbers sequentially.
- 🔢 **Multiple Inputs:** Enter as many numbers as needed for an operation.
- 🖥️ **Interactive CLI:** Navigate through a simple menu.
- 🔁 **Continuous Operation:** Perform multiple calculations without restarting the program.
- 🚪 **Exit Option:** Enter `0` to exit the calculator.

## 🛠️ Technologies Used

- **Python 3.10 or newer**
- Functions and return values
- `*args` for handling multiple arguments
- `while` loops
- `for` loops
- `match-case` statements
- Lists for collecting numbers
- User input with `input()`

## 🚀 Getting Started

### Prerequisites

Install Python 3.10 or newer.

Check your Python version:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Python-CLI-Calculator.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd Python-CLI-Calculator
```

### 3. Run the Calculator

If your Python file is named `main.py`, execute:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

No external libraries are required.

## 🎮 How to Use

When you start the program, a menu displays the available operations.

| Input | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `0` | Exit |

### Example: Addition

```text
Enter '+' to find sum of numbers
Enter '-' to find sub of numbers
Enter '*' to find product of numbers
Enter '/' to find division of numbers
Enter '0' to Exit the calculator: +

Enter numbers you want to find sum of and Enter '=' to calculate: 10
Enter numbers you want to find sum of and Enter '=' to calculate: 20
Enter numbers you want to find sum of and Enter '=' to calculate: 30
Enter numbers you want to find sum of and Enter '=' to calculate: =

60
```

### Example: Multiplication

Enter `*`, provide the numbers one by one, and enter `=` when you want the result.

```text
Numbers: 2, 3, 4
Result: 24
```

### How the Operations Work

- **Addition:** Adds all entered numbers together.
- **Subtraction:** Starts with the first number and subtracts each subsequent number.
- **Multiplication:** Multiplies all entered numbers together.
- **Division:** Starts with the first number and divides it by each subsequent number.

Enter `=` to finish entering numbers for the current operation.

## 📂 Project Structure

```text
Python-CLI-Calculator/
├── main.py
└── README.md
```

## 🧠 Concepts Practiced

This project demonstrates:

- Creating and calling Python functions.
- Using `*args` to accept a variable number of arguments.
- Performing arithmetic with loops.
- Collecting user input in lists.
- Using `match-case` for menu selection.
- Returning calculation results from functions.
- Building an interactive command-line application.

## 🔮 Future Improvements

- Handle division by zero.
- Validate numeric input and handle invalid entries.
- Display a helpful message when no numbers are entered.
- Support decimal numbers using `float()`.
- Prevent invalid calculations when too few numbers are provided.
- Add exponentiation and modulo operations.
- Improve error handling and user experience.
- Add calculation history.

## 👨‍💻 Author

Created as a beginner Python project to practice functions, variable-length arguments, loops, and basic arithmetic operations.

## 📄 License

This project is intended for educational and personal learning purposes. Consider adding an MIT License if you want to allow others to use, modify, and distribute your code under its terms.
