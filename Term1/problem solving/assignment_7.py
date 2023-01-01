'''
Student: Valmir de Barros Pedro
Student Number: C0868075
Assignment_7
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

'''
Question 1: 

Pseudo code and Programming
Given the following array, write a pseudo code and program to sort
the array using a selection sort and display the number of scores 
that are less than 500 and those greater than 500.

Scores[0] = 198 Scores[1] = 486 Scores[2] = 651
Scores[3] = 85 Scores[4] = 216 Scores[5] = 912
Scores[6] = 73 Scores[7] = 319 Scores[8] = 846
Scores[9] = 989
'''

def question1ass7():

    scores = [198, 486, 651, 85, 216, 912, 73, 319, 846, 989]
    print('-' * 50)
    print(color.green,'Scores: ',color.reset)
    print(scores)
    print('\n')

    for i in range(len(scores)-1):
        min = i
        for j in range(i+1,len(scores)):    
            if scores[j] < scores[min]:
                min = j
        if(min != i):
            scores[i], scores[min] = scores[min], scores[i]
    print(color.red,'Sorted scores:',color.reset)
    print(scores)
    print('\n')

    i = 0
    while i < len(scores) and scores[i] < 500:
        i += 1

    print(color.cyan,f'Scores  less than 500  = {i}', color.reset)
    print(color.cyan,f'Scores greater than or equal to 500: = {len(scores)-i}',color.reset)
    print('-' * 50)

# question1ass7()

'''
Question 2: 

Programming
Write a program to load an array, Squares, with 100 numbers. 
Each element should contain the square of its index value. 
In other words, 
Squares[0] = 0, Squares[3] = 9, Squares[8] = 64, and so on. 
Then prompt the user for a number from 0 through 1000 and write 
pseudo code to check if that number is a perfect square 
(i.e., if the user inputs X, check to see if X is a value in the array). 
Use a serial search for this program.

'''
def question2Ass7():
    aArray=[]
    for i in range(0,100):
        aArray.append(i*i)
        
    number=int(input("Type a Number between 0 to 1000: ")) 

    if number <= 1000:
        for i in range(len(aArray)):
            if aArray[i] == number:  
                print(color.green ,"This number is a perfect square" ,color.reset)
                exit()
        print(color.red, "This isn´t a Perfect Square" ,color.reset)
    elif number < 0:
        raise Exception("Sorry, Number can not be Negative")
    else:
        raise Exception("Sorry, Number Bigger than 10000")
              

question2Ass7()            