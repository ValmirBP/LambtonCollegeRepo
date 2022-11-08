
from prettytable import PrettyTable


class color:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightGrey = '\033[37m'
        darkGrey = '\033[90m'
        lightRed = '\033[91m'
        lightGreen = '\033[92m'
        yellow = '\033[93m'
        lightBlue = '\033[94m'
        pink = '\033[95m'
        lightCyan = '\033[96m'
        reset = '\033[0m'

def QuestContinue():
    ask = ''
    while ask == "":
        ask = input("Do you  wanna continue? [Y/N]: ").upper().strip()
        if ask == 'Y':
           return 'Y'

        elif ask == 'N':
           return 'N'

        else: 
            ask = ''
            print(color.red,"BAD INPUT",color.reset)
        
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Question 1: 

# Draw flowchart and write a program 
# Create a program that allows the user to input a list of first names into one array and last names into a parallel array. 
# Input should be terminated when the user enters a sentinel character. The output should be a list of email addresses
#  where the address is of the following form: first.last@mycollege.edu


def assignment6Q1():
    fName= []
    lName= []
    mail = []
    question = 'Y'

    while question == 'Y':
        interaction = input(" \ntype here the First name: ")
        fName.append(interaction)
        interaction2 = input(" \ntype here the last name: ")
        lName.append(interaction2)
        question = QuestContinue()

    for i in range (len(fName)):
        mail.append(fName[i] + "." + lName[i] + "@mycollege.edu")
    print("\n", mail, "\n")

assignment6Q1()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Question 2: 

# Write program 
# Write a program that allows a small business owner to input, 
# in parallel arrays, the type of item, its cost, and the number in stock. 
# The program should output this information in the form of a table. 
# You can assume that columns will be correctly formatted at later time. 
# The output will look something like this:

def assignment6Q2():
    table = PrettyTable(['Item','Cost','Stock'])
    item = []
    iCost = []
    iStock = []
    question = 'Y'

    while question == 'Y':
        interaction1 = input("\ntype here the Type of the item: ")
        interaction2 = input("\ntype here the Item cost: ")
        interaction3 = input("\ntype here the stock of the Item: ")

        item.append(interaction1)
        print(item)
        iCost.append(interaction2)
        print(iCost)
        iStock.append(interaction3)
        print(iStock)
        question = QuestContinue()

    for i in range (len(item)):
        table.add_row([item[i],iCost[i],iStock[i]])
    print(table)
        


assignment6Q2()
