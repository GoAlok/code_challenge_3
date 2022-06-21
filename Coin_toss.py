"""
    Instruction:
        Write program for a virtual coin toss. That will give heads and tails.
"""

import random

coin_toss = random.randint(0,1)

if coin_toss == 0:
    print("Head")
else:
    print("Tails")
