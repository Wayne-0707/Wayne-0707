import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class SimpleGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple Form")

        # Variables
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.email = tk.StringVar()
        self.gender = tk.StringVar()
        self.course = tk.StringVar()

        # Initialize UI components
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="First Name").grid(row=0, column=0)
        tk.Entry(self.window, textvariable=self.first_name).grid(row=0, column=1)

        tk.Label(self.window, text="Last Name").grid(row=1, column=0)
        tk.Entry(self.window, textvariable=self.last_name).grid(row=1, column=1)

        tk.Label(self.window, text="Email Address").grid(row=2, column=0)
        tk.Entry(self.window, textvariable=self.email).grid(row=2, column=1)

        # Gender selection
        tk.Label(self.window, text="Gender").grid(row=3, column=0)
        tk.Radiobutton(self.window, text="Male", variable=self.gender, value="Male").grid(row=3, column=1)
        tk.Radiobutton(self.window, text="Female", variable=self.gender, value="Female").grid(row=3, column=2)
        tk.Radiobutton(self.window, text="Prefer not to say", variable=self.gender, value="Prefer not to say").grid(row=3, column=3)

        # Course selection
        tk.Label(self.window, text="Course").grid(row=4, column=0)
        self.course_combo = ttk.Combobox(self.window, textvariable=self.course, values=["BSCS", "BSIT", "BSIS", "BSEMC"])
        self.course_combo.grid(row=4, column=1)

        # Buttons
        tk.Button(self.window, text="Submit", command=self.submit).grid(row=5, column=0)
        tk.Button(self.window, text="Clear", command=self.clear).grid(row=5, column=1)

    def submit(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        gender = self.gender.get()
        course = self.course.get()

        if not first_name or not last_name or not email or not gender or not course:
            messagebox.showwarning("Warning", "Please fill out all fields!")
        else:
            messagebox.showinfo("Information", f'Name: {first_name} {last_name}\n Email: {email}\n Gender: {gender}\n Course: {course}')

    def clear(self):
        self.first_name.set("")
        self.last_name.set("")
        self.email.set("")
        self.gender.set("")
        self.course.set("")

if __name__ == "__main__":
    window = tk.Tk()
    app = SimpleGUI(window)
    window.mainloop()
