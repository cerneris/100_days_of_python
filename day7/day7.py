# Hangman
import random

WORDS = [
    "test",
    "othertest"
]
LIVES = 5

guess_chars = set()
choice_word = WORDS[random.randint(0, len(WORDS) - 1)]

while LIVES:
    visualization = []
    for letter in choice_word:
        if letter in guess_chars:
            visualization.append(letter)
        else:
            visualization.append("_")
    print(" ".join(visualization))
    if "".join(visualization) == choice_word:
        print("You win!")
        break 
    char = input("Guess a character: ")
    if char not in guess_chars:
        guess_chars.add(char)
    else:
        print(f"{char} already used.")
        LIVES -= 1
        print(f"Lives left: {LIVES}")
        continue
    if char not in choice_word:
        LIVES -= 1
        print(f"{char} not in wanted word")
        print(f"Lives left: {LIVES}")
    else:
        print(f"Correct character guessed.")
if not LIVES:
    print("You died, game over.")