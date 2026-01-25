from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title("Mile to Km Converter")

def convert():
    miles = float(user_input.get())
    km = miles * 1.609
    answer.config(text=km)

user_input = Entry(width=20)
user_input.place(x=200, y=50)

label_1 = Label(text="Miles", font=("Arial", 10))
label_1.place(x=320, y=50)


label_2 = Label(text="is equal to", font=("Arial", 10))
label_2.place(x=120, y=75)

answer = Label(text="0", font=("Arial", 10))
answer.place(x=200, y=75)

label_3 = Label(text="Km", font=("Arial", 10))
label_3.place(x=320, y=75)

button = Button(text="Calculate", command=convert)
button.place(x=230, y=120)




window.mainloop()
