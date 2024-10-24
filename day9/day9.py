# Blind bid
import os

bidders = {}

answer = "yes".lower()
while answer == "yes":
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    answer = input("Is there any other bidders? (yes/no)").lower()
    os.system('cls')
    
highest_bidder = max(bidders, key=bidders.get)
print(f"The winner is {highest_bidder} with ${bidders[highest_bidder]}")