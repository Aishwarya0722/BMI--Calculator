
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Invalid input: weight and height must be positive numbers.")
        bmi = weight / (height ** 2)
        result = f"BMI: {bmi:.2f}\n"
        if bmi < 18.5:
            result += "Category: Underweight"
        elif 18.5 <= bmi < 24.9:
            result += "Category: Normal weight"
        elif 25 <= bmi < 29.9:
            result += "Category: Overweight"
        else:
            result += "Category: Obesity"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Weight (kg):", bg="#f0f0f0").pack(pady=(10, 0))
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (m):", bg="#f0f0f0").pack(pady=(10, 0))
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
label_result.pack()

root.mainloop()
