'''
Assignment 6_7
Student: Valmir de Barros Pedro
Student Number:C0868075 

'''

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

# 1) Create a list variable with the following data:
# head heartbreaking mark aboriginal
# activity valuable overjoyed abandoned
# snail tip

aList = ["head" ,"heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
print (color.red, '\n1)' ,color.green, ' Original:',color.reset)
print (aList)
print ('\n')

# 2) Add a word to the beginning of the list
aList.insert(0,"VALMIR")
print (color.red, '2)',color.green,'Add Valmir in 1st position',color.reset)
print (aList)
print ('\n')

# 3) Delete the 7th index of the list.
aList.pop(7)
print (color.red, '3)',color.green,'deleting 7th index overjoyed',color.reset)
print (aList)
print ('\n')

# 4) Delete the entry “valuable”
def removePop():
    aList = ["head" ,"heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    aList.pop(6)
    print (color.red, '4)',color.green,'deleting valuable Using pop()',color.reset)
    print (aList)
    print ('\n')
removePop()

def removeRemoveFunc():
    aList = ["head" ,"heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    print (color.red, '4)',color.green,'deleting valuable Using remove()',color.reset)
    aList.remove('valuable')
    print (aList)
    print ('\n')
removeRemoveFunc()

# 5) Search for the value “boo”. Delete it if found
def findBooFalse():
    print (color.red, '5)',color.green,'searching boo in list False',color.reset)
    if "boo" in aList:
        aList.remove('boo')
        print("boo found and removed")
        print ('\n')
    else:    
        print(color.red,"boo not found in this list",color.reset)
        print ('\n')

findBooFalse()        

def findBooTrue():
    aList = ["head" ,"heartbreaking" ,"mark" ,"aboriginal" ,"activity","boo" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    print (color.red, '5)',color.green,'searching boo in list True:\n',color.reset)
    if "boo" in aList:
        print(color.green,"boo found at" ,aList.index('boo') ,"position of the list and removed",color.reset)
        aList.remove('boo')
        print(aList)
        print ('\n')
    else:    
        print("boo not found in this list")
        print ('\n')

findBooTrue()

