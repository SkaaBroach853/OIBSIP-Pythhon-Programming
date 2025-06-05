import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        unit = unit_var.get()

        if weight <= 0 or height <= 0:
            raise ValueError("Inputs must be positive numbers.")

        # Convert height to meters
        if unit == "feet":
            height = height * 0.3048
        elif unit == "inch":
            height = height * 0.0254
        # if unit is meter, no change needed

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"Your BMI is: {bmi}\nCategory: {category}",
            fg="blue"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")

# --- GUI Setup ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x360")
root.resizable(False, False)

tk.Label(root, text="BMI Calculator", font=("Helvetica", 18, "bold")).pack(pady=15)

# Weight Entry
tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12)).pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height Entry
tk.Label(root, text="Enter Height:", font=("Arial", 12)).pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Unit Dropdown
unit_var = tk.StringVar()
unit_var.set("meter")  # Default unit

tk.Label(root, text="Select Height Unit:", font=("Arial", 12)).pack()
unit_menu = tk.OptionMenu(root, unit_var, "meter", "feet", "inch")
unit_menu.config(font=("Arial", 10))
unit_menu.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"), command=calculate_bmi).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
