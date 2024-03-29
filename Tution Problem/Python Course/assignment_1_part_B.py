
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 9108319
student_name   = 'Poly Debnath'
#
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data
    def data_set(new_seed = randint(0, 99999)):
        return raw_data(new_seed) # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.

def visualise_data(rename_me_in_task_1b):
    # pass # <--- Replace this statement with your solution
    speed(0)
    draw_plane2(-560,200,'up')
    goto(-560,130)
    color('slate gray')
    write('UP',align='center', font=['Arial',12,'bold'])
    # goto(-560,110)
    # write('this is up',align='center', font=['Arial',12,'bold'])
    draw_plane2(-560,0,'right')
    goto(-560,-70)
    color('slate gray')
    write('This is RIGHT',align='center', font=['Arial',12,'bold'])
    draw_plane2(-560,-200,'down')
    goto(-560,-270)
    color('slate gray')
    write('This is DOWN',align='center', font=['Arial',12,'bold'])

    draw_plane2(-40,0)  #####This line for checking the grid size and image background
    draw_plane2(-120,0,'down')
    draw_plane2(40,-80)

def draw_plane2(x=0, y=0, dir='up'):
    def draw_rect(x=0, y=0, length=20, width=10, clr='blue'):
        nonlocal dir
        penup()
        if(dir=='up'):
            goto(x-width/2, y-length/2)
        elif(dir=='down'):
            goto(x+width/2, y+length/2)
            setheading(180)
        elif(dir=='right'):
            goto(x-length/2,y+width/2)
            setheading(270)
        fillcolor(clr)
        begin_fill()
        pendown()
        for i in range(2):
            forward(width)
            left(90)
            forward(length)
            left(90)
        end_fill()
        penup()

    def draw_wing(x=0, y=0, length=30, width=10, clr='light gray'):
        nonlocal dir

        penup()
        goto(x,y)
        if(dir=='up'):
            setheading(0)
        elif(dir=='down'):
            setheading(180)
        elif(dir=='right'):
            setheading(270)
        right(135)
        fillcolor(clr)
        begin_fill()
        pendown()
        forward(length)
        left(45)
        forward(width)
        left(120)
        forward(length)
        end_fill()
        penup()
        goto(x,y)
        if(dir=='up'):
            setheading(0)
        elif(dir=='down'):
            setheading(180)
        elif(dir=='right'):
            setheading(270)
        right(45)
        begin_fill()
        pendown()
        forward(length)
        right(45)
        forward(width)
        right(120)
        forward(length)
        end_fill()
        setheading(0)

    # pensize(2)
    # speed(0)

    #drawing the frame
    hideturtle()
    penup()
    goto(x-40, y-39)
    setheading(0)
    pendown()
    # fillcolor(bg_color)
    color('slate gray')
    if(dir=='up'):
        fillcolor('steelblue1')
    elif(dir=='right'):
        fillcolor('slategray4')
    elif(dir=='down'):
        fillcolor('sienna2')
    begin_fill()
    for i in range(4):
        forward(79)
        left(90)
    end_fill()
    penup()
    if(dir=='right'):
        goto(x-36,y+33)
        setheading(0)
        pensize(3)
        color('white')
        for i in range(3):
            pendown()
            forward(20)
            penup()
            forward(6)
        penup()
        goto(x-36,y-33)
        setheading(0)
        for i in range(3):
            pendown()
            forward(20)
            penup()
            forward(6)
    penup()
    pensize(1)
    color('black')
    home()

    #drawing the plane
    if(dir=='up'):
        draw_rect(x+15, y+7, 10, 7, 'white')
        draw_rect(x-15, y+7,10,7, 'white')
        draw_wing(x,y+22,36)
        draw_rect(x,y+10, 40,10, 'white')
        draw_wing(x,y-14, 21, 5)
        draw_rect(x,y-18,16,10,'red')
        penup()
    elif(dir=='down'):
        draw_rect(x-15, y-7, 10, 7, 'white')
        draw_rect(x+15, y-7,10,7, 'white')
        draw_wing(x,y-22,36)
        draw_rect(x,y-10, 40,10, 'white')
        draw_wing(x,y+10, 20, 5)
        draw_rect(x,y+18,16,10,'red')
        penup()
    elif(dir=='right'):
        draw_rect(x+7, y+15, 10, 7, 'white')
        draw_rect(x+7, y-15,10,7, 'white')
        draw_wing(x+22,y,36)
        draw_rect(x+10,y, 40,10, 'white')
        draw_wing(x-10,y, 20, 5)
        draw_rect(x-18,y,16,10,'red')
        penup()

    if(dir=='up'):
        goto(x+5,y+30)
        setheading(0)
    elif(dir=='down'):
        goto(x-5,y-30)
        setheading(180)
    elif(dir=='right'):
        goto(x+30,y-5)
        setheading(270)
    fillcolor('white')
    left(90)
    pendown()
    begin_fill()
    circle(5,180)
    end_fill()

    penup()
    if(dir=='up'):
        goto(x+5,y-26)
    elif(dir=='down'):
        goto(x-5,y+26)
        setheading(90)
    elif(dir=='right'):
        goto(x-26,y-5)
        setheading(-180)
    fillcolor('red')
    pendown()
    begin_fill()
    circle(-5,180)
    end_fill()
    # color('gray')

    #drawing the tail
    if(dir=='up'):
        setheading(0)
        draw_rect(x,y-24, 20,4,'red')
    elif(dir=='down'):
        setheading(180)
        draw_rect(x,y+24, 20,4,'red')
    elif(dir=='right'):
        setheading(270)
        draw_rect(x-24,y, 20,4,'red')
#
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
#
# ***** You can add arguments to this function call to modify
# ***** features of the drawing canvas such as the background
# ***** and line colours, etc
create_drawing_canvas('This is Title', write_instructions=False)

# Create the data set and pass it to the student's function
#
# ***** While developing your Task 1B code you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
#
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
