from tkinter import ttk

class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = ttk.Label(self, text="CRM Dashboard", font=("Helvetica", 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Customers Section
        customers_frame = ttk.Frame(self)
        customers_frame.grid(row=1, column=0, padx=20, pady=20)
        ttk.Label(customers_frame, text="Customers").pack(pady=10)

        add_customer_button = ttk.Button(customers_frame, text="Add Customer", command=lambda: controller.show_frame('Addcustomer'))
        add_customer_button.pack(fill='x', pady=5)
        delete_customer_button = ttk.Button(customers_frame, text="Delete Customer",command=lambda:controller.show_frame('DeleteCustomer'))
        delete_customer_button.pack(fill='x', pady=5)
        search_customer_button = ttk.Button(customers_frame, text="Search Customer",command=lambda:controller.show_frame('SearchCustomer'))
        search_customer_button.pack(fill='x', pady=5)

        # Transactions Section
        transactions_frame = ttk.Frame(self)
        transactions_frame.grid(row=1, column=1, padx=20, pady=20)
        ttk.Label(transactions_frame, text="Transactions").pack(pady=10)

        add_transaction_button = ttk.Button(transactions_frame, text="Add Debt", command=lambda: controller.show_frame('TransactionsPage'))
        add_transaction_button.pack(fill='x', pady=5)
        remove_transaction_button = ttk.Button(transactions_frame, text="Remove Debt")
        remove_transaction_button.pack(fill='x', pady=5)
        search_transaction_button = ttk.Button(transactions_frame, text="Search Debt")
        search_transaction_button.pack(fill='x', pady=5)

        # Sales Section
        sales_frame = ttk.Frame(self)
        sales_frame.grid(row=1, column=2, padx=20, pady=20)
        ttk.Label(sales_frame, text="Sales").pack(pady=10)

        add_sales_button = ttk.Button(sales_frame, text="Add Sales Record", command=lambda: controller.show_frame('SalesPage'))
        add_sales_button.pack(fill='x', pady=5)
        delete_sales_button = ttk.Button(sales_frame, text="Delete Sales Record")
        delete_sales_button.pack(fill='x', pady=5)
        view_sales_summary_button = ttk.Button(sales_frame, text="View Sales Summary")
        view_sales_summary_button.pack(fill='x', pady=5)
