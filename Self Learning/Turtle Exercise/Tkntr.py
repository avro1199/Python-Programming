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
main_window = Tk()

# Give the window a title
main_window.title('Text Duplicator')

def duplicate_text():
    s = data.get()
    if(len(s) == 0):
        s = 'EMPTY'
    data_copy = Label(main_window, font = big_font, width = 18, height = 1,
                  border = 3, relief = 'groove',
                  text = s)
    data_copy.grid(row = 1, column = 0, padx = 5, pady = 5)


# Create a push button
Button(main_window, font = big_font, command=duplicate_text, text = ' Duplicate ',
       activeforeground = 'red').\
grid(row = 2, column = 0, padx = 5, pady = 5)

# Create a text entry box
data = StringVar()
data_entry = Entry(main_window, textvariable=data, font = big_font, width = 18,
                   border = 3, relief = 'groove')
data_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
data_entry.insert(END, 'Enter text here')

# Create a label
data_copy = Label(main_window, font = big_font, width = 18, height = 1,
                  border = 3, relief = 'groove',
                  text = 'Copy appears here')
data_copy.grid(row = 1, column = 0, padx = 5, pady = 5)

# Start the interactive event loop
main_window.mainloop()
