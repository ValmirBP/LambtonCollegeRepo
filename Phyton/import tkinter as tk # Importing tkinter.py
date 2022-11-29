import tkinter as tk                    # Importing tkinter module as tk
# Partial functions allow us to fix a certain number of arguments
from functools import partial
# of a function and generate a new function.


# findavg function finds the sum displays the result.
def findavg(l4, num1, num2, num3):
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    n4 = float((n1 + n2 + n3)/3)
    l4.config(text="Average: %f" % float(n4))
    return


root = tk.Tk()
root.title("tk")                       # title name of the window
root.geometry("400x300")               # size of the window

# StringVar helps you manage the value of a widget such as a Label or Entry more effectively.
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()

# Creating the labels names.
l1 = tk.Label(root, text="Enter the score for test 1: ").place(x=20, y=60)
l2 = tk.Label(root, text="Enter the score for test 2: ").place(x=20, y=120)
l3 = tk.Label(root, text="Enter the score for test 3: ").place(x=20, y=180)
# Creating entry where you can enter numbers.
t1 = tk.Entry(root, textvariable=number1).place(x=180, y=60)
t2 = tk.Entry(root, textvariable=number2).place(x=180, y=120)
t3 = tk.Entry(root, textvariable=number3).place(x=180, y=180)

labelResult = tk.Label(root)
labelResult.place(x=50, y=210)

# Function calling of finavg() with four parameters.
findsum = partial(findavg, labelResult, number1, number2, number3)

# Button for Average when we click we will get the average.
b1 = tk.Button(root, text="Average : ", command=findsum).place(x=200, y=230)
# Button for Exiting the window.
b2 = tk.Button(root, text="Exit", command=root.destroy).place(x=250, y=230)

root.mainloop()
