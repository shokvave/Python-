#import random
#define a function to roll a dice
#create a dictonary that will have the drawings of dice
#

import random


def roll_dice():
    
    roll = input("Roll dice (y/n): ")

    while roll.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(dice1, dice2))

    roll = input("roll again? (y/n): ")

roll_dice()

