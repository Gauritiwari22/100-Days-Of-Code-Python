from tkinter import *

window_1=Tk()
window_1.title("Another GUI")
window_1.minsize(width=400,height=200)

label_1=Label(text="hello",font=("Arial",24,"bold"))
label_1.pack()

def on_click():
    label_1.config(text=input_1.get())

button_1=Button(text="click me!",command=on_click)
button_1.pack()

input_1=Entry()
input_1.pack()



window_1.mainloop()




