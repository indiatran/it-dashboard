from my_info import displayInfo
import random
from pathlib import Path

# show assignment info first
displayInfo()

# ASCII art 8-ball
EIGHT_BALL_ART = r"""
            _____
     .-"     "-.
    /  .-'''-.  \
 /  /  .-.  \  \
|  |  /   \  |  |
|  | |  8  | |  |
|  |  \   /  |  |
 \  \  `-'  /  /
    '. '-._.-' .'
        '-.____.-'
"""
print(EIGHT_BALL_ART)
print("Welcome to the Magic 8 Ball! (press Enter to submit a blank question)")

# read responses from text file into list
RESPONSES_FILE = Path(__file__).parent / "responses.txt"
with open(RESPONSES_FILE, "r", encoding="utf-8") as file:
    answers = [line.strip() for line in file if line.strip()]

if not answers:
    print("No responses available in responses.txt. Exiting.")
    raise SystemExit(1)
# loop until user quits; treat an empty response (Enter) as "yes"
try:
    while True:
        # Accept empty question (Enter) and still give an answer
        question = input("Ask the Magic 8 Ball a question: ")

        print("Magic 8 Ball says:", random.choice(answers))

        choice = input("Do you want to ask another question? (yes/no) [yes]: ").strip().lower()
        if choice in ("no", "n"):
            break
except KeyboardInterrupt:
    print("\nInterrupted — exiting.")

print("Goodbye!")