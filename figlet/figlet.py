from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

if len(sys.argv) == 3:
    match sys.argv[1]:
        case "-f" | "--font":
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font = sys.argv[2])
                print(figlet.renderText(input("Input: ")))
            else:
                sys.exit("Invalid Usage")
        case _:
            sys.exit("Invalid Usage")

elif len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))
    print(figlet.renderText(input("Input: ")))
else:
    sys.exit("Invalid Usage")
