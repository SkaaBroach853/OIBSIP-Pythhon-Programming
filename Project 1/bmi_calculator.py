import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        result = f"BMI: {bmi:.2f}\n"

        if bmi < 18.5:
            result += "Category: Underweight"
        elif 18.5 <= bmi < 24.9:
            result += "Category: Normal weight"
        elif 25 <= bmi < 29.9:
            result += "Category: Overweight"
        else:
            result += "Category: Obese"

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for weight and height.")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

tk.Label(root, text="BMI Calculator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
