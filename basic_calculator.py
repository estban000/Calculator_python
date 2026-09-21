import tkinter as tk

from calculation_functions import add, clear, backspace, calculate

# Create the main window
window = tk.Tk()
window.title("Python Calculator")
window.geometry("350x500")
window.configure(bg="#4FBDF0")
window.resizable(False, False)

# Create the display screen of the calculator
screen = tk.Entry(
    window, font=("Arial", 22), justify="right",
    bg="#ffffff",
    fg="#000000",
    insertbackground="black",
    relief="flat", 
)
screen.pack(fill="x", padx=15, pady=20, ipady=12) # <= setting the size of the display screen 

# Define button labels, positions, colors and associated functions
button_data = [
    ("C", 0, 0, 2, "#E74C3C", lambda: clear(screen)), # 0,0,2 => row 0, column 0, column span 2
    ("⌫", 0, 2, 1, "#F39C12", lambda: backspace(screen)),
    ("÷", 0, 3, 1, "#3498DB", lambda: add(screen, "÷")),
    ("7", 1, 0, 1, "#ECF0F1", lambda: add(screen, "7")), # 1,0,1 => row 1, column 0, column span 1
    ("8", 1, 1, 1, "#ECF0F1", lambda: add(screen, "8")),
    ("9", 1, 2, 1, "#ECF0F1", lambda: add(screen, "9")),
    ("x", 1, 3, 1, "#3498DB", lambda: add(screen, "x")),
    ("4", 2, 0, 1, "#ECF0F1", lambda: add(screen, "4")),
    ("5", 2, 1, 1, "#ECF0F1", lambda: add(screen, "5")),
    ("6", 2, 2, 1, "#ECF0F1", lambda: add(screen, "6")),
    ("-", 2, 3, 1, "#3498DB", lambda: add(screen, "-")),
    ("1", 3, 0, 1, "#ECF0F1", lambda: add(screen, "1")),
    ("2", 3, 1, 1, "#ECF0F1", lambda: add(screen, "2")),
    ("3", 3, 2, 1, "#ECF0F1", lambda: add(screen, "3")),
    ("+", 3, 3, 1, "#3498DB", lambda: add(screen, "+")),
    ("0", 4, 0, 2, "#ECF0F1", lambda: add(screen, "0")), # 4,0,2 => row 4, column 0, column span 2
    (".", 4, 2, 1, "#ECF0F1", lambda: add(screen, ".")),
    ("=", 4, 3, 1, "#2ECC71", lambda: calculate(screen)),
]


window.mainloop()