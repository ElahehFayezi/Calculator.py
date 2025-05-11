# PyQt5 Calculator 🧮

A simple yet elegant calculator built using Python and PyQt5.  
It supports basic arithmetic operations like addition, subtraction, multiplication, and division.

## 💻 Features

- GUI made with PyQt5
- Responsive layout using manual geometry (can be improved with layout managers)
- Basic operations: `+`, `-`, `*`, `/`
- Clear and backspace functionality
- Error handling for invalid expressions
- Styled using custom colors and fonts

## 🚀 Getting Started

### Prerequisites

Make sure Python and PyQt5 are installed:

```bash
pip install PyQt5

## Run the Calculator

python calculator.py

Replace calculator.py with the actual filename if different.

🧠 How It Works
Uses QLineEdit to display the input and results.

Buttons are connected to slot functions using lambda.

📁 File Structure

calculator.py        # Main Python file with GUI and logic
README.md            # Project documentation


📌 To-Do
Improve layout using QGridLayout for better responsiveness

Add keyboard input support

Implement a safer expression evaluator (instead of eval())

✨ Author
Elaheh Fayezi
📧 eng.elahefayezi@gmail.com

Feel free to fork and contribute! 🌱
