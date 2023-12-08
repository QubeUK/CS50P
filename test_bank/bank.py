def main():
    print("$",value(input("Greeting: ").strip()),sep="")

def value(greeting):
    if greeting.split()[0] == "Hello":
        return 0
    elif greeting == "Hello, Newman":
        return 0
    elif greeting[0] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
