from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from customers_model import CustomerModel
class Addcustomer(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Customer Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # Name
        name_label = ttk.Label(self, text="Name", font=("Helvetica", 16, "bold"))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self)  # Changed to self to access in submit_customer
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email
        email_label = ttk.Label(self, text="Email", font=("Helvetica", 16, "bold"))
        email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        # Company
        company_label = ttk.Label(self, text="Company", font=("Helvetica", 16, "bold"))
        company_label.grid(row=3, column=0, padx=10, pady=10)
        self.company_entry = ttk.Entry(self)
        self.company_entry.grid(row=3, column=1, padx=10, pady=10)

        # Address
        address_label = ttk.Label(self, text="Address", font=("Helvetica", 16, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=10)
        self.address_entry = ttk.Entry(self)
        self.address_entry.grid(row=4, column=1, padx=10, pady=10)

        # Phone
        phone_label = ttk.Label(self, text="Phone", font=("Helvetica", 16, "bold"))
        phone_label.grid(row=5, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(self)
        self.phone_entry.grid(row=5, column=1, padx=10, pady=10)

        # Submit Button
        submit_button = ttk.Button(self, text="Submit", command=self.submit_customer)
        submit_button.grid(row=6, column=1, padx=20, pady=20, columnspan=2, sticky='ew')

        # Back Button
        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=6, column=0, padx=20, pady=20, sticky='ew')

    def submit_customer(self):
        name = self.name_entry.get()
        company = self.company_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()

        if name and company and email and address and phone:
            try:
                customer_model = CustomerModel(self.controller.connection)  # Using the existing connection
                customer_model.create_customer(name, company, email, address, phone)
                messagebox.showinfo("Success", "Customer added successfully!")
                self.clear_form()  # Optional: clear form after successful submission
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add customer: {e}")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.company_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)



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



class SearchCustomer(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer_model = CustomerModel(controller.connection)  # Initialize CustomerModel with connection

        label = ttk.Label(self, text="Customer Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        search_label = ttk.Label(self, text='Search By Name', font=('Helvetica', 16, 'bold'))
        search_label.grid(row=1, column=0, padx=10, pady=10)
        self.search_entry = ttk.Entry(self)  # Use self.search_entry to access value in search_customer
        self.search_entry.grid(row=1, column=1, padx=10, pady=10)

        search_button = ttk.Button(self, text='Search', command=self.search_customer)
        search_button.grid(row=1, column=2, padx=10, pady=10)

        # Label to display results
        self.result_label = ttk.Label(self, text="", font=('Helvetica', 12))
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Back Button
        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=6, column=0, padx=20, pady=20, sticky='ew')

    def search_customer(self):
        name = self.search_entry.get().strip()

        if name:
            try:
                results = self.customer_model.search_customer(name)
                if results:
                    customer = results[0]
                    display_text = f"Name: {customer[1]}, Email: {customer[2]}, Company: {customer[3]}, Address: {customer[4]}, Phone: {customer[5]}"
                    self.result_label.config(text=display_text)
                else:
                    messagebox.showinfo("No Results", "No customer found with that name.")
                    self.result_label.config(text="")
            except Exception as e:
                messagebox.showerror("Error", f"Error searching for customer: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid name.")