# Number guessing game
import random

NUMBER_TO_GUESS = random.randint(0, 100)
DIFFICULTY = 'easy'
LIVES = 5

def randomize_number():
    global NUMBER_TO_GUESS
    NUMBER_TO_GUESS = random.randint(0, 100)

def check_guess(guess):
    if guess == NUMBER_TO_GUESS:
        print(f"You guessed the correct number!! It was {NUMBER_TO_GUESS}.")
        return 0
    if guess > NUMBER_TO_GUESS:
        print("Number is lower than your guessed number.")
        return 1
    if guess < NUMBER_TO_GUESS:
        print("Number is higher than your guessed number.")
        return 2

def change_difficulty():
    global DIFFICULTY
    difficulty = input("Choose a difficulty. Type 'easy', 'hard' or 'impossible': ")
    DIFFICULTY = difficulty

def change_lives():
    global LIVES
    match DIFFICULTY:
        case 'easy':
            print("Easy mode chosen, 10 lives granted.")
            LIVES = 10
        case 'hard':
            print("Hard mode chosen, 5 lives granted.")
            LIVES = 5
        case 'impossible':
            print("Impossible mode chosen, 1 life granted.")
            LIVES = 1
        case _:
            print("Invalid difficulty, try again.")
    
while True:
    print("I'm thinking of a number between 0 and 100")
    change_difficulty()
    change_lives()
    while LIVES:
        player_guess = int(input("Guess a number: "))
        check = check_guess(player_guess)
        if not check:
            print("You win!")
            break
        else:
            LIVES -= 1
            print(f"You have lost a life, lives left: {LIVES}")
    play_again = input("Do you want to play again (y/n)? ")
    if play_again == "n":
        break
    else:
        randomize_number()
print("Thank you for playing!!")