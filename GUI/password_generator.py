# Password Generator Application

from string import *
import random
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Password Generator')
root.geometry('250x175')
root['bg'] = '#ffff00'

# generate password
def generate_password():
    textbox.delete(1.0, END) # clearing the textbox for new entry
    pwd = ''.join(random.SystemRandom().choice(ascii_letters + digits + punctuation) for x in range(15))
    textbox.insert(1.0, pwd)

# clear textbox
def clear():
    textbox.delete(1.0, END)

# textbox
textbox = Text(root, height=1, width=20)
textbox.pack(padx=20, pady=20)

# button options frame
button_options_frame = LabelFrame(root, bg='#ff8980')
button_options_frame.pack(pady=10)

# generate button
generate_button = Button(button_options_frame, text='Generate', command=generate_password)
generate_button.grid(row=0, column=0, padx=10, pady=10)

# clear button
clear_button = Button(button_options_frame, text='Clear', command=clear)
clear_button.grid(row=0, column=1, padx=10, pady=10)

# exit button
exit_button = Button(button_options_frame, text='Exit', command=root.destroy)
exit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
