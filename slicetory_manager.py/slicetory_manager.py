import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class SlicetoryManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slicetory Manager")
        
        # Form Title
        self.title_label = tk.Label(root, text="SLICETORY MANAGER", font=("Helvetica", 16))
        self.title_label.grid(row=0, columnspan=2, pady=10)

        # Date
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=1, column=0, sticky=tk.W)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)

        # Name of Product
        self.name_label = tk.Label(root, text="Name of Product")
        self.name_label.grid(row=2, column=0, sticky=tk.W)
        self.name_combobox = ttk.Combobox(root, values=["Cookies and Cream", "Chocolate Cookies", "Chocochips",
        "Specious Lotus Biscoff", "Green Matcha", "Caramelita", "Blueberry Yogurt", "Durian Palopo", "Strawberry",
        "Vanilla Regal", "Choco Mint", "Tiramissyou"])
        self.name_combobox.grid(row=2, column=1)

        # Initial Stock of Goods
        self.initial_stock_label = tk.Label(root, text="Initial Stock of Goods")
        self.initial_stock_label.grid(row=3, column=0, sticky=tk.W)
        self.initial_stock_entry = tk.Entry(root)
        self.initial_stock_entry.grid(row=3, column=1)
        

        # Incoming Goods
        self.incoming_goods_label = tk.Label(root, text="Incoming Goods")
        self.incoming_goods_label.grid(row=4, column=0, sticky=tk.W)
        self.incoming_goods_entry = tk.Entry(root)
        self.incoming_goods_entry.grid(row=4, column=1)

        # Outgoing Goods
        self.outgoing_goods_label = tk.Label(root, text="Outgoing Goods")
        self.outgoing_goods_label.grid(row=5, column=0, sticky=tk.W)
        self.outgoing_goods_entry = tk.Entry(root)
        self.outgoing_goods_entry.grid(row=5, column=1)

        # Price of Product
        self.price_label = tk.Label(root, text="Price of Product")
        self.price_label.grid(row=6, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=6, column=1)

        # Save Button
        self.save_button = tk.Button(root, text="Save", command=self.save_product)
        self.save_button.grid(row=7, columnspan=2, pady=10)

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def save_product(self):
        date = self.date_entry.get()
        name = self.name_combobox.get()
        initial_stock = self.initial_stock_entry.get()
        incoming_goods = self.incoming_goods_entry.get()
        outgoing_goods = self.outgoing_goods_entry.get()
        price = self.price_entry.get()

        
         # Validating date
        if not self.validate_date(date):
            messagebox.showerror("Error", "Date format is incorrect. Please use YYYY-MM-DD.")
            return

        # Validating that all fields are filled and numeric
        if not (date and name and initial_stock and incoming_goods and outgoing_goods and price):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if not (self.is_number(initial_stock) and self.is_number(incoming_goods) and self.is_number(outgoing_goods) and self.is_number(price)):
            messagebox.showerror("Error", "Please enter valid numeric values for stock and price")
            return

        # Convert numeric inputs to float
        initial_stock = float(initial_stock)
        incoming_goods = float(incoming_goods)
        outgoing_goods = float(outgoing_goods)
        price = float(price)

        # Calculate final stock
        final_stock = initial_stock + incoming_goods - outgoing_goods

        # Calculate total stock value
        total_value = final_stock * price

        # Display success message
        messagebox.showinfo("Success", f"Product {name} saved successfully!\n\nFinal Stock: {final_stock}\nTotal Stock Value: Rp {total_value:,.2f}")

        self.clear_entries()

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.name_combobox.set('')
        self.initial_stock_entry.delete(0, tk.END)
        self.incoming_goods_entry.delete(0, tk.END)
        self.outgoing_goods_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlicetoryManagerGUI(root)
    root.mainloop()