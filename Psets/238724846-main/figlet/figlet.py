import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

fonts = figlet.getFonts()


if  len(sys.argv) == 1: #Checks for the input if not present assign a random font
    fonts = random.choice(fonts)
    text = input("Input: ")
    figlet.setFont(font=fonts)
    print(figlet.renderText(text))


# Check if the user provided a font option with incorrect syntax
elif (len(sys.argv) == 2 or len(sys.argv) > 3):
    sys.exit("Invaild Usage")


# Check if the provided font is valid and was provided with the correct syntax
elif not (((sys.argv[1] == "-f") or (sys.argv[1] == "--font")) and (sys.argv[2] in fonts)):
    sys.exit("Invaild Usage")

else:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))

