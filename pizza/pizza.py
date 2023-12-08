import sys, csv
from tabulate import tabulate

def main():
    filename = read_argv()
    try:
        with open(filename) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(menu_create(filename), tablefmt="grid",headers="keys"))

def menu_create(filename):
    with open(filename) as csvfile:
        menu = list(csv.DictReader(csvfile, delimiter=","))
        return menu

def read_argv():
    while True:
        try:
            if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
                return sys.argv[1]
            elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
            elif len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            else:
                continue
        finally:
                pass

if __name__ == "__main__":
    main()
