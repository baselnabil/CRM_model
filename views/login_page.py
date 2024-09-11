import tkinter as tk
from tkinter import ttk

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Login to CRM")
        label.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        # Username Entry
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=2, column=0, padx=10, pady=10)

        # Password Entry
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=4, column=0, padx=10, pady=10)

        # Login Button
        login_button = ttk.Button(self, text="Login", command=self.check_login)
        login_button.grid(row=5, column=0, padx=10, pady=20)

    def check_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            self.controller.show_frame("MainPage")
        else:
            error_label = ttk.Label(self, text="Incorrect username or password", foreground="red")
            error_label.grid(row=6, column=0, padx=10, pady=10)
