from math import factorial


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

# ----------------------------------------------------------------------------------------------------------------------------------------

# Question 1: Draw flowchart and write pseudo code and program 
# The number N factorial, denoted by N!, is defined to be the product of the first N positive integers:

# N! = 1 × 2 × . . . × N
# For example:

# 5! = 1 × 2 × 3 × 4 × 5 = 120
# 7! = 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5,040

# Find N! where N is a positive integer input by the user.
# (Hint: initialize a Product to 1 and use a loop to multiply that Product by successive integers.)

# Be sure to check that the user enters a positive integer.

# ----------------------------------------------------------------------------------------------------------------------------------------
# SOLUTION:

def ass4Question1():
    print("Question 1: ".upper())
    print("The number N factorial, denoted by N!, is defined to be the product of the first N positive integers")
    print("N! = 1 × 2 × . . . × N")
    print("For example:")
    print("5! = 1 × 2 × 3 × 4 × 5 = 120")
    print("7! = 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5,040")
    print("Find N! where N is a positive integer input by the user.\n ")

    nFActorial = int(input("Type  here the number, it will show the factorial : "))
    count = 1
    calc = 1

    if factorial <= 0:
        print(f" The result of factorial is 1")
    else:
        while count <= nFActorial:
            calc *= count
            count += 1
        print(f" The result of factorial is{calc}")

ass4Question1()

# ----------------------------------------------------------------------------------------------------------------------------------------
# Question 2: programming  
# A biologist determines that the approximate number, Number, of bacteria present in a culture after a certain number of days, Time, is given by the following formula:

# Number = BacteriaPresent * 2ˆ(Time/10)

# where BacteriaPresent is the number present at the beginning of the observation period. Let the user input BacteriaPresent, 
# the number of bacteria present at the beginning. 
# Then compute the number of bacteria in the culture after each day for the first 10 days. Do this in a loop so that the user can see the results in a table. 
# The output table should have headings for Day and Number of Bacteria Present (on that day).


# ----------------------------------------------------------------------------------------------------------------------------------------
# SOLUTION:

def ass4Question2():
    print(color.red, "Question 2:".upper(), color.reset)
    print(color.green, "A biologist determines that the approximate number, Number, of bacteria present in a culture after a certain number of days, Time, is given by the following formula:", color.reset)
    print(color.yellow, "Number = BacteriaPresent * 2ˆ(Time/10) \n", color.reset)

    BacteriaPresent = int(input("Type here the Actual number of the colony :"))
    Time = int(input("Type here the time in days :"))
    count = 1
    print(color.cyan,f" Day {count}: The Colony of the bacteria on first day is {BacteriaPresent}", color.reset)

    while count < Time:
        count += 1
        Number = BacteriaPresent * 2**(count/10)
        print(color.cyan,f" Day {count}: {Number:.2f}", color.reset)

ass4Question2()
    