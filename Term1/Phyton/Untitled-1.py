
from tkinter import *
from tkinter import messagebox  # this is for message boxes (Alert)

# its common with GUI to use class to organize the window.


class StudantAverage:
    def __init__(self):
        # -----------------------------Window----------------------------
        self.window = Tk()  # it creates the window
        self.window.title('Student Average')
        self.window.geometry("350x200")  # width and length

        # --------------------------layout (Frame)------------------------
        self.top_frame = Frame(self.window)
        self.bottom_frame = Frame(self.window)
        self.result_frame = Frame(self.window)

        # ---------------------------widgets------------------------------
        self.prompt_label = Label(
            self.top_frame, text="Enter a weight in kilogram", padx=10, fg="blue", font=("arial", 12))
        self.kilo_entry = Entry(self.top_frame, bg="lightcyan")
        self.result_btn = Button(
            self.bottom_frame, text="Convert", padx=20, bg="yellow", command=self.calculate)
        self.exit_btn = Button(self.bottom_frame, text="exit", padx=10,
                               bg="orange", command=self.exit)  # inside the btn
        # its an object capable of changing throughout the window
        self.result = StringVar(value="Result : N/A")
        self.result_label = Label(
            self.result_frame, textvariable=self.result, fg="brown", font=('arial', 10))
        # --------------------------pack-----------------------------------
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack()
        self.result_btn.pack(side='left', padx=10)
        self.exit_btn.pack()
        self.result_label.pack()

        self.top_frame.pack(pady=10, padx=10)
        self.bottom_frame.pack(side="right", padx=10)
        self.result_frame.pack(pady=20)
        mainloop()

    def calculate(self):
        try:
            kilo = float(self.kilo_entry.get())
            pound = kilo * 2.2046
            print(pound)
            #messagebox.showinfo("Result", f"{kilo} kg is {pound} lb")
            self.result.set(f"{kilo:.2f} kg is {pound:.2f} lb")

        except Exception:
            messagebox.showerror(
                'bad input', 'Input has to be a digit\n EX : 1,2,3.4, etc')

    def exit(self):
        if (messagebox.askyesno('Are you sure?', 'Are you sure?')):
            self.window.destroy()


w1 = KiloConvertor()
