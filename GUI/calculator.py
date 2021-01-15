# Calculator Application

from tkinter import *
from tkinter import ttk, messagebox
import math

root = Tk()
root.title('Calculator')
root.geometry('380x380')
root['bg'] = '#b0c4de'

input_list = []

# clear most recent entry
def clear_entry():
    textbox.delete(1.0, END)
    input_list.pop()

# clear all entries
def cancel():
    textbox.delete(1.0, END)
    input_list.clear()

# change the sign of the integer
def change_sign():
    user_input = textbox.get(1.0, END)
    if '-' not in user_input:
        number = '-' + user_input.strip()
    else:
        number = user_input.strip()[1:]
    textbox.delete(1.0, END)
    textbox.insert(1.0, number)

# check if the input number is int or float and then push it in the list
def input_check():
    user_input = textbox.get(1.0, END)
    if '.' not in user_input:
        input_list.append(int(user_input.strip()))
    else:
        input_list.append(float(user_input.strip()))

# digit click
def digit_click(digit):
    if textbox.get(1.0, END) == '0':
        textbox.delete(1.0, END)
    textbox.insert(END, digit)

# square root
def square_root():
    input_check()
    if '-' not in str(input_list[-1]):
        textbox.delete(1.0, END)
        res = math.sqrt(input_list[-1])
        if str(res)[-2:] == '.0':
            res = int(res)
        operation.config(text='√'+str(input_list[-1]))
        textbox.insert(1.0, res)
    else:
        pass

# dot operator
def dot():
    user_input = textbox.get(1.0, END)
    if '.' not in user_input:
        if user_input.strip() == '':
            res = '0.' # set result value as '0.' if the user input is empty
        else:
            res = user_input.strip() + '.'
        textbox.delete(1.0, END)
        textbox.insert(1.0, res)
    else:
        pass

# division
def division():
    input_check()
    input_list.append('/')
    textbox.delete(1.0, END)

# multiplication
def multiplication():
    input_check()
    input_list.append('*')
    textbox.delete(1.0, END)

# subtraction
def subtraction():
    input_check()
    input_list.append('-')
    textbox.delete(1.0, END)

# addition
def addition():
    input_check()
    input_list.append('+')
    textbox.delete(1.0, END)

# equals to
def equals():
    input_check()
    if input_list[-2] == '+':
        textbox.delete(1.0, END)
        res = input_list[-3] + input_list[-1]
    elif input_list[-2] == '-':
        textbox.delete(1.0, END)
        res = input_list[-3] - input_list[-1]
    elif input_list[-2] == '*':
        textbox.delete(1.0, END)
        res = input_list[-3] * input_list[-1]
    elif input_list[-2] == '/':
        textbox.delete(1.0, END)
        res = input_list[-3] / input_list[-1]
    if str(res)[-2:] == '.0':
        res = int(res)
    textbox.insert(1.0, res)
    
    if len(input_list) == 1:
        operation.config(text=input_list[-1])
	elif len(input_list) == 2:
        operation.config(text=''.join(str(s) for s in input_list))
	elif len(input_list) >= 3:
        operation.config(text=''.join(str(s) for s in input_list[-3:]))

# label for the recent operation
operation = Label(root, text='0')
operation.place(x=40, y=0)
    
# textbox for entering numbers
textbox = Text(root, height=1, width=25, font=('Calibri', 18), spacing1=5, spacing3=5, bg='#ffffe6')  # spacing1/spacing3 is for upper/lower spacing
textbox.pack(padx=20, pady=20)

# buttons frame
buttons_frame = Frame(root, bg='#ff8980')
buttons_frame.pack(padx=10, pady=10)

# buttons for digits
nine_button = Button(buttons_frame, text='9', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(9))
nine_button.grid(row=1, column=0)
eight_button = Button(buttons_frame, text='8', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(8))
eight_button.grid(row=1, column=1)
seven_button = Button(buttons_frame, text='7', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(7))
seven_button.grid(row=1, column=2)
six_button = Button(buttons_frame, text='6', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(6))
six_button.grid(row=2, column=0)
five_button = Button(buttons_frame, text='5', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(5))
five_button.grid(row=2, column=1)
four_button = Button(buttons_frame, text='4', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(4))
four_button.grid(row=2, column=2)
three_button = Button(buttons_frame, text='3', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(3))
three_button.grid(row=3, column=0)
two_button = Button(buttons_frame, text='2', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(2))
two_button.grid(row=3, column=1)
one_button = Button(buttons_frame, text='1', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(1))
one_button.grid(row=3, column=2)
zero_button = Button(buttons_frame, text='0', font=('Calibri', 12), height=2, width=8, command=lambda: digit_click(0))
zero_button.grid(row=4, column=1)

# clear entry
clear_entry_button = Button(buttons_frame, text='CE', font=('Calibri', 12), height=2, width=8, bg='#696969', command=clear_entry)
clear_entry_button.grid(row=0, column=0)

# cancel
cancel_button = Button(buttons_frame, text='C', font=('Calibri', 12), height=2, width=8, bg='#696969', command=cancel)
cancel_button.grid(row=0, column=1)

# change sign
sign_button = Button(buttons_frame, text='+/-', font=('Calibri', 12), height=2, width=8, command=change_sign)
sign_button.grid(row=4, column=0)

# square root
sqrt_button = Button(buttons_frame, text='√', font=('Calibri', 12), height=2, width=8, command=square_root)
sqrt_button.grid(row=0, column=2)

# division
divide_button = Button(buttons_frame, text='/', font=('Calibri', 12), height=2, width=8, command=division)
divide_button.grid(row=0, column=3)

# multiplication
prod_button = Button(buttons_frame, text='*', font=('Calibri', 12), height=2, width=8, command=multiplication)
prod_button.grid(row=1, column=3)

# subtraction
subtract_button = Button(buttons_frame, text='-', font=('Calibri', 12), height=2, width=8, command=subtraction)
subtract_button.grid(row=2, column=3)

# addition
add_button = Button(buttons_frame, text='+', font=('Calibri', 12), height=2, width=8, command=addition)
add_button.grid(row=3, column=3)

# equals
equal_button = Button(buttons_frame, text='=', font=('Calibri', 12), height=2, width=8, bg='#696969', command=equals)
equal_button.grid(row=4, column=3)

# decimal
decimal_button = Button(buttons_frame, text='.', font=('Calibri', 12), height=2, width=8, command=dot)
decimal_button.grid(row=4, column=2)

root.mainloop()
