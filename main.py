from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")

def next_card():
    current_card = choice(data)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text= current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)

wrong_back_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_back_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()



window.mainloop()