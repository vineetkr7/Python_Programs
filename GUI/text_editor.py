# Simple text editor

from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title('Text Editor')
root.geometry('600x600')

# save file
def save_file():
    savefile = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetype=[('Text Files','*.txt'), ('All Files (*.*)','*.*')])
    if savefile:
        text = str(entry.get(1.0, END))
        savefile.write(text)
        savefile.close()
    else:
        pass

# clear
def clear():
    entry.delete(1.0, END)

# open file
def open_file():
    openfile = filedialog.askopenfile(mode='r', filetype=[('Text Files', '*.txt')])
    if openfile:
        content = openfile.read()
        entry.insert(INSERT, content)
    else:
        pass

# about
def about():
    messagebox.showinfo('About', 'Simple text editor like notepad, using Python')

# save button
save_button = Button(root, text='Save', command=save_file)
save_button.place(x=10, y=10)

# clear button
clear_button = Button(root, text='Clear', command=clear)
clear_button.place(x=48, y=10)

# open button
open_button = Button(root, text='Open', command=open_file)
open_button.place(x=88, y=10)

# quit button
quit_button = Button(root, text='Quit', command=root.destroy)
quit_button.place(x=130, y=10)

# about button
about_button = Button(root, text='About', command=about)
about_button.place(x=165, y=10)

# text area
entry = Text(root, height=33, width=72, wrap=WORD)
entry.place(x=10, y=50)

root.mainloop()
