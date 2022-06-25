#! /usr/bin/env python3
from tkinter import *
import random
from tkinter import messagebox

# initiliazing
seconds = 60
word = ""
score = 0
root = Tk()
root.title("Word_Jumble_Game")
root.geometry("600x400")
root.iconbitmap("C:/Users/msert/Downloads/python_18894.ico")
root_label = Label(root, text="press enter to start", font=("Helvatica", 20))
root_label.pack(pady=10)
root_word_label = Label(root, text="", font=("Helvatica", 50))
root_word_label.pack(pady=20)


# function for initiliaze functions
def start(event=""):
    if seconds == 60:
        countdown()
        shuffler()

    else:
        answer()


# function for shuffling
def shuffler():
    global word
    root_entry.delete(0, END)
    words = ["Turkey", "England", "Sweden", "Qatar", "Germany", "Spain", "China", "Norway", "Italy", "Cuba", "USA"]
    word = random.choice(words)
    breakdown = []
    for letter in word:
        breakdown.append(letter)
    random.shuffle(breakdown)
    shuffled_word = ""
    for letter in breakdown:
        shuffled_word += letter

    root_word_label.config(text=str(shuffled_word), font=("Helvatica", 50))


# function for second countdown
def countdown():
    global seconds
    if seconds == 0:
        messagebox.showinfo("Time over", "Time over and your score " + str(score))
    elif seconds > 0:
        root_time_label.config(text="time: " + str(seconds), font=("Helvatica", 20))
        seconds -= 1
        root.after(1000, countdown)


# function for check answer
def answer():
    global score
    global seconds
    if seconds > 0:
        if str(word).lower().strip() == root_entry.get().strip():
            score += 1
            root_score_label.config(text="score: " + str(score), font=("Helvatica", 20))
            root_entry.focus_set()
            shuffler()
        else:
            root_score_label.config(text="false")
            root_entry.focus_set()
            shuffler()


# function for restart
def restart():
    global score
    global seconds
    score = 0
    seconds = 60
    root_score_label.config(text="score: ")


# area for entering word
root_entry = Entry(root, font=("Helvatica", 50))
root_entry.pack(pady=10, padx=20)
root_entry.focus_set()
root_frame = Frame(root)
root_frame.pack(pady=10)
# button for answer, shuffling etc
root_button = Button(root_frame, text="New word", command=start)
root_button.grid(row=0, column=0, padx=10)
# button for restart
root_restart_button = Button(root_frame, text="restart", command=restart)
root_restart_button.grid(row=0, column=1, padx=10)
# score label
root_score_label = Label(root, text="score:", font=("Helvatica", 20))
root_score_label.pack(pady=10)
# time label
root_time_label = Label(root, text="time:", font=("Helvatica", 20))
root_time_label.pack(pady=10)
# key binding to start
root.bind('<Return>',start)
# loop for window stay open
root.mainloop()
