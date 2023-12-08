import random

def main(num):
    while True:
        guess = guess_number(num)
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        elif guess == num:
            print("Just right!")
            break
        continue

def guess_number(num):
    while True:
        try:
            guess=int(input("Guess: "))
            if guess >= 0:
                return guess
        except ValueError:
            continue

def level_select():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level <101:
                return level
        except ValueError:
            continue

num = random.randint(1,level_select())
main(num)
