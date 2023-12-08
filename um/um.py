import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = re.findall(r"\b(um)\b", s, re.IGNORECASE)

    return len(counter)



if __name__ == "__main__":
    main()
