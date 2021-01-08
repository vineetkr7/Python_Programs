# A simple paint application

# Credits to John Elder - Founder - CEO - Codemy.com, JohnElder.com

from tkinter import *
from tkinter import ttk, colorchooser, filedialog, messagebox
from PIL import ImageGrab

root = Tk()
root.title('Paint Program')
root.geometry('800x800')

def paint(e):
    # brush parameters
    brush_width = '%0.0f' % float(brush_slider.get())
    brush_type_val = brush_type.get()
    
    x1, y1 = e.x - 1, e.y - 1 # starting position
    x2, y2 = e.x + 1, e.y +	1 # ending position
    
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type_val, smooth=True) # drawing on the canvas

# change the size of the brush
def change_brush_size(thing):
    slider_label.config(text='%0.0f' % float(brush_slider.get()))

# change brush color
def change_brush_color():
    global brush_color
    brush_color = colorchooser.askcolor(color=brush_color)[1]

# change brush color
def change_canvas_color():
    global canvas_color
    canvas_color = 'white'
    canvas_color = colorchooser.askcolor(color=canvas_color)[1]
    my_canvas.config(bg=canvas_color)

# clear screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')

# save image
def save_image():
    result = filedialog.asksaveasfilename(title='Save As', filetypes = (("PNG Files","*.png"), ("JPEG Files","*.jpg"), ("All Files (*.*)","*.*")))
    
    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)
        
        # Pop up success message
        messagebox.showinfo("Image Saved", "Your image has been saved successfully!")
    
    else:
        pass

# creating the canvas
my_canvas = Canvas(root, width=600, height=400, bg='white')
my_canvas.pack(pady=10)

my_canvas.bind('<B1-Motion>', paint)

brush_color = 'black' # default brush color 

# brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=30)

# brush size frame
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=10)

# brush slider
brush_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
brush_slider.pack(pady=10)

# brush slider label
slider_label = Label(brush_size_frame, text=brush_slider.get())
slider_label.pack()

# brush type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type')
brush_type_frame.grid(row=0, column=1, padx=20)

brush_type = StringVar()
brush_type.set('round') # round, butt, projecting

# create radio buttons for brush types
brush_type_radio1 = Radiobutton(brush_type_frame, variable=brush_type, text='Round', value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, variable=brush_type, text='Slash', value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, variable=brush_type, text='Diamond', value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# change colors
change_colors_frame = LabelFrame(brush_options_frame, text='Change Colors')
change_colors_frame.grid(row=0, column=2, padx=10)

# change brush color button
brush_color_button = Button(change_colors_frame, text='Brush Color', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# change canvas background color
canvas_color_button = Button(change_colors_frame, text='Canvas Color', command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

# program options frame
options_frame = LabelFrame(brush_options_frame, text='Program Options')
options_frame.grid(row=0, column=3, padx=20)

# clear button
clear_button = Button(options_frame, text='Clear Screen', command=clear_screen)
clear_button.pack(padx=10, pady=10, anchor=W)

# save button
save_button = Button(options_frame, text='Save Image', command=save_image)
save_button.pack(padx=10, pady=10, anchor=W)

# exit button
exit_button = Button(options_frame, text='Exit', command=root.destroy)
exit_button.pack(padx=10, pady=10, anchor=W)

root.mainloop()

# pyinstaller.exe --onefile --windowed paint.py -> convert to .exe
