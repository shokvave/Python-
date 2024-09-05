#import random
#define a function to roll a dice
#create a dictonary that will have the drawings of dice




import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

    roll = input("Roll dice (y/n): ")

    while roll.lower() == "y":  # Use 'y' for a simpler yes/no check
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"Dice rolled: {dice1} and {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (y/n): ")

    print("Program ended.")  # Program ends when the user chooses not to roll again

roll_dice()
