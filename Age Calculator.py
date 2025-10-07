import tkinter as tk
from datetime import datetime, date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years", fg="green")
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.", fg="red")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")

tk.Label(root, text="Enter Date of Birth", font=("Arial", 14)).pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Day: ").grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(form_frame)
day_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Month: ").grid(row=1, column=0, padx=5, pady=5)
month_entry = tk.Entry(form_frame)
month_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Year: ").grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(form_frame)
year_entry.grid(row=2, column=1)

calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age, font=("Arial", 12))
calc_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()


