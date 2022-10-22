from random import randint
from turtle import colormode


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

# Question 1: Draw flowchart and write a program 
# Alberta Einstein teaches a business class at Podunk University. To evaluate the students in this class, she has given four tests. 
# It is now the end of the semester and Alberta asks you to Draw flowchart and write a program that inputs each student’s test scores and outputs the average score for each student and the overall
# class average. 

# (Hint: The outer loop should allow for Ms. Einstein to input all the students, one by one, and the inner loop should accept the three exam scores and compute the average for each student.)

def ass5Question1():
    count = 0
    sumStdAvg = 0
    classAvg = 0
    add = 'Y'
    while add == 'Y':
        count += 1
        tot =0
        std = input('Type the name of the student: ')
        print(f'Type the grades the three exams scores for the {std}:')

        for i in range (1,4):
            scr = float(input(f'Type the score {i}: '))
            tot += scr

        avgStd = tot / i
        print(color.green,f"The average of {std} is {avgStd}", color.reset)

        ask = ''
        while ask == "":
            ask = input("Do you  want to add other? [Y/N]: ").upper().strip()
            if ask == 'Y':
                add = 'Y'
                sumStdAvg += avgStd
                print(color.green,f"At this moment the sum of average of each Student is, {sumStdAvg}",color.reset)
                break

            elif ask == 'N':
                add = 'N'
                sumStdAvg += avgStd
                classAvg = sumStdAvg / count
                print(color.green,f"The average of the class is  {classAvg}",color.reset)
                break

            else: 
                ask = ''
                print(color.red,"BAD INPUT",color.reset)
            
    print('DONE')


# ----------------------------------------------------------------------------------------------------------------------------------

# Question 2: programming 
# Write a program that will simulate the process of dealing cards from a 52-card deck by generating 1,000 random integers in the range 1–52. 
# Assume that numbers 1–13 represent clubs, 14–26 represent diamonds, 27–39 represent hearts, and 40–52 represent spades. Display the number of times each suit occurred in the 1,000 “deals.”

def ass5Question2():
    clubs = 0 
    diamonds  = 0 
    hearts = 0 
    spades = 0 

    for i in range(1000):
        r1 = randint(1, 52) 

        if(1<=r1<=13):
            clubs += 1
        
        elif(14<=r1<=26):
            diamonds  += 1

        elif(27<=r1<=39):
            hearts += 1

        else:
            spades += 1

    totalOfSuits = clubs + diamonds + hearts + spades

    print(color.darkGrey,f"Clubs {clubs}",color.reset)
    print(color.darkGrey,f"Spades {spades}",color.reset)
    print(color.red,f"Hearts {hearts}",color.reset)
    print(color.red,f"Diamonds {diamonds} ",color.reset)
    print("-"*20)
    print(color.lightGreen,f"The total of the suits is {totalOfSuits}",color.reset)

ass5Question1()
ass5Question2()