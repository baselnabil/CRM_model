import tkinter as tk
from tkinter import ttk

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Configure rows and columns to control layout behavior
        self.grid_rowconfigure(0, weight=1)  # Padding row at the top
        self.grid_rowconfigure(1, weight=0)  # Title row
        self.grid_rowconfigure(2, weight=0)  # Username row
        self.grid_rowconfigure(3, weight=0)  # Password row
        self.grid_rowconfigure(4, weight=0)  # Button row
        self.grid_rowconfigure(5, weight=1)  # Padding row at the bottom
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Label for the login title
        label = ttk.Label(self, text="Login to CRM", font=("Helvetica", 18, "bold"))
        label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='n')

        # Username Entry
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # Password Entry
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        # Login Button
        login_button = ttk.Button(self, text="Login", command=self.check_login)
        login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="n")

        # Error message label (empty initially)
        self.error_label = ttk.Label(self, text="", foreground="red")
        self.error_label.grid(row=5, column=0, columnspan=2)

    def check_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            self.controller.show_frame("MainPage")
        else:
            self.error_label.config(text="Incorrect username or password")
