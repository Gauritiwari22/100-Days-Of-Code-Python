"Day 27"

import tkinter
window=tkinter.Tk()
window.title("My first GUI program") # to give titles
window.minsize(width=500, height=300) # setting up the size of the window

# Creating labels

my_label=tkinter.Label(text="My label",font=("Arial",24,"bold"))
my_label.pack() # Prints label to top

my_label["text"]="New text" # to edit text of a label
my_label.config(text="Another text") # to edit text of a label

from tkinter import * # to import all classes from the module

# Creating buttons

def button_clicked():
    my_label["text"]="Button clicked"


button=Button(text="Click me",command=button_clicked)
button.pack()

# Entry - creates a label for user to input data in

input=Entry(width=20)
input.pack() 
input.get()










# args= unlimited arguments - can add any number of values in a function

# to add n numbers passed in a function
def add(*args):
    return sum(args)

print(add(4,5,6,7,8,9,1,2)) # output=42

# **kwargs= key word arguments

def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(4,add=4,multiply=7)










window.mainloop()