from tkinter import *
import tkinter.messagebox

class calculator:
    def __init__(self, master):
        self.message = "0"
        self.adding = False
        self.dividing = False
        self.subtracting = False
        self.multiplying = False

        # whatever the message is, is displayed on the screen
        self.screen = Label(master,text=str(self.message), font=("times new roman", 40))
        self.screen.grid(columnspan=4, sticky=E)
        self.firstValDisplay = Label(master,text="", font=("times new roman", 20))
        self.firstValDisplay.grid(columnspan=4, row=0, sticky=W)

        self.separator= Frame(master, height=5,width=224, bg="black")
        self.separator.grid(columnspan=4, row=1)

        self.button7 = Button(master, text="7", padx=2, pady=2, command=self.seven, width=2)
        self.button7.config(font=('Times New Roman', 30))
        self.button7.grid(row=2, column=0)

        self.button8 = Button(master, text="8", padx=2, pady=2, command=self.eight, width=2)
        self.button8.config(font=('Times New Roman', 30))
        self.button8.grid(row=2, column=1)

        self.button9 = Button(master, text="9", padx=2, pady=2, command=self.nine, width=2)
        self.button9.config(font=('Times New Roman', 30))
        self.button9.grid(row=2, column=2)

        self.additionButton = Button(master, text="+", padx=2, pady=2, command=self.add, width=2)
        self.additionButton.config(font=('Times New Roman', 30))
        self.additionButton.grid(row=2, column=3)

        self.button4 = Button(master, text="4", padx=2, pady=2, command=self.four,width=2)
        self.button4.config(font=('Times New Roman', 30))
        self.button4.grid(row=3, column=0)

        self.button5 = Button(master, text="5", padx=2, pady=2, command=self.five,width=2)
        self.button5.config(font=('Times New Roman', 30))
        self.button5.grid(row=3, column=1)

        self.button6 = Button(master, text="6", padx=2, pady=2, command=self.six, width=2)
        self.button6.config(font=('Times New Roman', 30))
        self.button6.grid(row=3, column=2)

        self.subtractionButton = Button(master, text="-", width=2,padx=3,pady=2, command=self.subtract)
        self.subtractionButton.config(font=('Times New Roman', 30))
        self.subtractionButton.grid(row=3, column=3)

        self.button1 = Button(master, text="1", padx=2, pady=2, command=self.one, width=2)
        self.button1.config(font=('Times New Roman', 30))
        self.button1.grid(row=4, column=0)

        self.button2 = Button(master, text="2", padx=2, pady=2, command=self.two, width=2)
        self.button2.config(font=('Times New Roman', 30))
        self.button2.grid(row=4, column=1)

        self.button3 = Button(master, text="3", padx=2, pady=2, command=self.three, width=2)
        self.button3.config(font=('Times New Roman', 30))
        self.button3.grid(row=4, column=2)

        self.multiplicationButton = Button(master, text="x", width=2,padx=3,pady=2, command=self.multiply)
        self.multiplicationButton.config(font=('Times New Roman', 30))
        self.multiplicationButton.grid(row=4, column=3)

        self.clearButton = Button(master, text="c", padx=2, pady=2, width=2, command=self.clear)
        self.clearButton.config(font=('Times New Roman', 30))
        self.clearButton.grid(row=6, column=2)

        self.Button0 = Button(master, text="0", padx=2, pady=2, comman=self.zero, width=2)
        self.Button0.config(font=('Times New Roman', 30))
        self.Button0.grid(row=5, column=1)

        self.equalsButton = Button(master, text="=", padx=2, pady=2, command=self.equals, width=2)
        self.equalsButton.config(font=('Times New Roman', 30))
        self.equalsButton.grid(row=6, column=3)

        self.divisionButton = Button(master, text="/", padx=2, pady=2,width=2, command=self.divide)
        self.divisionButton.config(font=('Times New Roman', 30))
        self.divisionButton.grid(row=5, column=3)

        self.plusMinusButton = Button(master, text="±", padx=2, pady=2, command=self.plusMinus, width=2)
        self.plusMinusButton.config(font=('times new roman', 30))
        self.plusMinusButton.grid(row=5, column=0)

        self.decimalButton = Button(master, text=".", padx=2, pady=2, command=self.decimal, width=2)
        self.decimalButton.config(font=('times new roman', 30))
        self.decimalButton.grid(row=5, column=2)

        self.mainMenu = Menu()
        master.config(menu=self.mainMenu)
        self.fileMenu = Menu()
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="New Project...", command=self.clear)
        self.fileMenu.add_command(label="New...", command=self.clear)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=master.quit)

    def clear(self):
        self.message="0"
        self.firstVal=""
        self.screen.config(text=self.message)
        self.firstValDisplay.config(text="")

    def zero(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "0"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "0"
        self.screen.config(text=str(self.message))
    def one(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "1"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "1"
        self.screen.config(text=str(self.message))
    def two(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "2"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "2"
        self.screen.config(text=str(self.message))
    def three(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "3"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "3"
        self.screen.config(text=str(self.message))
    def four(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "4"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "4"
        self.screen.config(text=str(self.message))
    def five(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "5"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "5"
        self.screen.config(text=str(self.message))
    def six(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "6"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "6"
        self.screen.config(text=str(self.message))
    def seven(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "7"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "7"
        self.screen.config(text=str(self.message))
    def eight(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "8"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "8"
        self.screen.config(text=str(self.message))
    def nine(self):
        if self.message != "0" and len(str(self.message)) < 8:
            self.message = str(self.message) + "9"
        elif str(self.message) == "0" or str(self.message) == "0.0":
            self.message = "9"
        self.screen.config(text=str(self.message))

    def add(self):

        self.firstVal = self.message
        self.message = "0"
        self.adding = True
        self.dividing = False
        self.subtracting = False
        self.multiplying = False
        self.screen.config(text=self.message)
        self.firstValDisplay.config(text=str(self.firstVal))

    def multiply(self):

        self.firstVal = self.message
        self.message = "0"
        self.adding = False
        self.dividing = False
        self.subtracting = False
        self.multiplying = True
        self.screen.config(text=self.message)
        self.firstValDisplay.config(text=str(self.firstVal))

    def subtract(self):

        self.firstVal = self.message
        self.message = "0"
        self.adding = False
        self.dividing = False
        self.subtracting = True
        self.multiplying = False
        self.screen.config(text=self.message)
        self.firstValDisplay.config(text=str(self.firstVal))

    def divide(self):

        self.firstVal = self.message
        self.message = "0"
        self.adding = False
        self.dividing = True
        self.subtracting = False
        self.multiplying = False
        self.screen.config(text=self.message)
        self.firstValDisplay.config(text=str(self.firstVal))

    def equals(self):

        if self.adding:
            answer = float(self.firstVal) + float(self.message)
            answer = round(answer,2)
            if len(str(answer)) > 8:
                tkinter.messagebox.showinfo("Error", "answer is too large to handle : " + str(answer))
                self.clear()
            else:
                self.screen.config(text=str(answer))
                self.message = str(answer)
            self.adding = False

        elif self.subtracting:
            answer = float(self.firstVal) - float(self.message)
            answer = round(answer, 2)
            if len(str(answer)) > 8:
                tkinter.messagebox.showinfo("Error", "answer is too large to handle : " + str(answer))
                self.clear()
            else:
                self.screen.config(text=str(answer))
                self.message = str(answer)
            self.subtracting = False

        elif self.multiplying:
            answer = float(self.firstVal) * float(self.message)
            answer = round(answer, 2)
            if len(str(answer)) > 8:
                tkinter.messagebox.showinfo("Error", "answer is too large to handle : " + str(answer))
                self.clear()
            else:
                self.screen.config(text=str(answer))
                self.message = str(answer)
            self.multiplying = False

        elif self.dividing:
            if str(self.message) == "0":
                tkinter.messagebox.showinfo("Error", "Buddy, you know you're not supposed to divide by zero")
            else:
                answer = float(self.firstVal) / float(self.message)
                answer = round(answer, 2)
                if len(str(answer)) > 8:
                    tkinter.messagebox.showinfo("Error", "answer is too large to handle : " + str(answer))
                    self.clear()
                else:
                    self.screen.config(text=str(answer))
                    self.message = str(answer)
            self.dividing = False

        else:
            pass
        self.firstVal = 0
        self.firstValDisplay.config(text="")

    def plusMinus(self):
        if str(self.message) != "0" and str(self.message) != "0.0" and not(len(str(self.message)) >= 8 and float(self.message) > 0):
            self.message = float(self.message) * -1
            self.screen.config(text=str(self.message))


    def decimal(self):
        for i in str(self.message):
            if i == ".":
                self.priorDecimal = True
                break
            else:
                self.priorDecimal = False
        if not self.priorDecimal and len(str(self.message)) < 7:
            self.message = str(self.message) + "."
            self.screen.config(text=str(self.message))

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
# this keeps the window at a constant width and stuff, or tries to anyway

Calc = calculator(root)

root.mainloop()