# Rock, paper, scissors
import random

# Rock Paper Scissors ASCII Art
drawings = {
# Rock
"rock" : """
    _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
""",
# Paper
"paper" : """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
# Scissors
"scissors" : """
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
"""
}
choices = ["rock", "paper", "scissors"]
winners = {
    "rock" : "paper",
    "paper" : "scissors",
    "scissors" : "rock"
}
def opponent_choice():
    choice = random.randint(0, 2)
    print(f"Opponent choosed: {choices[choice]}")
    print(f"{drawings[choices[choice]]}")
    return choices[choice]

def player_choice():
    choice = input("Rock, paper or scissors? ").lower()
    if choice == "exit":
        print("Exiting game! Thank you for playing!")
        exit(0)
    if choice in choices:
        print(f"You choosed: {choice}")
        print(f"{drawings[choice]}")
        return choice
    else:
        print("That is not a correct choice, please choose again")
        return player_choice()
    
while True:
    print("Let's play rock, paper and scissors!")
    print("Type exit, to exit the game.")
    player = player_choice()
    opponent = opponent_choice()
    if winners[player] == opponent:
        print("You lose!")
    elif player == opponent:
        print("Draw!")
    else:
        print("You win!")
