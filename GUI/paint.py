from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser

root = Tk()
root.title('Paint Program')
root.geometry('800x800')

def paint(e):
	# brush parameters
	brush_width = '%0.0f' % float(brush_slider.get())
	brush_color = 'green'
	
	brush_type2 = brush_type.get() # brush type: BUTT, ROUND, PROJECTING

	x1, y1 = e.x - 1, e.y - 1 # starting position
	x2, y2 = e.x - 1, e.y - 1 # ending position

	my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type.get(), smooth=True) # drawing on the canvas

# change the size of the brush
def change_brush_size(thing):
	slider_label.config(text='%0.0f' % float(brush_slider.get()))

# change brush colour
def change_brush_color():
	pass

# change brush colour
def change_canvas_color():
	pass

# creating the canvas
my_canvas = Canvas(root, width=600, height=400, bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>', paint)

# brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=30)

# brush size
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=50)

# brush slider
brush_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
brush_slider.pack(padx=10, pady=10)

# brush slider label
slider_label = Label(brush_size_frame, text=brush_slider.get())
slider_label.pack(pady=5)

# brush type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set('round') # round, butt, projecting

# create radio button for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text='Round', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, text='Slash', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text='Diamond', variable=brush_type, value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# change colours
change_colors_frame = LabelFrame(brush_options_frame, text='Change Colours')
change_colors_frame.grid(row=0, column=2)

# change brush colour button
brush_color_button = Button(change_colors_frame, text='Brush Colour', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# change canvas background colour
canvas_color_button = Button(change_colors_frame, text='Canvas Colour', command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

root.mainloop()
