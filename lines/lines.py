import sys

def main():
    filename = read_argv()

    try:
        with open(filename) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
       print(count_lines(filename))


def count_lines(filename):
    with open(filename) as file:
        counter = 0
        for line in file:
            if line.startswith("\n") or line.isspace() or line.lstrip().startswith("#"):
                continue
            else:
                counter +=1
    return counter

def read_argv():
    while True:
        try:
            if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
                return sys.argv[1]
            elif len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            else:
                sys.exit("Not a Python file")
        finally:
            pass


if __name__ == "__main__":
    main()
