from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit('Invalid usage')

response = input('Input: ')
print(figlet.renderText(response))
