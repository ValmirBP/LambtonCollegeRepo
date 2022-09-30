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

# Question 1:
# Prompt for and input a saleswoman’s sales for the month (in dollars) and her commission rate (as a percentage). Output her commission for that month. Note that you will need to convert the percentage to a decimal. You will need the following variables: 
# SalesAmount 		CommissionRate	 CommissionedEarned 
# You will need the following formula: 
# CommissionedEarned = SalesAmount * (CommissionRate/100)

# ----------------------------------------------------------------------------------------------------------------------------------------
def question1():

    print(color.lightCyan,"\n Question 1:".upper(),color.reset)
    print(color.lightCyan, "Prompt for and input a saleswoman’s sales for the month (in dollars) and her commission rate (as a percentage). Output her commission for that month. Note that you will need to convert the percentage to a decimal.", color.reset)

    salesAmount = float(input("\n Type the Amount of sales: "))
    commissionRate = float(input("Type the commission rate here: "))
    commissionedEarned  = salesAmount *(commissionRate/100)

    print (color.blue,f" The Commission earned is $ {commissionedEarned:.2f} Dollars")

# ----------------------------------------------------------------------------------------------------------------------------------------

# Question 2:
# The manager of the Super Supermarket would like to be able to compare the unit price for products sold there. To do this, the program should input the name and price of an item per pound and its weights in pounds and ounces. Then it should determine and display the unit price (the price per ounce) of that item and the total cost of the amount purchased. You will need the following variables: 
# ProductName 		PricePerPound 		Pounds 
# Total 		Ounces			UnitPrice

# You will need the following formulas: 

# UnitPrice = PricePerPound/16 
# Total = PricePerPound * (Pounds + Ounces/16)

# ----------------------------------------------------------------------------------------------------------------------------------------
def question2():

    print(color.lightCyan,"\n Question 2:".upper(),color.reset)
    print(color.cyan," \n The manager of the Super Supermarket would like to be able to compare the unit price for products sold there. To do this, the program should input the name and price of an item per pound and its weights in pounds and ounces. Then it should determine and display the unit price (the price per ounce) of that item and the total cost of the amount purchased.\n ", color.reset)

    ProductName = input("Type the item name: ")
    PricePerPound = float(input("Type the Pond price: "))
    Pounds = float(input("Type the Pounds: "))
    Ounces =float(input("Type the Ounce : " ))

    UnitPrice = PricePerPound/16
    Total = PricePerPound * (Pounds + Ounces/16)

    print (color.blue,f"\n The Unit price of the {ProductName} ${UnitPrice:.2f} Dollars", color.reset)
    print (color.blue,f"\n The Total is ${Total:.2f} Dollars\n ", color.reset)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Question 3:

# A physicist is willing to develop a code fragment to read a temperature from user in centigrade and print out the temperature in Fahrenheit. To do this, the program should input the temperature in centigrade outputs the output in Fahrenheit degrees. 
# To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.

# ----------------------------------------------------------------------------------------------------------------------------------------
def question3():

    print(color.lightCyan,"\n Question 3:".upper(),color.reset)
    print(color.cyan," \n A physicist is willing to develop a code fragment to read a temperature from user in centigrade and print out the temperature in Fahrenheit. To do this, the program should input the temperature in centigrade outputs the output in Fahrenheit degrees\n ", color.reset)

    CelsiusTemp = float(input("Type here the temperature in Cercus ºC : "))
    FahrenheitTemp = (CelsiusTemp * 9/5) + 32

    print(color.blue, f"The conversion from {CelsiusTemp}ºC to Fahrenheit is {FahrenheitTemp:.2f} ºF \n", color.reset)
# ----------------------------------------------------------------------------------------------------------------------------------------

question1()
question2()
question3()
