import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
      name = name_entry.get()
      day = int(day_entry.get())
      month = int(month_entry.get())
      year = int(year_entry.get())

      today = datetime.now()
      age = today.year - year

      if (today.month, today.day) < (month, day):
          age -= 1

      result_label.config(text=f"{name}, you are {age} years old.")
    except ValueError:
      result_label.config(text="Please enter valid numbers for day, month, and year.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x300")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Day (DD):").pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

tk.Label(root, text="Month (MM):").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Year (YYYY):").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()