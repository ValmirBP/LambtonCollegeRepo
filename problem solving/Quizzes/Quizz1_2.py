
from zoneinfo import available_timezones


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


def main(): # main module
    
    #  Local variables
    SIZE = 12
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rain = [0] * SIZE
    high = 0
    low = 0
    average = 0
    total = 0

    #  Get monthly rainfall
    for i in range(0,SIZE):
       print(color.orange," \n Enter rainfall for ", month[i], ": ")
       rain[i] = int(input())

    for i in range(0,SIZE):
        total += rain[i]
        if i == 0:
            high = rain[i]
            low = rain[i]
        elif high < rain[i]:
            high = rain[i]
        else:
            low = rain[i]

    average = total / SIZE
    print(color.red, f"\n The High rainfall is: {high}",color.reset)
    print( color.yellow, f"\n Low rainfall is: {low} ",color.reset)
    print(color.green, f"\n The Total of rainfall is: {total}", color.reset)
    print(color.cyan, f"\nThe Average of rainfall is: {average} \n ", color.reset)

main()
