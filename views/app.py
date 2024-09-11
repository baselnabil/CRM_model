import tkinter as tk
from tkinter import ttk

class CRMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRM Dashboard')
        self.geometry('700x600')
        self.resizable(False, False)  # Make the window non-resizable

        # Apply ttk theme
        style = ttk.Style(self)
        style.theme_use('clam')  # You can try 'alt', 'default', 'classic'

        # Customizing the style for buttons, frames, and labels
        style.configure('TFrame', background='#E0E0E0')  # Light grey background for frames
        style.configure('TLabel', background='#E0E0E0', font=('Helvetica', 16, 'bold'))  # Styled labels
        style.configure('TButton', font=('Helvetica', 12), padding=10, background='#006699', foreground='white')
        style.map('TButton', background=[('active', '#004466')])  # Button changes color when hovered

        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        self.frames = {}
        for F in (LoginPage, MainPage, CustomerPage, TransactionsPage, SalesPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('LoginPage')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'LoginPage':
            self.geometry('600x300')  # Smaller size for the login page
        if page_name=='CustomerPage':
            self.geometry('400x600')
        else:
            self.geometry('600x300')  # Default size for the main CRM pages


class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Frame Styling
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Login Title
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
        # Simple authentication logic (for demonstration purposes)
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            self.controller.show_frame("MainPage")
        else:
            error_label = ttk.Label(self, text="Incorrect username or password", foreground="red")
            error_label.grid(row=6, column=0, padx=10, pady=10)

class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Layout
        title_label = ttk.Label(self, text="CRM Dashboard", font=("Helvetica", 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Column 1: Customers
        customers_frame = ttk.Frame(self)
        customers_frame.grid(row=1, column=0, padx=20, pady=20)
        ttk.Label(customers_frame, text="Customers").pack(pady=10)

        add_customer_button = ttk.Button(customers_frame, text="Add Customer", command=lambda: controller.show_frame('CustomerPage'))
        add_customer_button.pack(fill='x', pady=5)
        delete_customer_button = ttk.Button(customers_frame, text="Delete Customer")
        delete_customer_button.pack(fill='x', pady=5)
        search_customer_button = ttk.Button(customers_frame, text="Search Customer")
        search_customer_button.pack(fill='x', pady=5)

        # Column 2: Transactions
        transactions_frame = ttk.Frame(self)
        transactions_frame.grid(row=1, column=1, padx=20, pady=20)
        ttk.Label(transactions_frame, text="Transactions").pack(pady=10)

        add_transaction_button = ttk.Button(transactions_frame, text="Add Debt", command=lambda: controller.show_frame('TransactionsPage'))
        add_transaction_button.pack(fill='x', pady=5)
        remove_transaction_button = ttk.Button(transactions_frame, text="Remove Debt")
        remove_transaction_button.pack(fill='x', pady=5)
        search_transaction_button = ttk.Button(transactions_frame, text="Search Debt")
        search_transaction_button.pack(fill='x', pady=5)

        # Column 3: Sales
        sales_frame = ttk.Frame(self)
        sales_frame.grid(row=1, column=2, padx=20, pady=20)
        ttk.Label(sales_frame, text="Sales").pack(pady=10)

        add_sales_button = ttk.Button(sales_frame, text="Add Sales Record", command=lambda: controller.show_frame('SalesPage'))
        add_sales_button.pack(fill='x', pady=5)
        delete_sales_button = ttk.Button(sales_frame, text="Delete Sales Record")
        delete_sales_button.pack(fill='x', pady=5)
        view_sales_summary_button = ttk.Button(sales_frame, text="View Sales Summary")
        view_sales_summary_button.pack(fill='x', pady=5)

class CustomerPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Customer Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        user_laber = ttk.Label(self,text="Name",font=("Helvetica", 16, "bold"))
        user_laber.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

        user_laber = ttk.Entry(self, show="*")
        user_laber.grid(row=1, column=0, padx=20, pady=20)
        

        add_customer_btn = ttk.Button(self,text="Name")
        add_customer_btn.grid(row=1,column=1,padx=20,pady=20,sticky="ew")

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=2, column=0, padx=20, pady=20, sticky='ew')

class TransactionsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Transactions Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=1, column=0, padx=20, pady=20, sticky='ew')

class SalesPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Sales Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=1, column=0, padx=20, pady=20, sticky='ew')

if __name__ == "__main__":
    app = CRMApp()
    app.mainloop()
