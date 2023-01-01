import tkinter as tk                    
from functools import partial           
                                        


def avgCalc(l4, num1, num2, num3):      
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    n4 = float((n1 + n2 + n3)/3)
    l4.config(text="Average: %f" % float(n4))
    return


window = tk.Tk()
window.title("Student Average")
window.geometry("400x300")               

number1 = tk.StringVar()               
number2 = tk.StringVar()
number3 = tk.StringVar()

label1 = tk.Label(window, text="Enter the score for test 1: ").place(x=20, y=60)    
label2 = tk.Label(window, text="Enter the score for test 2: ").place(x=20, y=120)
label3 = tk.Label(window, text="Enter the score for test 3: ").place(x=20, y=180)
text1 = tk.Entry(window, textvariable=number1).place(x=180, y=60)                  
text2 = tk.Entry(window, textvariable=number2).place(x=180, y=120)
text3 = tk.Entry(window, textvariable=number3).place(x=180, y=180)

labelResult = tk.Label(window)                                                 
labelResult.place(x=50, y=210)

sumNumbers = partial(avgCalc, labelResult, number1, number2,number3)             
 
b1 = tk.Button(window, text="Average : ", command = sumNumbers, padx=10).place(x=200, y=230)  
b2 = tk.Button(window, text="Exit", command = window.destroy, padx=10).place(x=250, y=230)   

window.mainloop()