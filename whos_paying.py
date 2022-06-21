"""
    Instruction:
        Write a program which selects random name from a list . The person selected will have 
        to pay everybody's food bill.
        
    Hint:
        You can use str.split(',')  to separate item from string
        Do not use random.choice()
"""

import random


print("Some names for testing are: \n alok, raj, james, angela, boopati, sama, samir, sahid, mira, birendra")
name_string = input("Give me everybody's name, separated by comma(,). ")

name = name_string.split(", ")
print(type(name))
print(name)

random_choice = random.randint(0, len(name)-1)
print((name[random_choice]).capitalize())