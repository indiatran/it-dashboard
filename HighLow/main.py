from my_info import displayInfo
import random

def play_game():
    secret_number = random.randint(1, 100)
    tries = 0

    while True:
        try:
            raw = input("Guess the number (1-100): ")
            guess = int(raw)
        except ValueError:
            print("Please enter a valid integer between 1 and 100.")
            continue

        tries += 1

        if guess > secret_number:
            print("Too High")
        elif guess < secret_number:
            print("Too Low")
        else:
            print(f"You guessed it in {tries} tries!")
            break

# show assignment info first
displayInfo()

# Allow player to play again
again = "yes"

while again.lower() == "yes":
    play_game()
    again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")