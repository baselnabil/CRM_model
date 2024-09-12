from tkinter import ttk
from transaction_model import TRANSACTIONS
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import tkinter as tk



class TransactionsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Transactions Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=1, column=0, padx=20, pady=20, sticky='ew')


class AddTransaction(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.controller=controller
        self.transaction_type = ['Debt','Deposit']


        label = ttk.Label(self, text="Add Transactions Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        company_name_label = ttk.Label(self,text="Company Name",font=("Helvetica", 16, "bold"))
        company_name_label.grid(row=1, column=0, padx=20, pady=20)

        self.company_name_entry = ttk.Entry(self)
        self.company_name_entry.grid(row=1 ,column=1 ,padx=20,pady=20)


        transaction_type_label = ttk.Label(self, text="Choose Transactions Type", font=("Helvetica", 16, "bold"))
        transaction_type_label.grid(row=2 ,column=0 ,padx=20,pady=20)

        self.transaction_type_entry = ttk.Combobox(self,values=self.transaction_type)
        self.transaction_type_entry.grid(row=2, column=1, padx=20, pady=20)
        
        
        date_label = ttk.Label(self,text="Date",font=("Helvetica", 16, "bold"))
        date_label.grid(row=3, column=0, padx=20, pady=20)

        self.date_entry = DateEntry(self,date_pattern='yyyy-mm-dd' ,width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=3 ,column=1 ,padx=20,pady=20)

        
        transaction_amount_label = ttk.Label(self,text="Transaction Amount",font=("Helvetica", 16, "bold"))
        transaction_amount_label.grid(row=4, column=0, padx=20, pady=20)

        self.transaction_amount_entry = ttk.Entry(self)
        self.transaction_amount_entry.grid(row=4 ,column=1 ,padx=20,pady=20)

        
        submit_button = ttk.Button(self,text="Submit",command=self.add_transaction)
        submit_button.grid(row=5,column=1,padx=20,pady=20)

        
        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=5, column=0, padx=20, pady=20, sticky='ew')


    def add_transaction(self):
        company_name = self.company_name_entry.get()
        transacion_type = self.transaction_type_entry.get()
        date =self.date_entry.get()

        transaction_amount = self.transaction_amount_entry.get()
        
        if company_name and transacion_type and date and  transaction_amount:
            try:
                transaction=TRANSACTIONS(self.controller.connection)
                transaction.add_transaction(company_name , transacion_type , date , transaction_amount)
                messagebox.showinfo('success','Transaction Added successfully !!')
                self.clear_form()
            except Exception as err :
                messagebox.showerror(err,f'there is an error with this submetion {err}')
        else:
            messagebox.showwarning("Input Error", "Please enter a valid name.")
    def clear_form(self):
        self.company_name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.transaction_amount_entry.delete(0, tk.END)
        self.transaction_type_entry.delete(0, tk.END)

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class SearchTransaction(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.search_model = TRANSACTIONS(controller.connection)

        # Title Label
        label = ttk.Label(self, text="Search Transactions By Date", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Start Date Label and Entry
        search_label_start = ttk.Label(self, text="Start Date", font=("Helvetica", 16, "bold"))
        search_label_start.grid(row=1, column=0, padx=20, pady=20)

        self.search_entry_start = DateEntry(self, date_pattern='yyyy-mm-dd', width=12, background='darkblue', 
                                            foreground='white', borderwidth=2)
        self.search_entry_start.grid(row=1, column=1, padx=20, pady=20)

        # End Date Label and Entry
        search_label_end = ttk.Label(self, text="End Date", font=("Helvetica", 16, "bold"))
        search_label_end.grid(row=2, column=0, padx=20, pady=20)

        self.search_entry_end = DateEntry(self, date_pattern='yyyy-mm-dd', width=12, background='darkblue', 
                                          foreground='white', borderwidth=2)
        self.search_entry_end.grid(row=2, column=1, padx=20, pady=20)

        # Submit Button
        submit_button = ttk.Button(self, text="Search", command=self.search_by_date)
        submit_button.grid(row=3, column=1, padx=20, pady=20)

        # Result Frame (with Scrollbar)
        self.result_frame = ttk.Frame(self)
        self.result_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Add Scrollbar to the result frame
        self.canvas = tk.Canvas(self.result_frame)
        self.scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")


        save_button=ttk.Button(self,text='save to excel',command=self.save_output)
        save_button.grid(row=5,column=3,columnspan=1,padx=20,pady=20)

        # Back Button
        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky='ew')

    def search_by_date(self):
        start_date = self.search_entry_start.get()
        end_date = self.search_entry_end.get()

        if start_date and end_date:
            try:
                # Clear the previous search results
                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()

                # Search for transactions within the date range
                self.results = self.search_model.search_transaction(start_date, end_date)

                if self.results:
                    # Iterate through results and create labels for each transaction
                    for i, transaction in enumerate(self.results, start=1):
                        company_name = transaction[1]
                        transaction_type = transaction[2]
                        transaction_date = transaction[3]
                        transaction_amount = transaction[4]

                        transaction_info = (
                            f"Transaction {i}\n"
                            f"Company: {company_name}\n"
                            f"Type: {transaction_type}\n"
                            f"Date: {transaction_date}\n"
                            f"Amount: {transaction_amount}\n"
                            "------------------------"
                        )

                        # Create a label for each transaction and add it to the scrollable frame
                        transaction_label = ttk.Label(self.scrollable_frame, text=transaction_info, font=("Helvetica", 12))
                        transaction_label.pack(anchor="w", padx=10, pady=5)

                else:
                    messagebox.showinfo("No Results", "No transactions found in that date range.")
            except Exception as e:
                messagebox.showerror("Error", f"Error searching for transactions: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter both start and end dates.")
    def save_output(self):
        try:
            results = self.results
            if not results:
                messagebox.showwarning("No Data", "No data available to save.")
                return

            df = pd.DataFrame(results, columns=["Transaction", "Company", "Type", "Date", "Amount"])
            df.to_csv('data.csv', index=False)
            messagebox.showinfo("Success", "Data saved successfully to 'data.csv'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving data: {e}")
