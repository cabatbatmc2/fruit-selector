#9/02/26: Fruit Selector
from easygui import *
import sys 

def main_program():
    fruit = buttonbox("1 = Apple\n2 = Banana\n3 = Feijoa\n4 = Kiwi fruit \n5 = Quit", choices= ["1", "2", "3", "4", "5"])

    if fruit == "1":
        msgbox("You chose an apple.")
        
    elif fruit == "2":
        msgbox("You chose a banana")

    elif fruit == "3":
        msgbox("You chose a feijoa")

    elif fruit == "4":
        msgbox("You chose a kiwi fruit")

    else:
        msgbox("Thank you for making healthy choices. See you next time!")
        sys.exit(0)

while True:
    main_program()
    repeat = buttonbox("Would you like to select another fruit?", choices = ["Yes", "No"])

    if repeat != "Yes":
        msgbox("Thank you for making healthy choices. See you next time!")
        break

