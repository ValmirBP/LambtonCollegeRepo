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
    print(" 2 - Add information's to a new file")
    print(" 3 - add information's to a existing file")
    print(" 4 - view file")
    print(" 5 - Delete file")
    print(" 6 - exit",color.reset)
    print(color.darkGrey, "-"*50, color.reset)
    print (color.yellow,'Enter 1, 2, 3, 4, 5 or 6: ',color.reset, end="")
    return input ()

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
                stdPNumber = input("Type the Phone Number: ").strip().capitalize()
                stdGpaNumber = input("Type the GPA: ").strip().capitalize()
                stdDateBirth = input("Type the Date of Birth: ").strip().capitalize()
                spaceEntrances =  ("-" * 30)
                aFile.writelines(["StudentID: " + stdId + "\n","First Name: " + stdFName +"\n","Last Name: "+ stdLName + "\n","Major: " + stdMajor + "\n","Phone Number: " + stdPNumber + "\n","GPA: " + stdGpaNumber + "\n","Date of Birth: " + stdDateBirth + "\n",spaceEntrances + "\n"])
                add = input("Do you  want to add other? [Y/N]: ").upper()
            aFile.close()
        except OSError:
            print(OSError)
    else:
        print(color.red,f"\nThe file {fileName} already exists, if you want to add something use the menu 2\n", color.reset)

def AddInformationExistFile():

    print(color.green, "Type here the name of the file: ", color.reset, end="")
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
            add = input("Do you  want to add other? [Y/N]: ").upper()
        aFile.close()

    except OSError:
        print(OSError)



def viewFile():
    pass

def deleteFile():
    pass


def main():
    while True:
        choice = menu()

        if choice == '1':
            print(color.green, "\nYou  choose create a new  file",color.reset)
            createNewFile()

        elif choice == '2':
            print(color.green, "\nYou  choose Add information's to a new file",color.reset)
        elif choice == '3':
            print(color.green, "\nYou  choose add information's to a existing file",color.reset)
        elif choice == '4':
            print(color.green, "\nYou  choose view file",color.reset)
        elif choice == '5':
            print(color.green, "\nYou  choose Delete file",color.reset)
        elif choice == '6':
            print(color.orange, "\nYou  choose exit")
            print("Thanks to use my software\n",color.reset)
            break
        else:
            print(color.red,"\n BAD INPUT")
            print(" Please try again\n",color.reset)



