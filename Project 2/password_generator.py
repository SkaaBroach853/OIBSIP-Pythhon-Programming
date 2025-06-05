import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=var_symbols).pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result field
result_entry = tk.Entry(root, font=("Arial", 14), justify="center")
result_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
