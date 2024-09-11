from tkinter import ttk
from customers_model import CustomerModel
from db_connection import DB
from tkinter import messagebox

class Addcustomer(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Customer Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # Name
        name_label = ttk.Label(self, text="Name", font=("Helvetica", 16, "bold"))
        name_label.grid(row=1, column=0, padx=10, pady=10)

        name_entry = ttk.Entry(self)
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email
        email_label = ttk.Label(self, text="Email", font=("Helvetica", 16, "bold"))
        email_label.grid(row=2, column=0, padx=10, pady=10)

        email_entry = ttk.Entry(self)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        # Company
        company_label = ttk.Label(self, text="Company", font=("Helvetica", 16, "bold"))
        company_label.grid(row=3, column=0, padx=10, pady=10)

        company_entry = ttk.Entry(self)
        company_entry.grid(row=3, column=1, padx=10, pady=10)

        # Address
        address_label = ttk.Label(self, text="Address", font=("Helvetica", 16, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=10)

        address_entry = ttk.Entry(self)
        address_entry.grid(row=4, column=1, padx=10, pady=10)

        # Phone
        phone_label = ttk.Label(self, text="Phone", font=("Helvetica", 16, "bold"))
        phone_label.grid(row=5, column=0, padx=10, pady=10)

        phone_entry = ttk.Entry(self)
        phone_entry.grid(row=5, column=1, padx=10, pady=10)


        # submit Button

        submit_button = ttk.Button(self,text="Submit",command=None)
        submit_button.grid(row=6,column=1,padx=20,pady=20,columnspan=2,sticky='ew')

        # Back Button
        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=6, column=0, padx=20, pady=20, sticky='ew')
class DeleteCustomer(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

    
        label = ttk.Label(self,text="Delete Customer", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)


        delete_label = ttk.Label(self,text='Delete By Name',font=('Helvetica',16,'bold'))
        delete_label.grid(row=1,column=0,padx=10,pady=10)

        delete_entry = ttk.Entry(self)
        delete_entry.grid(row=1,column=1,padx=10,pady=10)


        delete_button=ttk.Button(self,text='Enter')
        delete_button.grid(row=1,column=2,padx=10,pady=10)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=6, column=0, padx=20, pady=20, sticky='ew')


class AddCustomer(ttk.Frame):
    # Your AddCustomer class remains the same
    pass

class DeleteCustomer(ttk.Frame):
    # Your DeleteCustomer class remains the same
    pass

class SearchCustomer(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.customer_model = CustomerModel()  # Initialize CustomerModel

        label = ttk.Label(self, text="Customer Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        search_label = ttk.Label(self, text='Search By Name', font=('Helvetica', 16, 'bold'))
        search_label.grid(row=1, column=0, padx=10, pady=10)

        self.search_entry = ttk.Entry(self)  # Use self.search_entry to access the value in the method
        self.search_entry.grid(row=1, column=1, padx=10, pady=10)

        search_button = ttk.Button(self, text='Search', command=self.search_customer)  # Call search_customer method
        search_button.grid(row=1, column=2, padx=10, pady=10)

        # Label to display results
        self.result_label = ttk.Label(self, text="", font=('Helvetica', 12))
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=6, column=0, padx=20, pady=20, sticky='ew')

