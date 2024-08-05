import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='products')
cursor = db.cursor()

access = Tk()
access.geometry('700x500')
access.title('Products Entry')
access.configure(bg='lightblue')

def calculate():
    product_tot.set(product_price.get() * product_qty.get())

def add():
    id = product_id.get()
    name = product_name.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('insert into details values(%s,%s,%s,%s,%s)',
                   [id,name,price,qty,tot])
    db.commit()
    tkinter.messagebox.showinfo('Products Entry','Added')

def view():
    id = product_id.get()
    cursor.execute('select * from details where ProId=%s',[id])
    data = cursor.fetchone()
    if data != None:
        product_name.set(data[1])
        product_price.set(data[2])
        product_qty.set(data[3])
        product_tot.set(data[4])
    else:
        tkinter.messagebox.showinfo('Product Entry','No data')

def update():
    id = product_id.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('update details set ProPrice=%s,ProQty=%s,TotalPrice=%s '
                   'where ProId=%s',[price,qty,tot,id])
    db.commit()
    tkinter.messagebox.showinfo('Products Entry','Products Updated')

def delete():
    id = product_id.get()
    cursor.execute('delete from details where ProId=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Products Entry','Deleted')

def clear():
    product_id.set('')
    product_name.set('')
    product_price.set('')
    product_qty.set('')
    product_tot.set('')

def overall():
    global viewpage
    viewpage = Toplevel(access)
    viewpage.geometry('1200x500')
    viewpage.title('Products List')
    viewpage.configure(bg='lightblue')
    cursor.execute('select * from details')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewpage, text='Pro Id', font=('calibri',15,'bold'),
          bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='Pro Name', font=('calibri',15,'bold'),
          bg='lightblue').grid(row=0,column=1)
    Label(viewpage, text='Pro Price', font=('calibri',15,'bold'),
          bg='lightblue').grid(row=0,column=2)
    Label(viewpage, text='Pro Qty', font=('calibri',15,'bold'),
          bg='lightblue').grid(row=0,column=3)
    Label(viewpage, text='Total Price', font=('calibri',15,'bold'),
          bg='lightblue').grid(row=0,column=4)
    for i in range(rows):
        for j in range(cols):
            s = Entry(viewpage, font=('calibri',13))
            s.grid(row=i+1,column=j)
            s.insert(END,data[i][j])



Label(access, text='Products Entry', font=('calibri',25), fg='blue').place(x=200,y=10)

product_id_label = Label(access, text='Product Id', font=('calibri',20),
                         bg='lightblue')
product_id_label.place(x=100,y=70)
product_id = StringVar()
product_id_entry = Entry(access, textvariable=product_id, font=('calibri',17))
product_id_entry.place(x=280,y=70)

product_name_label = Label(access, text='Product Name', font=('calibri',20),
                         bg='lightblue')
product_name_label.place(x=100,y=120)
product_name = StringVar()
product_name_entry = Entry(access, textvariable=product_name, font=('calibri',17))
product_name_entry.place(x=280,y=120)

product_price_label = Label(access, text='Product Price', font=('calibri',20),
                         bg='lightblue')
product_price_label.place(x=100,y=170)
product_price = IntVar()
product_price_entry = Entry(access, textvariable=product_price, font=('calibri',17))
product_price_entry.place(x=280,y=170)

product_qty_label = Label(access, text='Product Qty', font=('calibri',20),
                         bg='lightblue')
product_qty_label.place(x=100,y=220)
product_qty = IntVar()
product_qty_entry = Entry(access, textvariable=product_qty, font=('calibri',17))
product_qty_entry.place(x=280,y=220)

product_tot_label = Label(access, text='Total Price', font=('calibri',20),
                         bg='lightblue')
product_tot_label.place(x=100,y=270)
product_tot = IntVar()
product_tot_entry = Entry(access, textvariable=product_tot, font=('calibri',17))
product_tot_entry.place(x=280,y=270)

but_cal = Button(access, text='Calculate', font=('calibri',10), bg='blue', fg='white',
                 width='8', height='1', command=calculate)
but_cal.place(x=540,y=220)

but_add = Button(access, text='Add', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=add)
but_add.place(x=100,y=330)

but_view = Button(access, text='View', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=view)
but_view.place(x=230,y=330)

but_upd = Button(access, text='Update', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=update)
but_upd.place(x=360,y=330)

but_del = Button(access, text='Delete', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=delete)
but_del.place(x=100,y=400)

but_clr = Button(access, text='Clear', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=clear)
but_clr.place(x=230,y=400)

but_ovr = Button(access, text='Overall', font=('calibri',15), bg='blue', fg='white',
                 width='10', height='1', command=overall)
but_ovr.place(x=360,y=400)

access.mainloop()