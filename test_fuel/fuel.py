def main():
    x,y = get_input()
    output = convert(x,y)
    result = gauge(output)
    print(result)

def gauge(output):
    match output:
        case 99 | 100:
            return "F"
        case 0 | 1:
            return "E"
        case _:
            return str(output)


def convert(top,bottom):
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


if __name__ == "__main__":
    main()

