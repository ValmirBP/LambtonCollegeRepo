'''
Test 2
Student Valmir  de Barros Pedro
Student Number C0868075
FSDT  Fall  2022
CSD 1133 Problem Solving/Program Logic
'''

# 1.	Write a Python Program to Swap the First and Last Value of a List.


def SwapList():
    aList = []x
    n = int(input("Type here the number of the elements: "))

    for x in range(0, n):
        element = int(input("Enter here the " + str(x+1) + " number "+": "))
        aList.append(element)

    print("\n")
    print("list is:")
    print(aList)
    print("\n")

    temp = aList[0]
    aList[0] = aList[n-1]
    aList[n-1] = temp

    print("New list is:")
    print(aList)
    print("\n")


SwapList()

# 2.Write a Python Program to Count the Number of Vowels in a String.


def ContVowels():
    word = input("Enter string: ").strip().upper()
    vowels = 0

    for i in word:
        if (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels+1

    print("\n")
    print("The word is:")
    print(word)
    print("\n")

    print("The number of vowels is:")
    print(vowels)
    print("\n")


ContVowels()

# 3.	Write a Python Program to Check Common Letters in Two Input String.


def commonLetters():

    print("\n")
    word1 = input("Type here the first string: ").strip()
    word2 = input("Type here the second string: ").strip()

    aList = list(set(word1) & set(word2))

    print("\n")
    print(f"The first string typed was {word1}")
    print(f"The second string typed was {word2}")
    print("\n")
    print("The common letters are:")

    for i in aList:
        print(i)

# commonLetters()

# 4.	Write a program to find the average of numbers in a list in Python.


def avgNumbers():
    qndtyNum = int(input("Type here the quantity of numbers: ").strip())
    aList = []

    for i in range(0, qndtyNum):
        elem = int(input("type the number: "))
        aList.append(elem)

    average = sum(aList)/qndtyNum

    print(f"The Average of the list is {round(average,2)}")


avgNumbers()

# 5.	Write a Python Program to Count the Number of Digits in a Number.


def contNumbersInNumber():

    number = int(input("Type here the number: ").strip())
    count = 0

    while (number > 0):
        count = count+1
        number = number//10

    print(f"The number of digits {count}")


contNumbersInNumber()

# 6.Write a Python Program to take three integers from user and
# returns true if these three integers represent the three edges
# of a right-angle triangle.


def Triplets(a, b, c):

    if (a <= 0 or b <= 0 or c <= 0):
        return False

    vec = [a, b, c]
    vec.sort()
    a = vec[0]
    b = vec[1]
    c = vec[2]

    if (a + b <= c):
        return False
    p1 = a
    p2 = c - b

    div = __gcd(p1, p2)
    p1 //= div
    p2 //= div
    q1 = c + b
    q2 = a

    div = __gcd(q1, q2)
    q1 //= div
    q2 //= div

    return (p1 == q1 and p2 == q2)


def righAngleRect(a, b, c):

    if (Triplets(a, b, c)):
        return "Yes, it is a right angle rectangle"
    else:
        return "No, it is NOT a right angle rectangle"


def __gcd(a, b):
    if (b == 0):
        return a
    return __gcd(b, a % b)


a = int(input("type here a side 1 of a Triangle: ").strip())
b = int(input("type here a side 2 of a Triangle: ").strip())
c = int(input("type here a side 3 of a Triangle: ").strip())
print("\n")

print(righAngleRect(a, b, c))
