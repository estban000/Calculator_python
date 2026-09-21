import tkinter as tk

# function to add a character to the display screen
def add(screen, value):
    screen.insert(tk.END, value)

# function to clear the display screen
def clear(screen):
    screen.delete(0, tk.END)

# function to handle backspace operations
def backspace(screen):
    current_value = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current_value[:-1])

# function to evaluate the expression on the display screen (replace the symbols for multiplication and division with Python's operations, also handle errors)
def calculate(screen):
    expression = screen.get().replace("x", "*").replace("÷", "/")
    try:
        result = eval(expression, {"__builtins__": {}}, {})
    except (SyntaxError, TypeError, ZeroDivisionError, NameError):
        result = "Erreur"

    screen.delete(0, tk.END)
    screen.insert(0, str(result))
