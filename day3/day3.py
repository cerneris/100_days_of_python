
answers = {
    "right_answers" : ["left", "wait", "yellow"],
    "wrong_answers" : ["right", "swim", "red", "blue"]
}

print(""""          ████████████████████████████████████████████████████████          
        ██        ██    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ██        
      ██  ██████░░  ██    ▓▓▓▓██████████████████████████████████    ██      
    ██  ██▓▓▓▓▓▓██░░  ██    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒██    ██    
    ██░░██▓▓▒▒▒▒██░░░░██░░░░██▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██    
  ██  ██████████████░░  ██░░  ██████████████████████████████████████░░  ██  
  ██░░██▓▓▒▒▓▓▒▒▒▒██░░░░██░░░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██░░░░██  
██  ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░  ██░░  ██▒▒▒▒▒▒▒▒▒▒██████████████▒▒▒▒▒▒▒▒▒▒██░░  ██
██░░██████████████████░░░░██░░░░████████████              ████████████░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░██░░▒▒██████░░░░██░░░░░░░░░░░░░░██
██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒██▒▒▒▒▓▓████░░░░░░██░░░░░░██▓▓▒▒▒▒██▓▓▓▓▓▓██
██▒▒▒▒██░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒██░░██▒▒████▒▒████░░░░░░██░░░░░░██▒▒████▒▒▒▒▒▒▒▒██
██░░██████████████████░░░░▓▓░░░░████████████░░░░░░░░░░░░░░████████████░░░░██
██░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░▓▓░░░░██▓▓▓▓▓▓▓▓▓▓████▓▓████████▓▓▓▓▓▓▓▓▓▓██░░░░██
██░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒██░░░░██    ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓██    ██
██░░██████████████████░░░░██░░░░██████████████████████████████████████░░░░██
██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░░░██▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░░░██
██░░██▒▒▒▒▒▒▒▒▒▒▓▓▒▒██░░░░██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░░░██
██░░██████████████████░░░░██░░░░██████████████████████████████████████░░░░██
██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓██░░░░██
██░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░░░██
██░░██████████████████░░░░██░░░░██████████████████████████████████████░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
  ██▓▓████████████████████▓▓████████████████████▓▓████████████████████████  
############################################################################""")
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
cross_road = input('\tType "left" or "right: ')
if cross_road not in answers["right_answers"]:
    print(cross_road)
    print(answers["right_answers"])
    print("A bear came and ate you! Game Over!")
    exit(0)
print("You have come to a lake? Swim or wait?")
swim_wait = input('\tType swim or wait: ')
if swim_wait not in answers["right_answers"]:
    print("You drowned! Game Over!")
    exit(0)
print("A ship came and took you to a set of doors.")
print("Which door shall you open, red blue or yellow?")
door_color = input('\tType red, blue or yellow: ')
if door_color not in answers["right_answers"]:
    print("You fell in an endless hole behind the door! Game Over!")
    exit(0)
print("You win! You got the treasure!!")