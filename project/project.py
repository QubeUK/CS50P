from dataclasses import dataclass
from random import randint

@dataclass
class DiceFactory:
    name: str
    value: int
    save: bool = False

    def roll(self):
        self.value = randint(1,6)

def main():
    dice=create_dice()
    roll_again = "y"
    score = 0
    roll = 0
    while roll_again == "y" and roll <3:
        roll +=1
        roll_dice(dice)
        d2p=get_dice(dice)
        print(f"\n{'='*21}\n {d2p}\n{'='*21}")
        print(f"Number of rolls: {roll}")
        dice, score = check_dice(dice, score)
        if roll <3:
            roll_again = input("\nPress 'Y' to roll the dice again: ").lower()
    if score == 0:
        print(f"\nYou failed to secure as Captain, Ship and Cargo and are left with {score} gold.\n")
    else:
       print(f"\n{'='*28}\n Final Cargo Value: {score} gold\n{'='*28}\n")
    return

def check_dice(dice, score):
    current_roll = []
    current_roll.clear()
    for i in range(5):
        current_roll.append(dice[i].value)

    if 6 in current_roll:
        print(f"\n[6] A Captain has been found!")
        dice[0].value = 6
        dice[0].save = True

    if 6 in current_roll and 5 in current_roll:
        print(f"[5] The Captain has secured a ship!")
        dice[1].value = 5
        dice[1].save = True

    if 6 in current_roll and 5 in current_roll and 4 in current_roll:
        score = sum(current_roll)-15
        print("[4] The Captain has hired a crew!")
        if score == 12:
            print(f"\nCurrent cargo is worth {score}, that's the largest haul I've ever seen!")
        else:
            print(f"\nCurrent cargo of barrels is worth {score} gold!")
        dice[2].value = 4
        dice[2].save = True
    return dice, score

def roll_dice(dice):
    for i in range(5):
        if dice[i].save == False:
            dice[i].roll()
    return dice

def get_dice(dice):
    d2p = ""
    for i in range(5):
        d2p += (f"[{dice[i].value}] ")
    return d2p

def create_dice():
    dice=[]
    for i in range(5):
        dice.append(DiceFactory(f"d{i+1}",0,False))
        dice[i].roll()
    return dice

if __name__ == "__main__":
    main()
