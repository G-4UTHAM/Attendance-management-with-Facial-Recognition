import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def on_submit():
    selected_option = var.get()
    if selected_option:
        subprocess.Popen(["python", "main.py", selected_option])
    else:
        messagebox.showerror("Error", "Please select an option from the drop-down menu.")

def open_second_gui():
    subprocess.Popen(["python", "second_gui.py"])

root = tk.Tk()
root.title("Add Attendance")

# Create a custom style for the application
custom_style = ttk.Style()
custom_style.configure("TButton", foreground="black", background="blue", font=("Helvetica", 12))
custom_style.configure("TLabel", font=("Helvetica", 14))
custom_style.configure("TCombobox", font=("Helvetica", 12))

var = tk.StringVar()

label = ttk.Label(root, text="Select an option:")
label.grid(row=0, column=0, padx=10, pady=10)

options = ["ICS211", "ICS212", "ICS213", "ICS214", "ICS215", "IMA211", "ISC211"]
option_menu = ttk.Combobox(root, textvariable=var, values=options)
option_menu.grid(row=0, column=1, padx=10, pady=10)
option_menu.set("Select Option")

submit_button = ttk.Button(root, text="Submit", command=on_submit, style="TButton")
submit_button.grid(row=1, column=0, padx=10, pady=10)

open_second_button = ttk.Button(root, text="Attendance Checker", command=open_second_gui, style="TButton")
open_second_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
