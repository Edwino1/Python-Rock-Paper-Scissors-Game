# Rock Paper Scissors Game
import random

options = ("rock", "paper", "scissors",)
user_score = 0
com_score = 0

print("Press q to quit")

while True: 
    user_choice = input("Type either 'r' for rock, 'p' for paper or 's' for scissors")
    com_choice = random.choice(options)
    
    if user_choice.lower() == "r":
        user_choice = "rock"
    elif user_choice.lower() == "p":
        user_choice = "paper"
    elif user_choice.lower() == "s":
        user_choice = "scissors"
    
        
    if user_choice == com_choice:
        print("Draw, please try again")
    elif user_choice == "rock" and com_choice == "paper":
        print("Computer wins")
        com_score += 1
    elif user_choice == "rock" and com_choice == "scissors":
        print("User wins")
        user_score += 1
    elif user_choice == "paper" and com_choice == "rock":
        print("User wins")
        user_score += 1
    elif user_choice == "paper" and com_choice == "scissors":
        print("Computer wins")
        com_score += 1
    elif user_choice == "scissors" and com_choice == "paper":
        print("User wins")
        user_score += 1
    elif user_choice == "scissors" and com_choice == "rock":
        print("Computer wins")
        com_score += 1
    elif user_choice.lower() == "q":
        print(f"The player's score is {user_score}")
        print(f"The computer's  score is {com_score}")
        if user_score > com_score:
            print("Player wins")
        elif user_score < com_score:
            print("Computer wins")
        elif user_score == com_score:
            print("The game is a draw")
        print("Thanks for playing!")
        break

