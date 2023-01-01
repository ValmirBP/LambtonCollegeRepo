'''
Student Name: Valmir de Barros Pedro
Student Number: C0868075
Course: CSD 1233 Python Programming
Professor: Hesam Akbari
'''
# ------------------------------------------------------------------

'''
using the Tkinter library in python creates a window that collects 
three numbers and displays the sumCalc and average of the numbers.
your windows should be similar to the following picture. 
Throw your py file into the provided area:
'''
# ------------------------------------------------------------------
# SOLUTION

from tkinter import *

window = Tk()
window.title("Student Average")
window.geometry('350x200')

label1 = Label(window, text = "Type here the marks for test 1:")
label1.grid()
text1 = Entry(window, width=10)
text1.grid(column =1, row =0)


label2 = Label(window, text = "Type here the marks for test 2:")
label2.grid()
text2 = Entry(window, width=10)
text2.grid(column =1, row =1)


label3 = Label(window, text = "Type here the marks for test 3:")
label3.grid()
text3 = Entry(window, width=10)
text3.grid(column =1, row =2)

label4 = Label(window, text = "Average:")
label4.grid()
label5 = Label(window, text = "sumCalc:")
label5.grid()


def averageCalc():
        result = label4.cget('text')
        sumMarks = int(text1.get()) + int(text2.get()) + int(text3.get())
        result = result + str(sumMarks/3)
        label4.configure(text = result)

def sumCalc():
        result = label5.cget('text')
        sumMarks = int(text1.get()) + int(text2.get()) + int(text3.get())
        result = result + str(sumMarks)
        label5.configure(text = result)


button1 = Button(window, text = "Average" ,command=averageCalc)
button1.grid(column=0, row=5)

button2 = Button(window, text = "Sum" ,command=sumCalc)
button2.grid(column=1, row=5)

button3 = Button(window, text = "Exit" ,command=window.destroy, padx = 10)
button3.grid(column=3, row=5)

window.mainloop()
