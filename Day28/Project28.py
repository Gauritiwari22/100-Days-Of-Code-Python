from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
BROWN = "#701705"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps%8==0:
        countdown(long_break_sec)
        title_label.config(text="Break",fg=BROWN)
    elif reps%2==0:
        countdown(short_break_sec)
        title_label.config(text="Break",fg=BROWN)
    else:
        countdown(work_sec)
        title_label.config(text="Work",fg=BROWN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=(f"0{count_sec}") #dynamic typing i.e changing the variable type from one data type to another

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=0
        sessions=math.floor(reps/2)
        for i in range(sessions):
            mark+=1
        check_marks.config(text=f"Session: {mark}",font=(FONT_NAME, 20, "bold"), fg=BROWN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(600,600)
window.title("Pomodoro")
window.config(bg=YELLOW) 


canvas = Canvas(width=600, height=500, bg=YELLOW, highlightthickness=0)
clock_img = PhotoImage(file="Day28/CLOCK.png")
canvas.create_image(250, 257, image=clock_img)
timer_text=canvas.create_text(250, 250, text="00:00", font=(FONT_NAME, 35, "bold"), fill="black")
canvas.place(x=50,y=50)


title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=BROWN, bg=YELLOW)
title_label.place(x=230,y=30)

start_button = Button(text="Start", width=10, font=(FONT_NAME, 8, "bold"), highlightthickness=0,command=start_timer)
start_button.place(x=150,y=550)

reset_button = Button(text="Reset", width=10, font=(FONT_NAME, 8, "bold"), highlightthickness=0,command=reset_timer)
reset_button.place(x=360,y=550)

check_marks=Label(text="",highlightthickness=0,bg=YELLOW)
check_marks.place(x=220,y=500)


window.mainloop()