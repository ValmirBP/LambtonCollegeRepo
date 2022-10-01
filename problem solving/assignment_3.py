
from cmath import sqrt


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

#         Question 1: 
# Consider the equation Ax2 + B = 0.
# 	If B/A < 0, this equation has two solutions. The solutions are:

# (1) X1 = Sqrt(–B/A)
# (2) X2 = −Sqrt(–B/A)

# 	If B/A = 0, this equation has one solution which is X = 0
# 	If B/A > 0, this equation has no real number solutions

# Draw a flowchart and Write a program to have the user input any numbers for the coefficients, A and B, for this equation. If A = 0, terminate the program. Otherwise, solve the equation.

# ----------------------------------------------------------------------------------------------------------------------------------------
def ass2Question1():
    while True:
        print(color.cyan,"question1\n".upper(), color.reset)
        print(color.cyan,"Consider the equation Ax2 + B = 0. If B/A < 0, this equation has two solutions. The solutions are:\n", color.reset)
        print(color.cyan,"(1) X1 = Sqrt(–B/A): \n (2) X2 = −Sqrt(–B/A)\n", color.reset)
        print(color.cyan,"If B/A = 0, this equation has one solution which is X = 0\n If B/A > 0, this equation has no real number solutions\n", color.reset)
        print(color.cyan,"Draw a flowchart and Write a program to have the user input any numbers for the coefficients, A and B, \nfor this equation. If A = 0, terminate the program. Otherwise, solve the equation.\n", color.reset)

        varA = float(input("Type here the Value of the Variable A: "))
        varB = float(input("Type here the Value of the Variable B: "))

        if varB/varA < 0 :
            x1 = sqrt(-varA/varB)
            x2 = -sqrt(-varA/varB)

            print(color.green,f"The two points of this Parable are {x1} and  {x2}", color.reset)
            break
        elif varB/varA == 0 :
            print(color.red,f"sorry impossible to calculate", color.reset)
            break
        elif varB/varA > 0 :
            print(color.red,f"There is no real solutions", color.reset)
        elif varA == 0 :
            print(color.red,f"sorry impossible to calculate", color.reset)
            break

# ----------------------------------------------------------------------------------------------------------------------------------------

# Write a program that allows the user to input a total dollar amount for an online shopping order and computes and outputs the shipping cost 
def ass2Question2():
    shoppingAmount = float(input("Type here the amount of the shop you´ve done: "))

    if shoppingAmount <= 50 :
        shipUSA = 6.00
        shipCA = 8.00
        print(color.blue,f"\nThe shipment to  USA is ${shipUSA} and to  Canada is ${shipCA}",color.reset)
    elif shoppingAmount >= 50.01 and shoppingAmount <= 100:
        shipUSA = 9.00
        shipCA = 12.00
        print(color.cyan,f"\nThe shipment to  USA is ${shipUSA} and to  Canada is ${shipCA}",color.reset)
    elif shoppingAmount >= 100.01 and shoppingAmount <= 150:
        shipUSA = 12.00
        shipCA = 15.00
        print(color.yellow,f"\nThe shipment to  USA is ${shipUSA} and to  Canada is ${shipCA}",color.reset)
    else:
        shipUSA = "FREE"
        shipCA = "FREE"
        print(color.green,f"\nThe shipment to  USA is {shipUSA} and to  Canada is ${shipCA}",color.reset)


ass2Question1()
ass2Question2()


