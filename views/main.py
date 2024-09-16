import tkinter as tk
from tkinter import ttk
from login_page import LoginPage
from main_page import MainPage
from customer_page import Addcustomer, DeleteCustomer, SearchCustomer
from transactions_page import TransactionsPage, AddTransaction, SearchTransaction
from sales_page import SalesPage
from customers_model import CustomerModel
from tkinter import messagebox

class CRMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRM Dashboard')
        self.geometry('700x600')
        self.resizable(False, False)

        # Database connection
        self.connection = CustomerModel.connection_db()
        if self.connection is None:
            messagebox.showerror("Database Error", "Could not connect to the database.")
            self.quit()

        # Apply ttk theme
        style = ttk.Style(self)
        style.theme_use('clam')

        # Customizing the style for buttons, frames, and labels
        style.configure('TFrame', background='#E0E0E0')
        style.configure('TLabel', background='#E0E0E0', font=('Helvetica', 16, 'bold'))
        style.configure('TButton', font=('Helvetica', 12), padding=10, background='#006699', foreground='white')
        style.map('TButton', background=[('active', '#004466')])

        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        self.frames = {}  # Dictionary to store the frames

        # Show the initial frame (Login Page)
        self.show_frame('LoginPage')

    def show_frame(self, page_name):
        """Show a frame for the given page name. Create the frame if it doesn't exist."""
        # If the frame is not already created, create it
        if page_name not in self.frames:
            frame = self.create_frame(page_name)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Raise the frame to the front
        frame = self.frames[page_name]
        frame.tkraise()

        # Adjust window size based on the page
        if page_name == 'Addcustomer':
            self.geometry('400x400')
        elif page_name == 'SearchTransaction':
            self.geometry('550x700')
        else:
            self.geometry('600x500')

    def create_frame(self, page_name):
        """Create a new frame based on the page name"""
        if page_name == 'LoginPage':
            return LoginPage(parent=self.container, controller=self)
        elif page_name == 'MainPage':
            return MainPage(parent=self.container, controller=self)
        elif page_name == 'Addcustomer':
            return Addcustomer(parent=self.container, controller=self)
        elif page_name == 'DeleteCustomer':
            return DeleteCustomer(parent=self.container, controller=self)
        elif page_name == 'SearchCustomer':
            return SearchCustomer(parent=self.container, controller=self)
        elif page_name == 'TransactionsPage':
            return TransactionsPage(parent=self.container, controller=self)
        elif page_name == 'SalesPage':
            return SalesPage(parent=self.container, controller=self)
        elif page_name == 'AddTransaction':
            return AddTransaction(parent=self.container, controller=self)
        elif page_name == 'SearchTransaction':
            return SearchTransaction(parent=self.container, controller=self)
        else:
            raise ValueError(f"Unknown page name: {page_name}")

if __name__ == "__main__":
    app = CRMApp()
    app.mainloop()
