import tkinter as tk
from tkinter import ttk
import subprocess
import sys

def open_first_gui():
    subprocess.Popen(["python", "Attendance.py"])

def on_submit():
    selected_option = var.get()
    if selected_option:
        subprocess.Popen(["python", "retriver.py", selected_option])
    else:
        print("Please select an option before submitting.")

root = tk.Tk()
root.title("Attendance retrieval")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))

var = tk.StringVar()

label = ttk.Label(root, text="Select an option:")
label.grid(row=0, column=0, padx=10, pady=10)

options = ["ICS211", "ICS212", "ICS213", "ICS214", "ICS215", "IMA211", "ISC211"]
option_menu = ttk.Combobox(root, textvariable=var, values=options)
option_menu.grid(row=0, column=1, padx=10, pady=10)
option_menu.set("Select Option")

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

open_first_button = ttk.Button(root, text="Add Attendance", command=open_first_gui)
open_first_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a Text widget to display the list
text_widget = tk.Text(root, width=40, height=10)
text_widget.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
