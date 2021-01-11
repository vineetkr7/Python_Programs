# Temperature Unit Converter Application

from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Temperature Conversion')
root.geometry('350x225')
root['bg'] = '#909090'

# convert temperature
def convert_temp():
    textbox2.delete(1.0, END)
    param1 = unit1.get()
    param2 = unit2.get()
    try:
        user_input = float(textbox1.get(1.0, END).strip())
        
        if param1 == param2:
            textbox2.insert(1.0, user_input)
            return
            
        if param1 == 'Celsius':
            if param2 == 'Fahrenheit':
                res = ((user_input * 9) / 5) + 32
            elif param2 == 'Kelvin':
                res = user_input + 273.15     
        elif param1 == 'Fahrenheit':
            if param2 == 'Celsius':
                res = (user_input - 32) * 5 / 9
            elif param2 == 'Kelvin':
                res = ((user_input - 32) * 5 / 9) + 273.15
        elif param1 == 'Kelvin':
            if param2 == 'Celsius':
                res = user_input - 273.15
            elif param2 == 'Fahrenheit':
                res = ((user_input - 273.15) * 9 / 5) + 32

        textbox2.insert(1.0, res)

    except:
        messagebox.showinfo('Invalid input', 'Enter a valid input')

# clear values
def clear_values():
    textbox1.delete(1.0, END)
    textbox2.delete(1.0, END)

# main frame
main_frame = Frame(root, bg='#696969')
main_frame.pack(pady=10)

# 1st value
unit1 = StringVar()
units_list = ['Celsius', 'Fahrenheit', 'Kelvin']
unit1.set(units_list[0])
opt_menu1 = OptionMenu(main_frame, unit1, *units_list)
opt_menu1.grid(row=0, column=0, padx=20, pady=10)

# 1st textbox
textbox1 = Text(main_frame, height=1, width=15)
textbox1.grid(row=0, column=1)

# 2nd value
unit2 = StringVar()
unit2.set(units_list[0])
opt_menu2 = OptionMenu(main_frame, unit2, *units_list)
opt_menu2.grid(row=1, column=0, padx=20, pady=10)

# 2nd textbox
textbox2 = Text(main_frame, height=1, width=15)
textbox2.grid(row=1, column=1)


# button options frame
button_options_frame = LabelFrame(root, text='Options', labelanchor='n', bg='#696969')
button_options_frame.pack(pady=10)

# convert button
convert_button = Button(button_options_frame, text='Convert', command=convert_temp)
convert_button.grid(row=0, column=0, padx=10, pady=10)

# clear button
clear_button = Button(button_options_frame, text='Clear', command=clear_values)
clear_button.grid(row=0, column=1, padx=10, pady=10)

# exit button
exit_button = Button(button_options_frame, text='Exit', command=root.destroy)
exit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
