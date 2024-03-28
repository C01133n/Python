import tkinter as tk
from tkinter import messagebox
import math

def calculate_square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        result_label.config(text=f"The square root of {number} is {result:.4f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Square Root Calculator")

# Create widgets
label = tk.Label(root, text="Enter a number:")
entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate", command=calculate_square_root)
result_label = tk.Label(root, text="")

# Place widgets using grid layout
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
