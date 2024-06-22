import tkinter as tk
from tkinter import messagebox
import random

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#f00")
        self.root.title("Billing System")
        title = tk.Label(self.root, text="Billing System", bd=12, relief=tk.RIDGE, font=("Arial Black", 20), bg="#A569BD", fg="white").pack(fill=tk.X)
        
        # Variables
        self.init_variables()

        # Customer details frame
        self.customer_details_frame()

        # Items frames
        self.items_frame()

        # Bill area
        self.bill_area()

        # Billing menu
        self.billing_menu()

        # Initialize bill area with intro text
        self.intro()

    def init_variables(self):
        self.Chowmein = tk.IntVar()
        self.Fried_Rice = tk.IntVar()
        self.Manchurian = tk.IntVar()
        self.Cheese_Chilly = tk.IntVar()
        self.Honey_Chilly_Cauliflower = tk.IntVar()
        self.Honey_Chilly_Potatoes = tk.IntVar()
        self.Pasta = tk.IntVar()

        self.Dal_Makhani = tk.IntVar()
        self.Paneer_Butter_Masala = tk.IntVar()
        self.Malai_Kofta = tk.IntVar()
        self.Kadhai_Paneer = tk.IntVar()
        self.Plain_Roti = tk.IntVar()
        self.Butter_Naan = tk.IntVar()
        self.Tandoori_Roti = tk.IntVar()

        self.Vanilla_Icecream = tk.IntVar()
        self.Strawberry_Icecream = tk.IntVar()
        self.Ras_Malai = tk.IntVar()
        self.Gulab_Jamun = tk.IntVar()
        self.Kheer = tk.IntVar()
        self.Custard = tk.IntVar()
        self.Brownie_Sizzler = tk.IntVar()

        self.total_Starters = tk.StringVar()
        self.total_Maincourse = tk.StringVar()
        self.total_Desserts = tk.StringVar()
        self.total_Tax = tk.StringVar()
        self.c_name = tk.StringVar()
        self.bill_no = tk.StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = tk.StringVar()

    def customer_details_frame(self):
        details = tk.LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white", relief=tk.GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = tk.Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=0, padx=15)
        cust_entry = tk.Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)
        contact_name = tk.Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=2, padx=10)
        contact_entry = tk.Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)
        bill_name = tk.Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=4, padx=10)
        bill_entry = tk.Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

    def items_frame(self):
        self.create_frame("Starters", 5, 180, [
            ("Chowmein", self.Chowmein),
            ("Fried Rice", self.Fried_Rice),
            ("Manchurian", self.Manchurian),
            ("Cheese Chilly", self.Cheese_Chilly),
            ("Honey Chilly Cauliflower", self.Honey_Chilly_Cauliflower),
            ("Honey Chilly Potatoes", self.Honey_Chilly_Potatoes),
            ("Pasta", self.Pasta)
        ])
        self.create_frame("Main Course", 340, 180, [
            ("Dal Makhani", self.Dal_Makhani),
            ("Paneer Butter Masala", self.Paneer_Butter_Masala),
            ("Malai Kofta", self.Malai_Kofta),
            ("Kadhai Paneer", self.Kadhai_Paneer),
            ("Plain Roti", self.Plain_Roti),
            ("Butter Naan", self.Butter_Naan),
            ("Tandoori Roti", self.Tandoori_Roti)
        ])
        self.create_frame("Desserts", 677, 180, [
            ("Vanilla Icecream", self.Vanilla_Icecream),
            ("Strawberry Icecream", self.Strawberry_Icecream),
            ("Ras Malai", self.Ras_Malai),
            ("Gulab Jamun", self.Gulab_Jamun),
            ("Kheer", self.Kheer),
            ("Custard", self.Custard),
            ("Brownie Sizzler", self.Brownie_Sizzler)
        ])

    def create_frame(self, title, x, y, items):
        frame = tk.LabelFrame(self.root, text=title, font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=tk.GROOVE, bd=10)
        frame.place(x=x, y=y, height=380, width=325)
        for i, (item, var) in enumerate(items):
            tk.Label(frame, text=item, font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=i, column=0, pady=11)
            tk.Entry(frame, borderwidth=2, width=15, textvariable=var).grid(row=i, column=1, padx=10)

    def bill_area(self):
        billarea = tk.Frame(self.root, bd=10, relief=tk.GROOVE, bg="#E5B4F3")
        billarea.place(x=1010, y=188, width=330, height=372)
        bill_title = tk.Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=tk.GROOVE, bg="#E5B4F3", fg="#6C3483").pack(fill=tk.X)
        scrol_y = tk.Scrollbar(billarea, orient=tk.VERTICAL)
        self.txtarea = tk.Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=tk.BOTH, expand=1)

    def billing_menu(self):
        billing_menu = tk.LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12), relief=tk.GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)
        tk.Label(billing_menu, text="Cost Of Starters ", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=0, column=0)
        tk.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_Starters).grid(row=0, column=1, padx=10, pady=7)
        tk.Label(billing_menu, text="Cost Of Maincourse ", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=1, column=0)
        tk.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_Maincourse).grid(row=1, column=1, padx=10, pady=7)
        tk.Label(billing_menu, text="Cost Of Desserts ", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=2, column=0)
        tk.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_Desserts).grid(row=2, column=1, padx=10, pady=7)

        button_frame = tk.Frame(billing_menu, bd=7, relief=tk.GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)
        tk.Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=self.total).grid(row=0, column=0, padx=12)
        tk.Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=self.clear).grid(row=0, column=1, padx=10, pady=6)
        tk.Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=self.exit_app).grid(row=0, column=2, padx=10, pady=6)

    def total(self):
        self.calculate_totals()
        self.update_bill_area()

    def calculate_totals(self):
        total_Starters_Price = (self.Chowmein.get() * 50) + (self.Fried_Rice.get() * 60) + (self.Manchurian.get() * 70) + (self.Cheese_Chilly.get() * 80) + (self.Honey_Chilly_Cauliflower.get() * 90) + (self.Honey_Chilly_Potatoes.get() * 70) + (self.Pasta.get() * 70)
        total_Maincourse_Price = (self.Dal_Makhani.get() * 90) + (self.Paneer_Butter_Masala.get() * 100) + (self.Malai_Kofta.get() * 110) + (self.Kadhai_Paneer.get() * 120) + (self.Plain_Roti.get() * 15) + (self.Butter_Naan.get() * 20) + (self.Tandoori_Roti.get() * 25)
        total_Desserts_Price = (self.Vanilla_Icecream.get() * 50) + (self.Strawberry_Icecream.get() * 60) + (self.Ras_Malai.get() * 70) + (self.Gulab_Jamun.get() * 50) + (self.Kheer.get() * 70) + (self.Custard.get() * 60) + (self.Brownie_Sizzler.get() * 80)
        self.total_Starters.set("Rs. " + str(total_Starters_Price))
        self.total_Maincourse.set("Rs. " + str(total_Maincourse_Price))
        self.total_Desserts.set("Rs. " + str(total_Desserts_Price))
        total_Price = total_Starters_Price + total_Maincourse_Price + total_Desserts_Price
        Tax = round(total_Price * 0.05)
        self.total_Tax.set("Rs. " + str(Tax))
        self.Total_Bill = "Rs. " + str(total_Price + Tax)

    def update_bill_area(self):
        self.txtarea.delete('1.0', tk.END)
        self.intro()
        self.txtarea.insert(tk.END, "\n=====================================")
        self.txtarea.insert(tk.END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(tk.END, f"\nPhone Number : {self.phone.get()}")
        self.txtarea.insert(tk.END, "\n=====================================")
        self.txtarea.insert(tk.END, "\nProduct\t\tQTY\tPrice")
        self.txtarea.insert(tk.END, "\n=====================================")
        self.print_items("Chowmein", self.Chowmein.get(), 50)
        self.print_items("Fried Rice", self.Fried_Rice.get(), 60)
        self.print_items("Manchurian", self.Manchurian.get(), 70)
        self.print_items("Cheese Chilly", self.Cheese_Chilly.get(), 80)
        self.print_items("Honey Chilly Cauliflower", self.Honey_Chilly_Cauliflower.get(), 90)
        self.print_items("Honey Chilly Potatoes", self.Honey_Chilly_Potatoes.get(), 70)
        self.print_items("Pasta", self.Pasta.get(), 70)
        self.print_items("Dal Makhani", self.Dal_Makhani.get(), 90)
        self.print_items("Paneer Butter Masala", self.Paneer_Butter_Masala.get(), 100)
        self.print_items("Malai Kofta", self.Malai_Kofta.get(), 110)
        self.print_items("Kadhai Paneer", self.Kadhai_Paneer.get(), 120)
        self.print_items("Plain Roti", self.Plain_Roti.get(), 15)
        self.print_items("Butter Naan", self.Butter_Naan.get(), 20)
        self.print_items("Tandoori Roti", self.Tandoori_Roti.get(), 25)
        self.print_items("Vanilla Icecream", self.Vanilla_Icecream.get(), 50)
        self.print_items("Strawberry Icecream", self.Strawberry_Icecream.get(), 60)
        self.print_items("Ras Malai", self.Ras_Malai.get(), 70)
        self.print_items("Gulab Jamun", self.Gulab_Jamun.get(), 50)
        self.print_items("Kheer", self.Kheer.get(), 70)
        self.print_items("Custard", self.Custard.get(), 60)
        self.print_items("Brownie Sizzler", self.Brownie_Sizzler.get(), 80)
        self.txtarea.insert(tk.END, "\n-------------------------------------")
        self.txtarea.insert(tk.END, f"\nTotal Tax :\t\t{self.total_Tax.get()}")
        self.txtarea.insert(tk.END, f"\nTotal Bill :\t\t{self.Total_Bill}")
        self.txtarea.insert(tk.END, "\n-------------------------------------")
        self.save_bill()

    def print_items(self, item, qty, price):
        if qty > 0:
            self.txtarea.insert(tk.END, f"\n{item}\t\t{qty}\t{price * qty}")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', tk.END)
            with open("bills/" + str(self.bill_no.get()) + ".txt", "w") as f:
                f.write(self.bill_data)
            messagebox.showinfo("Saved", f"Bill No.: {self.bill_no.get()} saved successfully.")
        else:
            return

    def clear(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear the data?")
        if op > 0:
            self.reset_fields()
            self.intro()
        else:
            return

    def reset_fields(self):
        self.c_name.set("")
        self.phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.Chowmein.set(0)
        self.Fried_Rice.set(0)
        self.Manchurian.set(0)
        self.Cheese_Chilly.set(0)
        self.Honey_Chilly_Cauliflower.set(0)
        self.Honey_Chilly_Potatoes.set(0)
        self.Pasta.set(0)
        self.Dal_Makhani.set(0)
        self.Paneer_Butter_Masala.set(0)
        self.Malai_Kofta.set(0)
        self.Kadhai_Paneer.set(0)
        self.Plain_Roti.set(0)
        self.Butter_Naan.set(0)
        self.Tandoori_Roti.set(0)
        self.Vanilla_Icecream.set(0)
        self.Strawberry_Icecream.set(0)
        self.Ras_Malai.set(0)
        self.Gulab_Jamun.set(0)
        self.Kheer.set(0)
        self.Custard.set(0)
        self.Brownie_Sizzler.set(0)
        self.total_Starters.set("")
        self.total_Maincourse.set("")
        self.total_Desserts.set("")
        self.total_Tax.set("")

    def intro(self):
        self.txtarea.delete('1.0', tk.END)
        self.txtarea.insert(tk.END, "\tWelcome to Our Restaurant\n")
        self.txtarea.insert(tk.END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(tk.END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(tk.END, f"\nPhone Number: {self.phone.get()}")
        self.txtarea.insert(tk.END, "\n=====================================")
        self.txtarea.insert(tk.END, "\nProduct\t\tQTY\tPrice")
        self.txtarea.insert(tk.END, "\n=====================================")

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

root = tk.Tk()
app = BillApp(root)
root.mainloop()
