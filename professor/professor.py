import random

def main():
    score = 0
    counter = 0

    level = get_level()
    while counter <10:
        counter +=1
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while tries < 3:
            total = x + y
            print(x,"+",y,"= ", end="")
            try:
                ans=int(input())
                if ans == total:
                    tries = 3
                    score += 1
                if ans != total:
                    tries +=1
                    print("EEE")
                    if tries >2:
                        print(x,"+",y,"=",total)
            except ValueError:
                tries +=1
                print("EEE")
                if tries >2:
                    print(x,"+",y,"=",total)
        continue
    print("Score: ",score)

def get_level():
     while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level <4:
                return level
        except ValueError:
            continue

def generate_integer(level):
    match level:
        case 1:
            num = random.randint(0,9)
        case 2:
            num = random.randint(10,99)
        case 3:
            num = random.randint(100,999)
    return num

if __name__ == "__main__":
    main()
