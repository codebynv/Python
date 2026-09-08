# Program 49
# Rock Paper Scissors
#gpt

import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input("Enter rock/paper/scissors (quit to exit): ").lower()

    if user == "quit":
        break

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Draw")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win")
    else:
        print("Computer Wins")