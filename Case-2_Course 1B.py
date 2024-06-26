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
