# Program 50
# Number Guessing Game
#gpt

import random

secret = random.randint(1, 100)

for attempt in range(1, 6):

    guess = int(input(f"Attempt {attempt}/5 - Enter Guess: "))

    if guess == secret:
        print("Congratulations! Correct Guess.")
        break

    elif guess < secret:
        print("Too Low")

    else:
        print("Too High")

else:
    print("You Lost!")
    print("Secret Number was:", secret)