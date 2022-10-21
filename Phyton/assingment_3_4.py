from asyncore import read
from datetime import date
from fileinput import filename
from gettext import find
import os

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

print("Create a python application that inputs, processes, and stores student data using menu-driven programming")

def menu():
    print(color.darkGrey, " MENU ".center(50,"-"), color.reset)
    print(color.blue,"1 - Create a new  file")
    print(" 2 - Add information's to a existing file")
    print(" 3 - View file")
    print(" 4 - Find on file")
    print(" 5 - Exit",color.reset)
    print(color.darkGrey, "-"*50, color.reset)
    print (color.yellow,'Enter 1, 2, 3, 4, or 5: ',color.reset, end="")
    return input ()

def formatPhoneNumber():
    while True:
        phone=input("Type the Phone Number:")
        if len(phone) <= 10:
            phoneFormatted = ( phone[0:3] + "-" +  phone[3:6] + "-" + phone[6:10])
            break
        else:
            print("phone is bigger than 10 chars please check the number")
    return phoneFormatted

def createNewFile():
    
    print(color.green, "Type here the name of the file: ", color.reset, end="")
    fileName = input() + ".txt" .strip()
    add = "Y"
    if not os.path.exists(fileName):
        try:
            aFile = open(fileName,'w')
            while add == "Y":
                stdId = input("Type the Student ID: ").strip().capitalize()
                stdFName = input("Type the First Name: ").strip().capitalize()
                stdLName = input("Type the Last Name: ").strip().capitalize()
                stdMajor = input("Type the major: ").strip().capitalize()
                stdPNumber = formatPhoneNumber()
                stdGpaNumber = input("Type the GPA: ").strip().capitalize()
                stdDateBirth = input('Type the Date of Birth (month,day,year):')
                spaceEntrances =  ("-" * 30)
                aFile.writelines(["StudentID: " + stdId + "\n","First Name: " + stdFName + "\n","Last Name: "+ stdLName + "\n","Major: " + stdMajor + "\n","Phone Number: " + stdPNumber + "\n","GPA: " + stdGpaNumber + "\n","Date of Birth: " + stdDateBirth + "\n",spaceEntrances + "\n"])
                ask = ''

                while ask == "":
                    ask = input("Do you  want to add other? [Y/N]: ").upper().strip()
                    if ask == 'Y':
                        add = 'Y'
                        break
                    elif ask == 'N':
                        add = 'N'
                        break
                    else: 
                        ask = ''
                        print(color.red,"BAD INPUT",color.reset)

            aFile.close()
        except OSError:
            print(OSError)
    else:
        print(color.red,f"\n The file {fileName} already exists, if you want to add something use the menu 2\n", color.reset)

def addInformationExistFile():
    print(color.green, " Type here the name of the file: ", color.reset, end="")
    fileName = input() + ".txt" .strip()
    add = "Y"

    try:
        aFile = open(fileName,'a')

        while add == "Y":
            stdId = input("Type the Student ID: ").strip().capitalize()
            stdFName = input("Type the First Name: ").strip().capitalize()
            stdLName = input("Type the Last Name: ").strip().capitalize()
            stdMajor = input("Type the major: ").strip().capitalize()
            stdPNumber = input("Type the Phone Number: ").strip().capitalize()
            stdGpaNumber = input("Type the GPA: ").strip().capitalize()
            stdDateBirth = input("Type the Date of Birth: ").strip().capitalize()
            spaceEntrances =  ("-" * 30)
            aFile.writelines(["StudentID: " + stdId + "\n","First Name: " + stdFName +"\n","Last Name: "+ stdLName + "\n","Major: " + stdMajor + "\n","Phone Number: " + stdPNumber + "\n","GPA: " + stdGpaNumber + "\n","Date of Birth: " + stdDateBirth + "\n",spaceEntrances + "\n"])
            ask = ''

            while ask == "":
                ask = input("Do you  want to add other? [Y/N]: ").upper().strip()
                if ask == 'Y':
                    add = 'Y'
                    break
                elif ask == 'N':
                    add = 'N'
                    break
                else: 
                    ask = ''
                    print(color.red,"BAD INPUT",color.reset)
        aFile.close()

    except OSError:
        print(OSError)
        
def viewFile():
    print(color.green,"Type here the name of the file, You want to view: ", color.reset, end="")
    fileName = input() + ".txt" .strip()

    if not os.path.exists(fileName):
        print(color.red,f"The document {fileName}, do not exist in this folder",color.reset)
    else:
        print(color.yellow,"Document: \n",color.reset)
        aFile = open(fileName,'r')
        out = aFile.readlines()
        for lines in out:
            print(lines.strip("\n"))
        aFile.close()

def findOnFile():
        print(color.green,"Type here the name of the file, You want to view: ", color.reset, end="")
        fileName = input() + ".txt" .strip()

        if not os.path.exists(fileName):
            print(color.red,f"The document {fileName}, do not exist in this folder",color.reset)

        else:    
            print(color.green,"Type here the nStudent id that you  looking for : ", color.reset, end="")
            stdIdFind = "StudentID: " + input().strip()
            print(color.yellow,"\n Document: \n",color.reset)

            with open(fileName,'r') as aFile :
                read = aFile.readlines()

                for line in read:
                    if line.find(stdIdFind) != -1:
                        findIdxLine = read.index(line)

                for i in range(findIdxLine,(findIdxLine+7)):
                    print(color.cyan,read[i].strip("\n"), color.reset)
            aFile.close()

def main():
    while True:
        choice = menu()

        if choice == '1':
            print(color.green, "\n You  choose create a new  file",color.reset)
            createNewFile()

        elif choice == '2':
            print(color.green, "\n You  choose add information's to a existing file",color.reset)
            addInformationExistFile()

        elif choice == '3':
            print(color.green, "\n You  choose view file",color.reset)
            viewFile()

        elif choice == '4':
            print(color.green, "\n You  choose find on file",color.reset)
            findOnFile()

        elif choice == '5':
            print(color.orange, "\n You  choose exit")
            print("Thanks to use my software\n",color.reset)
            break

        else:
            print(color.red,"\n BAD INPUT")
            print(" Please try again\n",color.reset)

main()