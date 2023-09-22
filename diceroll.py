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
    
    while True:
        roll = input('Roll the dice? (y/n): ')

        if roll.lower() == 'y':
            while True:
                dice = random.randint(1,6)
                print('\n'.join(dice_drawing[dice]))
                roll_again = input('Roll again? (y/n): ')
                if roll_again.lower() != 'y':
                    break
            if roll_again.lower() == 'n':
                break
            else:
                print('Please reply with y or n!')
        elif roll.lower() == 'n':
            break
        else: 
            print('Please reply with y or n!')

roll_dice()