![pythonProject8 – simple_calculator py 4_23_2021 11_44_19 AM](https://user-images.githubusercontent.com/78782346/115825799-a98aea80-a429-11eb-9b0a-1f13803f045d.png)
![pythonProject8 – simple_calculator py 4_23_2021 11_44_33 AM](https://user-images.githubusercontent.com/78782346/115825810-ab54ae00-a429-11eb-8d70-acf7f43a2548.png)
![pythonProject8 – simple_calculator py 4_23_2021 11_44_50 AM](https://user-images.githubusercontent.com/78782346/115825820-ae4f9e80-a429-11eb-892e-209989125881.png)
![pythonProject8 – simple_calculator py 4_23_2021 11_44_58 AM](https://user-images.githubusercontent.com/78782346/115825826-b0196200-a429-11eb-8bd8-cbb7e4a7cd15.png)
![pythonProject8 – simple_calculator py 4_23_2021 11_45_02 AM](https://user-images.githubusercontent.com/78782346/115825838-b3145280-a429-11eb-87cd-b65fa9d71c53.png)
![Simple Calculator 4_23_2021 11_00_49 AM](https://user-images.githubusercontent.com/78782346/115825854-b7d90680-a429-11eb-90d2-719a7220217c.png)
![Simple Calculator 4_23_2021 11_01_10 AM](https://user-images.githubusercontent.com/78782346/115825859-bad3f700-a429-11eb-814a-ad0abc90bf1a.png)

    # Python program to create a simple GUI calculator using Tkinter 
   
    # import everything from tkinter module
from tkinter import *

expression = ""

 
    # Function to update expressiom
    # in the text entry box
    # Function to update expression in the text entry box

def press(num):
    # point out the global expression variable
    global expression
    
def press(num):


    # Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
def equal_press():
    # Try and except statement is used for handling the errors like zero division error etc.

    # Put that code inside the try block which may generate the error

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string

        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        # initialize the expression variable by empty string

        expression = ""

    # if error is generate then handle
    # by the except block

    except:

        equation.set(" error ")
        expression = ""


    # Function to clear the contents
    # of text entry box
    # declare Function to clear the contents of text entry box

def clear():
    global expression
    expression = ""
def clear():
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")
    gui.configure(background="light blue")

    # set the title of GUI window
    # title of the program
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    # create the text entry box for showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    # creating Buttons

    button1 = Button(gui, text=' 1 ', fg='black',  command=lambda: press(1), height=1, width=7)

    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2 = Button(gui, text=' 2 ', fg='black', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3 = Button(gui, text=' 3 ', fg='black', command=lambda: press(3), height=1, width=7)

    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4 = Button(gui, text=' 4 ', fg='black', command=lambda: press(4), height=1, width=7)

    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5 = Button(gui, text=' 5 ', fg='black', command=lambda: press(5), height=1, width=7)

    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6 = Button(gui, text=' 6 ', fg='black', command=lambda: press(6), height=1, width=7)

    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7 = Button(gui, text=' 7 ', fg='black', command=lambda: press(7), height=1, width=7)

    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8 = Button(gui, text=' 8 ', fg='black', command=lambda: press(8), height=1, width=7)

    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9 = Button(gui, text=' 9 ', fg='black', command=lambda: press(9), height=1, width=7)

    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0 = Button(gui, text=' 0 ', fg='black', command=lambda: press(0), height=1, width=7)

    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus = Button(gui, text=' + ', fg='black', bg='green', command=lambda: press("+"), height=1, width=7)

    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus = Button(gui, text=' - ', fg='black', bg='green', command=lambda: press("-"), height=1, width=7)

    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply = Button(gui, text=' * ', fg='black', bg='green', command=lambda: press("*"), height=1, width=7)

    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide = Button(gui, text=' / ', fg='black', bg='green',command=lambda: press("/"), height=1, width=7)

    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal = Button(gui, text=' = ', fg='yellow', bg='blue',command=equal_press, height=1, width=7)

    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear = Button(gui, text='Clear', fg='yellow', bg='blue',command=clear, height=1, width=7)

    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal = Button(gui, text='.', fg='yellow', bg='blue',command=lambda: press('.'), height=1, width=7)

    Decimal.grid(row=6, column=0)


    # start the GUI

gui.mainloop() 
