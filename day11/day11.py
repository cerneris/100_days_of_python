# Blackjack
import random
from enum import Enum

class CardValues(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10

CARDSET = set(["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"])
CARDS = {
    "spades" : CARDSET.copy(),
    "clubs" : CARDSET.copy(),
    "hearts" : CARDSET.copy(),
    "diamonds" : CARDSET.copy()
}

def pick_card_random(amount):
    ret_cards = []
    for i in range(amount):
        rand_choice_suit = list(CARDS.keys())[random.randint(0, 3)]
        rand_choice_card = list(CARDS[rand_choice_suit])[random.randint(0, len(CARDS[rand_choice_suit]) - 1)]
        CARDS[rand_choice_suit].remove(rand_choice_card)
        ret_cards.append((rand_choice_suit, rand_choice_card))
    return ret_cards

def opponent_draw():
    cards = pick_card_random(2)
    return cards
    
def player_draw():
    cards = pick_card_random(2)
    return cards

def check_result(cards_player, cards_opponent):
    total_value_player = 0
    total_value_opponent = 0
    for card in cards_player:
        total_value_player += CardValues[card[1]].value
    for card in cards_opponent:
        total_value_opponent += CardValues[card[1]].value
    if total_value_player > 21:
        print("Over 21 for player.")
        print("You lose!!")
    elif total_value_opponent > 21:
        print("Over 21 for opponent.")
        print("You win!!")
    elif total_value_player == total_value_opponent:
        print("Draw, you get your money back.")
    elif total_value_player > total_value_opponent:
        print("You win!!")
    else:
        print("You lose!!")

def print_cards(cards, amount, side):
    print(f"{side} CARDS: ")
    for i in range(amount):
        print(f"{cards[i]}", end="")
    print("")

def calculate_total(cards, first_draw):
    total_value = 0
    for card in cards:
        if card[1] == "ACE" and first_draw:
            total_value += 11
        else:
            total_value += CardValues[card[1]].value
    print(f"The total value of these cards is currently: {total_value}")
    if total_value == 21:
        print("THIS IS A BLACKJACK (21)!!")
    return total_value

def game():
    # Initial draw
    opponent = opponent_draw()
    player = player_draw()
    print_cards(opponent, 1, "OPPONENT")
    print_cards(player, 2, "PLAYER")
    player_total = calculate_total(player, True)
    while True:
        hit = input("Would you like another card (y/n): ")
        if hit == "y":
            print("Player hits another card")
            player += pick_card_random(1)
        else:
            break
        print_cards(player, len(player), "PLAYER")
        player_total = calculate_total(player, True)
        if player_total > 21:
            check_result(player, opponent)
            break
    print_cards(opponent, len(opponent), "OPPONENT")
    cur_total = calculate_total(opponent, True)
    while True:
        if cur_total <= player_total and player_total < 22 and cur_total <= 17:
            print("Opponent hits another card")
            opponent += pick_card_random(1)
            print_cards(opponent, len(opponent), "OPPONENT")
            cur_total = calculate_total(opponent, True)
        else:
            break
    check_result(player, opponent)

game()