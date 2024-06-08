
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
#
#--------------------------------------------------------------------#

# Import necessary functions
from tkinter import *

# Define some helpful constants
big_font = ('Verdana', 22)

# Create an interactive window
gui_window = Tk()

# Give the window a title and colour
gui_window.title('Light Switches')
gui_window['bg'] = 'light grey'

# callback functions
def fnc_left():
    val = left_checked.get()
    if(val == True):
        color = 'white'
    else:
        color = 'black'
    # print(color)
    left_light = Label(gui_window, font = big_font, height = 4,
                   width = 10, bg = color)
    left_light.grid(row = 0, column = 0, padx = 5, pady = 5)

def fnc_right():
    val = right_checked.get()
    if(val == True):
        color = 'white'
    else:
        color = 'black'
    # print(color)
    right_light = Label(gui_window, font = big_font, height = 4,
                    width = 10, bg = color)
    right_light.grid(row = 0, column = 1, padx = 5, pady = 5,
               columnspan = 2)

# Create two labels
left_light = Label(gui_window, font = big_font, height = 4,
                   width = 10, bg = 'black')
left_light.grid(row = 0, column = 0, padx = 5, pady = 5)

right_light = Label(gui_window, font = big_font, height = 4,
                    width = 10, bg = 'black')
right_light.grid(row = 0, column = 1, padx = 5, pady = 5,
               columnspan = 2)

# Create two Boolean Tk variables
left_checked = BooleanVar()
right_checked = BooleanVar()

# Create two check buttons
left_button = Checkbutton(gui_window, text = ' Left', command=fnc_left, variable=left_checked,
                          bg = 'light grey', font = big_font)
left_button.grid(row = 1, column = 0, padx = 5, pady = 5)

right_button = Checkbutton(gui_window, text = ' Right', command=fnc_right, variable=right_checked,
                           bg = 'light grey', font = big_font)
right_button.grid(row = 1, column = 1, padx = 5, pady = 5)

# Start the interactive event loop
gui_window.mainloop()
