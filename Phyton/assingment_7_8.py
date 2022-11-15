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
print (color.red, '3)',color.green,'deleting 7th index overjoyed',color.reset)
print(color.green,"BEFORE:",color.reset)
print(aList)
aList.pop(7)
print(color.red,"AFTER:",color.reset)
print (aList)
print ('\n')

# 4) Delete the entry “valuable”
def removePop():
    aList = ["head" ,"heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    aList.pop(5)
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
    print(aList)
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
    print ('\n')
    print (color.red, '5)',color.green,'searching boo in list True:\n',color.reset)
    print(aList)
    if "boo" in aList:
        print(color.green,"boo found at" ,aList.index('boo') ,"position of the list and removed",color.reset)
        aList.remove('boo')
        print(aList)
        print ('\n')
    else:    
        print("boo not found in this list")
        print ('\n')

findBooTrue()

# 6) Add any value after the item “activity”
def  addWithNoLoop():
    aList = ["head","heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    print(color.red,"6)",color.green,"adding a C0868075 after activity coded",color.reset)
    print(color.green,"BEFORE:",color.reset)
    print(aList)
    aList.insert(5,"C0868075")
    print(color.red,"AFTER:",color.reset)
    print(aList)
    print ('\n')

addWithNoLoop()

def addWithLoop():
    aList = ["head","heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
    print(color.red,"6)",color.green,"adding a C0868075 after activity using loop",color.reset)
    print(color.green,"BEFORE:",color.reset)
    print(aList)

    for i in range  (len(aList)):
        if aList[i] == 'activity':
            aList.insert(i+1, "C0868075")

    print(color.red,"AFTER:",color.reset)
    print(aList)
    print ('\n')

addWithLoop()

# 7) Output every other value of the list starting with index 1 using a loop
aList = ["head","heartbreaking" ,"mark" ,"aboriginal" ,"activity" ,"valuable" ,"overjoyed" ,"abandoned" ,"snail" ,"tip"]
print(color.red,"7)",color.green,"Printing the array stating with index 1 it takes out the head ",color.reset)
for index in range(1, len(aList)):
    print(aList[index],end=", ")
print ('\n')

# -----------------------------------------------------

# 1) Ask the user for 3 numbers
print(color.red,'1)',color.green,'Asking for  3 numbers\n')


n1 = int(input ('Enter First number:'))
n2 = int(input('Enter Second number:'))
n3 = int(input('Enter Third number:'))

print (" \n You  entered \n", n1,n2,n3)


# 2) Using a loop,
# a) Start from either the first or second number
# b) End at either the first or second number (inclusive)
# c) Increment or decrement by the third number.
# d) Output the number AND the cubed value of the number

def quest2LoopWhile():
    '''
    Using a While loop the is needed to have a control variable,
    in this case was used the n1, and checked bigger than the 
    second number the number printing the cubed of first number
    summing the first to  the second   
    evaluating is the third number is positive or negative to decide if starts with
    first or second number
    '''
    print(color.red,'2)',color.green,'Using the 3 numbers in a While loop: \n',color.reset)
    if n3 > 0 :
        start = n1  #a
        while start <= n2: #b
            print(color.cyan ,start,'cubed is', start ** 3, color.reset) #d
            start += n3  #c
        print('\n')
    else:
        start = n2  #a
        while start >= n1 : #b
            print(color.cyan ,start,'cubed is', start ** 3, color.reset) #d
            start += n3  #c
        print('\n')

quest2LoopWhile()

def quest2LoopFor():
    '''
    Using a for  loop  and the range() function
    the first  is the condition to start the 
    second one is for takes the inclusive range 
    or the range of interactions, the third one is the
    step, so how many steps it will jump is possible to do without
    the third  number due to  the default of the this is 1.
    evaluating is the third number is positive or negative to decide if starts with
    first or second number
    '''
    if n3 > 0 :
        print(color.red,'2)',color.green,'Using the 3 numbers in a For loop using  range() function: \n',color.reset)
        # >>>>>>>>>>>> #a   #b   #c
        for i in range(n1, n2, n3):
            print(color.cyan ,f'{i} cubed is {i**3}' ,color.reset)
        print('\n')
    else:
        print(color.red,'2)',color.green,'Using the 3 numbers in a For loop using  range() function: \n',color.reset)
        # >>>>>>>>>>>> #a   #b   #c
        for i in range(n2, n1, n3):
            print(color.cyan ,f'{i} cubed is {i**3}' ,color.reset)
        print('\n')

quest2LoopFor()