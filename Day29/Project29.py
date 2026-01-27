from tkinter import *
from tkinter import messagebox
import random
import string

FONT=("Courier",8,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)

    letters=list(string.ascii_letters)
    numbers=list(string.digits)
    symbols=list(string.punctuation)

    password_list=(
        random.choices(letters,k=8)+
        random.choices(numbers,k=4)+
        random.choices(symbols,k=4)
    )

    random.shuffle(password_list)
    password="".join(password_list)

    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
        return

    is_ok=messagebox.askokcancel(title=website,
        message=f"These are the details entered:\n\n"
                f"Email:{email}\n"
                f"Password:{password}\n\n"
                f"Save?"
    )

    if is_ok:
        with open("Day29/data.txt","a") as file:
            file.write(f"{website} | {email} | {password}\n")

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

Button(text="Generate Password",command=generate_password).grid(row=3,column=3)
Button(text="Add",width=36,command=save_info).grid(row=4,column=1,columnspan=2)

window.mainloop()
