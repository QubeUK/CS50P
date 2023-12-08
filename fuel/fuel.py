def main():
    x,y = get_input()
    output = con(x,y)

    match output:
        case 99 | 100:
            print("F")
        case 0 | 1:
            print("E")
        case _:
            print(output,"%" ,sep="")

def con(top,bottom):
    while True:
        try:
            result = round((top / bottom) * 100)
        except ZeroDivisionError:
                top,bottom = get_input()
        else:
            if result > 100:
                top,bottom = get_input()
            else:
                return result

def get_input():
    while True:
            try:
                f = input("Fraction: ").split("/")
                x = int(f[0])
                y = int(f[1])
            except ValueError:
                pass
            else:
                return x,y

main()
