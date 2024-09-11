from tkinter import ttk

class SalesPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Sales Page", font=("Helvetica", 16, "bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        back_button = ttk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame('MainPage'))
        back_button.grid(row=1, column=0, padx=20, pady=20, sticky='ew')
