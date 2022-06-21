"""
#   https://www.asciiart.eu/people/body-parts/hand-gestures 
"""

import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# RULES TO WIN ----- Rock > Scissors > Paper > Rock
options = ["R", "P", "S"]
# Selections: 
player_select = input("Please select your choice Rock(R), Paper(P), Scissors(S): \n").upper()

computer_select = options[random.randint(0, len(options) - 1)]


# Player selection
if player_select == "R":
    print(f"You selected {rock} ")
elif player_select == "P":
    print(f"You selected {paper} ")
elif player_select == "S":
    print(f"You selected {scissors} ")
else:
    print("Invalid choice. Try Again.")
    
# Computer selection 
if computer_select == "R":
    print(f"Computer selected {rock} ")
elif computer_select == "P":
    print(f"Computer selected {paper} ")
elif computer_select == "S":
    print(f"Computer selected {scissors} ")

# Game logic
# RULES TO WIN ----- Rock > Scissors > Paper > Rock
if player_select == computer_select:
    print("Its tie!")
elif player_select == "R" :
    if computer_select == "S":
        print("You Win")
    else: 
        print("You lost")
elif player_select == "S":
    if computer_select == "P":
        print("You Win")
    else: 
        print("You lost")
elif player_select == "P":
    if computer_select == "R":
        print("You Win")
    else: 
        print("You lost")
        