from tkinter import *
import mysql.connector
import os
from dotenv import load_dotenv

root = Tk()
root.title("Address Book")
root.geometry("500x400")

# Loading the env file
load_dotenv("address_cred.env")

def submit_db():
    # connecting to database
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    # Creating a cursor
    cursor = conn.cursor()

    cursor.execute("INSERT INTO address_info (name, surname, gender, state, phone, address) VALUES (%s, %s, %s, %s, %s, %s)",
                (name_var.get(), surname_var.get(), gender_var.get(), state_var.get(), phone_var.get(), address_var.get()))

    conn.commit()

    cursor.close()
    conn.close()

    name_var.set("")
    surname_var.set("")
    gender_var.set("")
    state_var.set("")
    phone_var.set("")
    address_var.set("")

def record():

    record_window = Toplevel(root)
    record_window.title("Records")
    record_window.geometry("800x400")

    # connecting to database
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    # Creating a cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM address_info")
    display = cursor.fetchall()
    
    Label(record_window, text="Records", font=("Arial", 8))
    
    for i in display:
        record_label = Label(record_window, text=str(i), font=("Arial", 12))
        record_label.pack(anchor='w')

    cursor.close()
    conn.close()

def click():
    submit_db()

# Creating Label
address_book = Label(root, text="Address Book", font=("Arial Bold", 20))

# Placing the Label
address_book.grid(row=0, column=1, columnspan=1, padx=20, pady=15)

# Creating the information field
name = Label(root, text="Name", font=("Arial", 12))
surname = Label(root, text="Surname", font=("Arial", 12))
gender = Label(root, text="Gender", font=("Arial", 12))
state = Label(root, text="State", font=("Arial", 12))
phone= Label(root, text="Contact", font=("Arial", 12))
address = Label(root, text="Address", font=("Arial", 12))

# Placing the information field
name.grid(row=2, column=0, padx=10, pady=5)
surname.grid(row=3, column=0, padx=10, pady=5)
gender.grid(row=4, column=0, padx=10, pady=5)
state.grid(row=5, column=0, padx=10, pady=5)
phone.grid(row=6, column=0, padx=10, pady=5)
address.grid(row=7, column=0, padx=10, pady=5)

# Creating variables
name_var = StringVar()
surname_var = StringVar()
gender_var = StringVar()
state_var = StringVar()
phone_var = StringVar()
address_var = StringVar()

# Creating Entry Field
name_entry = Entry(root, font=("Arial",12), textvariable=name_var, width=40)
surname_entry = Entry(root, font=("Arial",12), textvariable=surname_var, width=40)
gender_entry = Entry(root, font=("Arial",12), textvariable=gender_var, width=40)
state_entry = Entry(root, font=("Arial",12), textvariable=state_var, width=40)
phone_entry = Entry(root, font=("Arial",12), textvariable=phone_var, width=40)
address_entry = Entry(root, font=("Arial",12), textvariable=address_var, width=40)

# Placing the entry fields
name_entry.grid(row=2, column=1)
surname_entry.grid(row=3, column=1)
gender_entry.grid(row=4, column=1)
state_entry.grid(row=5, column=1)
phone_entry.grid(row=6, column=1)
address_entry.grid(row=7, column=1)

# Creating a submit button
submit = Button(root, text="Add to address book", font=("Arial",10), command=click)
exit = Button(root, text="Exit", command=root.quit, font=("Arial",12))

# Creating record button
query = Button(root, text="Show Records", font=("Arial",10), command=record)

# Placing the button
submit.grid(row=8, column=1, padx=10, pady=5, ipadx=100)
query.grid(row=9, column=1, padx=10, pady=5, ipadx=100)
exit.grid(row=10, column=1, padx=10, pady=5)

root.mainloop()