import inflect
p = inflect.engine()

def main():
    output=[]
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            mylist = p.join((output))
            print("Adieu, adieu, to",mylist)
            break
        output.append(name)

        pass

main()
