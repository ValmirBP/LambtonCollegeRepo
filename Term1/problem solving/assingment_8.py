import random

'''
Student: Valmir de Barros Pedro
Student Number: C0868075
Assignment_8
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

def names():
    name = input("Enter Student Name: ")
    return name

def getterNumbers():
    num1 = random.randrange(1, 500)
    num2 = random.randrange(1, 500)
    return num1, num2

def getterSum(num1, num2, ans):
    print("What is the answer to the following equation")
    print(str(num1) + "\n+\n" + str(num2))
    print("What is the sum", sep = ': ')
    ans = int(input())
    return ans

def answerChecker(num1, num2, ans, right):
    if ans == num1 + num2:
        print("Right")
        right = right + 1
    else:
        print("Wrong")
    return right

def results(right, averageRight):
    averageRight = right/10
    return averageRight

def displayInfo(right, averageRight, studentName):
    print("Infomation for student: "+studentName)
    print("The number right: "+str(right))
    print("The average right is "+str(averageRight)+" or "+str(averageRight*100)+" %")


def main():
    c = 0
    studentName = "NO NAME"
    averageRight = 0.0
    right = 0

    num1 = 0
    num2 = 0
    ans = 0
    studentName = names()

    while c < 10:
        num1, num2 = getterNumbers()
        ans = getterSum(num1, num2, ans)
        right = answerChecker(num1, num2, ans, right)
        c = c + 1
        averageRight = results(right, averageRight)
    
    displayInfo(right, averageRight, studentName)

    
main()