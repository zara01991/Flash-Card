import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
df = pd.DataFrame(data)

try:
    data_to_learn = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    
    df.to_csv("./data/words_to_learn.csv", index = False)
    data_to_learn = pd.read_csv("./data/words_to_learn.csv")

finally:
    df_to_learn = pd.DataFrame(data_to_learn)


french_list = list(df_to_learn["French"])
dict = {row.French: row.English   for (index, row) in df_to_learn.iterrows() }
#dict_to_learn = dict

# ---------------------------- pick a random word -------------------- #
def right_show_french_word():

    #random_word = random.choice(french_list)
    global random_word
  
    dict.pop(random_word)
    word_to_learn = pd.DataFrame(dict.items(), columns = ['French','English'])
    word_to_learn.to_csv ("./data/words_to_learn.csv", index = None)


    random_word = random.choice(french_list)

    canvas.itemconfig (canvas_image,image =card_front_img )
        
    canvas.itemconfig (title_text , text = "French", fill = "black")

    canvas.itemconfig (word_text , text = random_word, fill = "black")

    count_down(3, random_word)




def wrong_show_french_word():

    random_word = random.choice(french_list)

    canvas.itemconfig (canvas_image,image =card_front_img )
        
    canvas.itemconfig (title_text , text = "French", fill = "black")

    canvas.itemconfig (word_text , text = random_word, fill = "black")

    count_down(3, random_word)

# ---------------------------- 3s count down -------------------------- #
def count_down(count, frenchword):
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1,frenchword )

    else:
        canvas.itemconfig (canvas_image,image =card_back_img )
        
        canvas.itemconfig (title_text , text = "English", fill = "white")

        canvas.itemconfig (word_text, text = dict[frenchword], fill = "white")


        


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.minsize (height = 700, width = 800)
window.config (padx = 70, pady = 20, bg = BACKGROUND_COLOR)

canvas = tk.Canvas(height = 600, width = 850, bg = BACKGROUND_COLOR,highlightthickness=0)
card_front_img = tk.PhotoImage (file = "./images/card_front.png")
card_back_img = tk.PhotoImage (file = "./images/card_back.png")
canvas_image = canvas.create_image(430,300, image = card_front_img)
title_text = canvas.create_text(430,180, text = "French",fill = "black", font = ("Arial", 35, "bold"))
word_text = canvas.create_text(430,300, text = random.choice(french_list),fill = "black", font = ("Arial", 50, "bold"))
random_word = random.choice(french_list)
count_down(3, random_word)
canvas.grid(column = 1, row = 1,columnspan = 2)



rightbutton_img = tk.PhotoImage (file = "./images/right.png")
rightbutton = tk.Button(image = rightbutton_img , highlightthickness=0, command = right_show_french_word)
rightbutton.grid(column = 2, row= 2)

wrongbutton_img = tk.PhotoImage (file = "./images/wrong.png")
wrongbutton = tk.Button(image = wrongbutton_img , highlightthickness=0, command = wrong_show_french_word)
wrongbutton.grid(column = 1, row= 2)




window.mainloop()




