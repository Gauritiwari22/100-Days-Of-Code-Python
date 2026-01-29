from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
current_card={}

try:
    data=pandas.read_csv("Day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("Day31/data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("Day31/data/words_to_learn.csv",index=False)
    next_card()

window = Tk()

window.title("Flashcard Game Capstone Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer=window.after(3000,flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="Day31/images/card_front.png")
card_back=PhotoImage(file="Day31/images/card_back.png")
card_background=canvas.create_image(400, 263, image=card_front)
card_title=canvas.create_text(400,150,text="",font=("arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_button=PhotoImage(file="Day31/images/wrong.png")
unknown=Button(image=cross_button,highlightthickness=0,command=next_card)
unknown.grid(row=1,column=0)

correct_button=PhotoImage(file="Day31/images/right.png")
known=Button(image=correct_button,highlightthickness=0,command=is_known)
known.grid(row=1,column=1)

next_card()

window.mainloop()
