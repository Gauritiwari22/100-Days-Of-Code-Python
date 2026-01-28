from tkinter import *
from tkinter import messagebox
import random
import string
import json

FONT=("Courier", 8, "bold")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("Day30/data.json", "r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email=data[website]["Email"]
            password=data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters=list(string.ascii_letters)
    numbers=list(string.digits)
    symbols=list(string.punctuation)

    password_list = (
        random.choices(letters,k=8) +
        random.choices(numbers,k=4) +
        random.choices(symbols,k=4)
    )

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Day30/data.json","r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            #If file doesn't exist, start with new_data
            data=new_data
        else:
            #Updating old data with new data
            data.update(new_data)
        finally:
            with open("Day30/data.json","w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)
            
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="Day29/logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

Label(text="Website:",font=FONT).grid(row=1,column=0)
Label(text="Email/Username:",font=FONT).grid(row=2,column=0)
Label(text="Password:",font=FONT).grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_entry=Entry(width=35)
email_entry.insert(0,"hello123@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=3)
add_button=Button(text="Add",width=36,command=save_info)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=3)

add_button=Button(text="Add",width=36,command=save_info)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()