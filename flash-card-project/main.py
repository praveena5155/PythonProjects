import tkinter
import  random
import time
from tkinter import *
import pandas



#creating new flash cards
#creating a dataframe called data and loading the data from the below file.
data = pandas.read_csv("./data/french_words.csv")
#converting csv data into dictionary: using parameter-orient ="column value as a list"
dict_french_words = data.to_dict(orient="records")
print(dict_french_words)
current_card={}

#creating a function.to get hold of word and translation
def next_card() :
    global current_card #to save the french and english version of this random choice .
    global flip_timer #invalidating this timer each timw we go to a new card
    window.after_cancel(flip_timer)
    #picking up a random word
    current_card = random.choice(dict_french_words)
    #print(current_card)
    french_word = current_card["French"]
    #print(french_word)
    #to display the title and word on the window
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    #instead of above line we can also use : canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=front_image)
    #replacing it here also so that we get the english verson for every french word.
    flip_timer = window.after(3000, func=flip_card)

#chANGING THE CARD TO SHOW THE ENGLISH VERSION OF CURRENT CARD AND ALSO GONNA CHANGE THE IMAGE. 
def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text=current_card["English"],fill= "white")
    canvas.itemconfig(card_background, image= back_image)

#removing it from the list of all the wprds
def is_known () :
    dict_french_words.remove(current_card)
    data1 = pandas.DataFrame(dict_french_words)
    data1.to_dict("data/words_to_learn.csv")
    next_card()



#colors
Background_color = "#B1DDC6"

#developing the UI
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=Background_color)

flip_timer = window.after(3000, func=flip_card)

#Creating Buttons
button = tkinter.Button

image_of_right = PhotoImage(file="./images/right.png")
right_button = Button(image=image_of_right,highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)

image_of_wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image = image_of_wrong,highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=1,)

#displaying the flashcards through canvas.
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
#highlightthickness= to get rid of the border around.
canvas.config(bg=Background_color, highlightthickness=0)
#coulmnspan=to drag it towards the next coulmn also
canvas.grid(row=0, column=0, columnspan=2)
#adding text on images through canvas
#font will be in tuple(fontname,size,variety)
#card_word and card_title to hold on to the word text
card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word= canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))


next_card()



window.title("Flashy")
window.mainloop()

