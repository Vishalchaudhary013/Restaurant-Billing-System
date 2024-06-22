from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#f00")
        self.root.title("Billing System")
        title=Label(self.root,text="Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.Chowmein=IntVar()
        self.Fried_Rice=IntVar()
        self.Manchurian=IntVar()
        self.Cheese_Chilly=IntVar()
        self.Honey_Chilly_Cauliflower=IntVar()
        self.Honey_Chilly_Potatoes=IntVar()
        self.Pasta=IntVar()

        self.Dal_Makhani=IntVar()
        self.Paneer_Butter_Masala=IntVar()
        self.Malai_Kofta=IntVar()
        self.Kadhai_Paneer=IntVar()
        self.Plain_Roti=IntVar()
        self.Butter_Naan=IntVar()
        self.Tandoori_Roti=IntVar()

        self.Vanilla_Icecream=IntVar()
        self.Strawberry_Icecream=IntVar()
        self.Ras_Malai=IntVar()
        self.Gulab_Jamun=IntVar()
        self.Kheer=IntVar()
        self.Custard=IntVar()
        self.Brownie_Sizzler=IntVar()

        self.total_Starters=StringVar()
        self.total_Maincourse=StringVar()
        self.total_Desserts=StringVar()
        self.total_Tax=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)

        #=======================================Starters=================================================================
        Starters=LabelFrame(self.root,text="Starters",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        Starters.place(x=5,y=180,height=380,width=325)
        
        item1=Label(Starters,text="Chowmein",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Chowmein).grid(row=0,column=1,padx=10)

        item2=Label(Starters,text="Fried Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Fried_Rice).grid(row=1,column=1,padx=10)

        item3=Label(Starters,text="Manchurian",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Manchurian).grid(row=2,column=1,padx=10)

        item4=Label(Starters,text="Cheese Chilly",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Cheese_Chilly).grid(row=3,column=1,padx=10)

        item5=Label(Starters,text="Honey Chilly Cauliflower",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Honey_Chilly_Cauliflower).grid(row=4,column=1,padx=10)

        item6=Label(Starters,text="Honey Chilly Potatoes",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Honey_Chilly_Potatoes).grid(row=5,column=1,padx=10)

        item7=Label(Starters,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(Starters,borderwidth=2,width=15,textvariable=self.Pasta).grid(row=6,column=1,padx=10)


    
        #===================================Main Course=====================================================================================
        Main_Course=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        Main_Course.place(x=340,y=180,height=380,width=325)

        item8=Label(Main_Course,text="Dal Makhani",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Dal_Makhani).grid(row=0,column=1,padx=10)

        item9=Label(Main_Course,text="Paneer Butter Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Paneer_Butter_Masala).grid(row=1,column=1,padx=10)

        item10=Label(Main_Course,text="Malai Kofta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Malai_Kofta).grid(row=2,column=1,padx=10)

        item11=Label(Main_Course,text="Kadhai Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Kadhai_Paneer).grid(row=3,column=1,padx=10)

        item12=Label(Main_Course,text="Plain Roti",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Plain_Roti).grid(row=4,column=1,padx=10)

        item13=Label(Main_Course,text="Butter Naan",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Butter_Naan).grid(row=5,column=1,padx=10)

        item14=Label(Main_Course,text="Tandoori Roti",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.Tandoori_Roti).grid(row=6,column=1,padx=10)

        #========================================Desserts===============================================================================
        Desserts=LabelFrame(self.root,text="Desserts",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        Desserts.place(x=677,y=180,height=380,width=325)

        item15=Label(Desserts,text="Vanilla Icecream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Vanilla_Icecream).grid(row=0,column=1,padx=10)

        item16=Label(Desserts,text="Strawberry Icecream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Strawberry_Icecream).grid(row=1,column=1,padx=10)

        item17=Label(Desserts,text="Ras Malai",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Ras_Malai).grid(row=2,column=1,padx=10)

        item18=Label(Desserts,text="Gulab Jamun",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Gulab_Jamun).grid(row=3,column=1,padx=10)

        item19=Label(Desserts,text="Kheer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Kheer).grid(row=4,column=1,padx=10)

        item20=Label(Desserts,text="Custard",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Custard).grid(row=5,column=1,padx=10)

        item21=Label(Desserts,text="Brownie Sizzler",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(Desserts,borderwidth=2,width=15,textvariable=self.Brownie_Sizzler).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summary",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_Starters=Label(billing_menu,text="Cost Of Chinese ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_Starters_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_Starters).grid(row=0,column=1,padx=10,pady=7)
        
        total_Maincourse=Label(billing_menu,text="Cost Of Maincourse ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_Maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_Maincourse).grid(row=1,column=1,padx=10,pady=7)

        total_Desserts=Label(billing_menu,text="Cost Of Desserts ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_Desserts_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_Desserts).grid(row=2,column=1,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.Ch=self.Chowmein.get()*160
    self.FR=self.Fried_Rice.get()*180
    self.MA=self.Manchurian.get()*200
    self.CC=self.Cheese_Chilly.get()*240
    self.HCC=self.Honey_Chilly_Cauliflower.get()*160
    self.HCP=self.Honey_Chilly_Potatoes.get()*140
    self.Pas=self.Pasta.get()*120

    total_Starters_price=(
                self.Ch+
                self.FR+
                self.MA+
                self.CC+
                self.HCC+
                self.HCP+
                self.Pas)          
    self.total_Starters.set(str(total_Starters_price)+" Rs")

    self.DM=self.Dal_Makhani.get()*130
    self.PBM=self.Paneer_Butter_Masala.get()*160
    self.MK=self.Malai_Kofta.get()*150
    self.KP=self.Kadhai_Paneer.get()*160
    self.PR=self.Plain_Roti.get()*10
    self.BN=self.Butter_Naan.get()*30
    self.TR=self.Tandoori_Roti.get()*15

    total_Maincourse_price=(
        self.DM+
        self.PBM+
        self.MK+
        self.KP+
        self.PR+
        self.BN+
        self.TR)
        
    self.total_Maincourse.set(str(total_Maincourse_price)+" Rs")


    self.VI=self.Vanilla_Icecream.get()*40
    self.SI=self.Strawberry_Icecream.get()*40
    self.RM=self.Ras_Malai.get()*60
    self.GJ=self.Gulab_Jamun.get()*50
    self.Kh=self.Kheer.get()*60
    self.Cu=self.Custard.get()*60
    self.BS=self.Brownie_Sizzler.get()*80
    
    total_Desserts_price=(
        self.VI+
        self.SI+
        self.RM+
        self.GJ+
        self.Kh+
        self.Cu+
        self.BS)
        
    self.total_Desserts.set(str(total_Desserts_price)+" Rs")
    
    
    self.total_all_bill=(total_Starters_price+
                total_Maincourse_price+
                total_Desserts_price)

    self.total_Tax=(round(self.total_all_bill*0.18,3))
                
    self.total_all_bil=str(self.total_all_bill+self.total_Tax)+" Rs"
    
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO OUR RESTAURANT\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Chowmein.get()!=0:
        self.txtarea.insert(END,f"Chowmein\t\t {self.Chowmein.get()}\t{self.Ch}\n")
    if self.Fried_Rice.get()!=0:
        self.txtarea.insert(END,f"Fried Rice\t\t {self.Fried_Rice.get()}\t{self.FR}\n")
    if self.Manchurian.get()!=0:
        self.txtarea.insert(END,f"Manchurian\t\t {self.Manchurian.get()}\t{self.MA}\n")
    if self.Cheese_Chilly.get()!=0:
        self.txtarea.insert(END,f"Cheese Chilly\t\t {self.Cheese_Chilly.get()}\t{self.CC}\n")
    if self.Honey_Chilly_Cauliflower.get()!=0:
        self.txtarea.insert(END,f"Honey Chilly Cauliflower\t\t {self.Honey_Chilly_Cauliflower.get()}\t{self.HCC}\n")
    if self.Honey_Chilly_Potatoes.get()!=0:
        self.txtarea.insert(END,f"Honey Chilly Potatoes\t\t {self.Honey_Chilly_Potatoes.get()}\t{self.HCP}\n")
    if self.Pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.Pasta.get()}\t{self.Pas}\n")
    if self.Dal_Makhani.get()!=0:
        self.txtarea.insert(END,f"Dal Makhani\t\t {self.Dal_Makhani.get()}\t{self.DM}\n")
    if self.Paneer_Butter_Masala.get()!=0:
        self.txtarea.insert(END,f"Paneer Butter Masala\t\t {self.Paneer_Butter_Masala.get()}\t{self.PBM}\n")
    if self.Malai_Kofta.get()!=0:
        self.txtarea.insert(END,f"Malai Kofta\t\t {self.Malai_Kofta.get()}\t{self.MK}\n")
    if self.Kadhai_Paneer.get()!=0:
        self.txtarea.insert(END,f"Kadhai Paneer\t\t {self.Kadhai_Paneer.get()}\t{self.KP}\n")
    if self.Plain_Roti.get()!=0:
        self.txtarea.insert(END,f"Plain Roti\t\t {self.Plain_Roti.get()}\t{self.PR}\n")
    if self.Butter_Naan.get()!=0:
        self.txtarea.insert(END,f"Butter Naan\t\t {self.Butter_Naan.get()}\t{self.BN}\n")
    if self.Tandoori_Roti.get()!=0:
        self.txtarea.insert(END,f"Tandoori_Roti\t\t {self.Tandoori_Roti.get()}\t{self.TR}\n")
    if self.Vanilla_Icecream.get()!=0:
        self.txtarea.insert(END,f"Vanilla Icecream\t\t {self.Vanilla_Icecream.get()}\t{self.VI}\n")
    if self.Strawberry_Icecream.get()!=0:
        self.txtarea.insert(END,f"Strawberry Icecream\t\t {self.Strawberry_Icecream.get()}\t{self.SI}\n")
    if self.Ras_Malai.get()!=0:
        self.txtarea.insert(END,f"Ras Malai\t\t {self.Ras_Malai.get()}\t{self.RM}\n")
    if self.Gulab_Jamun.get()!=0:
        self.txtarea.insert(END,f"Gulab Jamun\t\t {self.Gulab_Jamun.get()}\t{self.GJ}\n")
    if self.Kheer.get()!=0:
        self.txtarea.insert(END,f"Kheer\t\t {self.Kheer.get()}\t{self.Kh}\n")
    if self.Custard.get()!=0:
        self.txtarea.insert(END,f"Custard\t\t {self.Custard.get()}\t{self.Cu}\n")
    if self.Brownie_Sizzler.get()!=0:
        self.txtarea.insert(END,f"Brownie Sizzler\t\t {self.Brownie_Sizzler.get()}\t{self.BS}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    self.txtarea.insert(END,f"Total Tax Amount: {self.total_Tax}\n")
    self.txtarea.insert(END,f"Total Bill incl Taxex: {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
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
        self.total_Starters.set(0)
        self.total_Maincourse.set(0)
        self.total_Desserts.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
