def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2:
        return False
    if len(s)>7:
        return False
    test = s.isalnum()
    if test == False:
        return False

    if s.isalnum() and len(s) >1 and len(s) <8 and s[0:2].isalpha():
        if s.isalpha():
            return True

        else:
            num = ""
            for char in s:
                if char.isdigit():
                    num += char
                    num = list(num)

            if num[0] == "0":
                return False

            x = s[len(s.rstrip('0123456789')):]
            y = x.isdigit()

            if y != True:
                return False

    index = [x.isdigit() for x in s].index(True)
    right = len(s)

    for char in s[index:right]:
        if char.isdigit():
            continue
        else:
            return False

    return True

main()
