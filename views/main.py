import tkinter as tk
from tkinter import ttk
from login_page import LoginPage
from main_page import MainPage
from customer_page import Addcustomer
from customer_page import DeleteCustomer
from customer_page import SearchCustomer
from transactions_page import TransactionsPage
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

        self.frames = {}
        for F in (LoginPage, MainPage, Addcustomer, TransactionsPage, SalesPage,DeleteCustomer,SearchCustomer):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('LoginPage')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'Addcustomer':
            self.geometry('400x400')  # Smaller size for the login page
        else:
            self.geometry('600x500')  # Default size for main pages

if __name__ == "__main__":
    app = CRMApp()
    app.mainloop()

