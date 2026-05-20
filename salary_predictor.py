import tkinter as tk
from tkinter import messagebox
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression

salary_data = {
    "YearsExperience": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
    "Salary": [20000, 35000, 45000, 50000, 65000, 70000, 75000, 80000, 85000, 100000]
}
df = pd.DataFrame(salary_data)

x_vals = df[["YearsExperience"]]
y_vals = df[["Salary"]]

salary_model = LinearRegression()
salary_model.fit(x_vals,y_vals)

def predict_salary():  # This function is triggered by the button click in Tkinter UI
    try:
        user_input = entry.get().strip()
        years_exp = float(user_input)
        input_array = np.array([[years_exp]])
        predicted = salary_model.predict(input_array)
        final_salary = int(predicted.item())
        result_label.config(text = f"Predicted Salary: Rs.{final_salary}")
    except ValueError: messagebox.showerror("Error", "Please enter a valid number!")

window = tk.Tk()
window.title("Salary Predictor")
window.geometry("420x300")
window.resizable(False, False)

title_label = tk.Label(window, text="Salary Predictor", font = ("Arial", 18, "bold"))
title_label.pack(pady=15)

input_label = tk.Label(window, text="Enter Years of Experience:")
input_label.pack()

entry = tk.Entry(window, font=("Arial", 12))
entry.pack()

predict_btn = tk.Button(window, text="Predict Salary", command=predict_salary)
predict_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="green")
result_label.pack(pady=20)

window.mainloop()
