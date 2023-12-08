def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    result =""
    for letter in word:
        match letter.lower():
            case  "a" | "e" | "i" | "o" | "u":
                 continue
            case _:
                result += letter
    return(result)

if __name__ == "__main__":
    main()
