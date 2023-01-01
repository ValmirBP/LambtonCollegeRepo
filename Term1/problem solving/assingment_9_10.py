'''
Student: Valmir de Barros Pedro
Student Number: C0868075
Assignment_9_10
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
The Department of Motor Vehicles in the state of Euphoria has finally decided to computerize its list of licensed drivers. Write a program that makes use of an existing file named "licenses" with records of the following form:

driver_name (String), license_number (String), number_of_tickets (Integer)

The program will prompt the user to enter the license number, then it displays the corresponding driver’s name and number of tickets.

Hint: load the "licenses" file into three parallel arrays and search one of these for the license number input.

'''
def question_01_ass0910():
    driverNames = []
    driverLicenseNumbers = []
    tickets = []

    print(color.green,"Enter license number to search: ", color.reset)
    licenseNumSearch = input()

    with open("licensesDBA.txt") as f:
        for record in f:
            [driverName, licenseNumber, ticket] = record.split(",")
            driverNames.append(driverName.strip())
            driverLicenseNumbers.append(licenseNumber.strip())
            tickets.append(ticket.strip())

    found = False
    for i in range(len(driverLicenseNumbers)):
        if driverLicenseNumbers[i] == licenseNumSearch:
            print(color.green,"Driver name:", driverNames[i],color.reset)
            print(color.red,"License number:", driverLicenseNumbers[i],color.reset)
            print(color.red,"Number of tickets:", tickets[i],color.reset)
            found = True

    if not found:
        print(color.red,"Nothing was found",color.reset)

question_01_ass0910()

# ---------------------------------------------------------------------------------------------------------------------------------------------------
'''
The information of credit card transactions are stored in file with the following format:
date, company,  amount

Example:
15/1/2021, Best Buy,  TV,  $1200.54
20/1/2021, Costco, Chair, $220.37

Develop a program that reads the information of transactions from a file and calculates the total amount of payments that are made.  Then, adds the following sentence to the end of that file:

Total amount spent: $total calculated amount. 

For example: 
“Total amount spent: $1420.91.
'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------
def question_02_ass0910():
    
    total=0
    try:
        file = open("receipt.txt", "r")
    except IOError:
        print(color.red,"Error no component found",color.reset)
    else:
        idxes=file.readlines()

        for line  in idxes:
            fmtLine=line.strip('\n').split(',')
            total+=float(fmtLine[3][2:])
        print(color.green,f"Total amount spent: ${total:.2f}",color.reset)
        file.close()

question_02_ass0910()