import tkinter as tk

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

window.mainloop()