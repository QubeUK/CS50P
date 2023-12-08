input = input("Input: ")

for letter in input:
    match letter.lower():
        case  "a" | "e" | "i" | "o" | "u":
             print("", end="")
        case _:
            print(letter,end="")
print()
