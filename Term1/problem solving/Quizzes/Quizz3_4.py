def readFromFile(months, savings):
    savingsFile = open("savings1.txt",'r')
    lines = savingsFile.readlines()
    for line in lines:
        print(line)
    savingsFile.close()


def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:
        print("Enter NOT GREEN energy costs for", months[counter])
        notGreenCosts[counter] = float(input())
        counter += 1

def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 12:
        print("Enter GONE GREEN energy costs for", months[counter])
        goneGreenCosts[counter] = float(input())
        counter += 1


def energySaved(notGreenCost,goneGreenCost,savings):
    counter = 0
    while counter < 12:
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter = counter + 1



def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < 12:
        print("Information for", months[counter])
        print("Savings $", savings[counter])
        print("Not Green Costs $", notGreenCost[counter])
        print("Gone Green Costs $", goneGreenCost[counter])




def main():
    endProgram = "no"
    notGreenCost = [None] * 12
    goneGreenCost = [None] * 12
    savings = [None] * 12
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    option = 0
    while endProgram == "no":
        if option == 1:
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCost, months)
            energySaved(notGreenCost, goneGreenCosts, savings)
        elif option == 2:
            displayInfo(notGreenCost, goneGreenCosts, savings, months)
        elif option == 3:
            writeToFile(months, savings)
        elif option == 4:
            readFromFile(months, savings)
            print("Do you want to end the program? Yes or no")
    endProgram = str(input())



def writeToFile(months, savings):
    savingsFile = open("savings1.txt",'a')
    savingsFile.write("Savings\n")
    counter = 0
    while counter < 12:
        savingsFile.write(months[counter])
        savingsFile.write(savings[counter])
        savingsFile.write('\n')
        counter += 1
    savingsFile.close()

main()


