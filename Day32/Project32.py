import requests
from tkinter import *

# --------------------- API FUNCTION --------------------- #
def get_quote():
    try:
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()

        data = response.json()
        quote = data["quote"]

        canvas.itemconfig(quote_text, text=quote)

    except Exception as e:
        canvas.itemconfig(quote_text, text="API Error")


# --------------------- UI --------------------- #
window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414, highlightthickness=0)

# ✅ FIX 1: use forward slashes
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(
    150,
    207,
    text="Click for quote",
    width=250,
    font=("Arial", 14, "bold"),
    fill="black"
)

canvas.grid(row=0, column=0)

# ✅ FIX 2: forward slashes again
kanye_img = PhotoImage(file="kanye.png")

button = Button(
    image=kanye_img,
    command=get_quote,
    highlightthickness=0,
    borderwidth=0
)

button.grid(row=1, column=0)

window.mainloop()
