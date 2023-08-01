import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

mainWindow = Tk()
mainPic = PhotoImage(file='RPS main image.png')
mainWindow.geometry("400x320")
mainWindow.title("Rock Paper Scissors Game")
mainWindow.config(background="#0377fc")
mainLabel1 = Label(mainWindow,text="This is the rock paper scissors game",
                  font=("Comic Sans",20,"bold"),
                  fg="black",
                  bg="White",
                  relief=RAISED,
                  bd=10,).pack()

def pick_rock():
    user_choice = "rock"
    com_choice = random.choice(options)
    global user_score, com_score
    if user_choice == com_choice:
        result_str.set("Draw")
    elif com_choice == "paper":
        result_str.set("Computer wins")
        com_score += 1
    elif com_choice == "scissors":
        result_str.set("Player wins")
        user_score += 1

def pick_paper():
    user_choice = "paper"
    com_choice = random.choice(options)
    global user_score,com_score
    if user_choice == com_choice:
        result_str.set("Draw")
    elif com_choice == "rock":
        result_str.set("Player wins")
        user_score += 1
    elif com_choice == "scissors":
        result_str.set("Computer wins")
        com_score += 1

def pick_scissors():
    user_choice = "scissors"
    com_choice = random.choice(options)
    global user_score, com_score
    if user_choice == com_choice:
        result_str.set("Draw")
    elif com_choice == "paper":
        result_str.set("Player wins")
        user_score += 1
    elif com_choice == "rock":
        result_str.set("Computer wins")
        com_score += 1

def pick_quit():
    endWindow = Toplevel()
    endWindow.geometry("400x320")
    endWindow.config(background="#0377fc")
    endLabel1 = Label(endWindow,
                     text=f"The player's score is {user_score}",
                     font=("Comic Sans",30),
                      fg="black",
                      bg="White",
                      relief=RAISED).pack()
    endLabel2 = Label(endWindow,
                     text=f"The computer's score is {com_score}",
                     font=("Comic Sans",30),fg="black",
                     bg="White",
                     relief=RAISED).pack()
    if user_score > com_score:
        endLabel3 = Label(endWindow,
                          text=f"Player wins!",
                          font=("Comic Sans",30),
                          fg="black",
                          bg="White",
                          relief=RAISED).pack()
    elif user_score < com_score:
        endLabel3 = Label(endWindow,
                          text=f"Computer wins!",
                          font=("Comic Sans",30),
                          fg="black",
                          bg="White",
                          relief=RAISED).pack()
    elif user_score == com_score:
        endLabel3 = Label(endWindow,
                          text=f"The game is a draw",
                          font=("Comic Sans",30),
                          fg="black",
                          bg="White",
                          relief=RAISED).pack()
    endLabel4 = Label(endWindow,
                      text="Thanks for Playing",
                      font=("Comic Sans",30),
                      fg="black",
                      bg="White",
                      relief=RAISED).pack()

def StartGame():
    startWindow = Toplevel()
    startWindow.geometry("1000x380")
    startWindow.title("Rock Paper Scissors Game")
    startWindow.config(background="#0377fc")
    startLabel1 = Label(startWindow,text="Select Rock, Paper or Scissors. Click exit to end game",
                       font=("Comic Sans",20,"bold"),
                       bg="White",
                       fg="Black",
                        relief=RAISED).pack()
    rockButton = Button(startWindow,image=rockPic,
                        command=pick_rock).place(x=25,y=70)
    paperButton = Button(startWindow,image=paperPic,
                         command=pick_paper).place(x=250,y=70)
    scissorsButton = Button(startWindow,image=scissorsPic,
                            command=pick_scissors).place(x=465,y=70)
    quitButton = Button(startWindow,image=quitPic,
                        command=pick_quit).place(x=710,y=70)
    result_label = Label(startWindow, textvariable=result_str,
                        font=("Comic Sans", 20, "bold"),
                        bg="White",
                        fg="Black",
                         relief=RAISED).pack()

mainButton = Button(mainWindow,text="Click me to start",
                    font=("Comic Sans",20),
                    command=StartGame,
                    image=mainPic,
                    compound="top").place(x=50,y=70)

options = ("rock", "paper", "scissors")
user_score = 0
com_score = 0
result_str = StringVar()
result_str.set("Result")
rockPic = PhotoImage(file="rock.png")
paperPic = PhotoImage(file="paper.png")
scissorsPic = PhotoImage(file="scissors.png")
quitPic = PhotoImage(file="exit_button.png")
mainWindow.mainloop()