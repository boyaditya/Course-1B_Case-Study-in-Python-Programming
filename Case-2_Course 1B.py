# • You roll two six-sided dice, each with faces containing one, two, three, four, five and six spots, respectively. When the dice come to rest, the sum of the spots on the two upward faces is calculated.

# • If the sum is 7 or 11 on the first roll, you win. If the sum is 2, 3 or 12 on the first roll (called “craps”), you lose (i.e., the “house” wins).

# • If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your “point.” To win, you must continue rolling the dice until you “make your point” (i.e., roll that same point value). You lose by rolling a 7 before making your point.

import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_game():
    point = 0
    first_roll = roll_dice()
    print(f"First roll: {first_roll}")

    if first_roll in [7, 11]:
        print("You win!")
    elif first_roll in [2, 3, 12]:
        print("You lose (craps)!")
    else:
        point = first_roll
        print(f"Your point is {point}")
        while True:
            roll = roll_dice()
            print(f"Roll: {roll}")
            if roll == point:
                print("You win!")
                break
            elif roll == 7:
                print("You lose!")
                break

if __name__ == "__main__":
    play_game()
