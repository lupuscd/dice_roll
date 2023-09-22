import random

def roll_dice():
    
    while True:
        roll = input('Roll the dice? (y/n): ')

        if roll.lower() == 'y':
            while True:
                dice = random.randint(1,6)
                print(dice)
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