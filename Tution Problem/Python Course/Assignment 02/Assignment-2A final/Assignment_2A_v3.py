
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
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
student_number = 1234567
student_name   = 'x y'
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#



#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message: # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution below.
#

# Create the main window
main_window = Tk()

# Your code goes here
bg_color = 'gray90'
font_face = 'cascadia'
box_heading =('cascadia',16)

main_window.geometry('740x500')
main_window.title("Poly Debnath's Fact Checking") #put a title here
main_window.config(background=bg_color)

# all callback function
def fnc_show_source():
    global msg
    msg.grid_forget() #remove all past texts
    selection = source.get()
    # print('The message is \"', m, '\"')
    msg = Message(status_frame, width=360, text= selection,
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

def fnc_show_latest():
    global msg
    msg.grid_forget()
    # print('Show Latest Button Pressed !')
    msg = Message(status_frame, width=360, text='Show Latest Button Pressed !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

def fnc_show_details():
    global msg
    msg.grid_forget()
    # print('Show Details Button Pressed !')
    msg = Message(status_frame, width=360, text='Show Details Button Pressed !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

def fnc_show_rating(r):
    global msg
    msg.grid_forget()
    msg = Message(status_frame, width=360, text='Rating '+str(r)+' selected !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

def fnc_save_rating():
    global msg
    msg.grid_forget()
    # print('Save Rating Button Pressed !')
    msg = Message(status_frame, width=360, text='Save Rating Button Pressed !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

# Creating frames
text_frame = Frame(master=main_window, width=400, height=500, padx=10, background=bg_color)
text_frame.grid_propagate(0)
img_frame = Frame(master=main_window, borderwidth=4, border=0, background='red2')

status_frame = LabelFrame(master=text_frame, text='System Status', background=bg_color,
                          font=box_heading,fg='gray',labelanchor='nw', padx=5, pady=5,
                          borderwidth=3, border=4, width=380, height=150)
status_frame.grid_propagate(0)

data_frame = LabelFrame(master=text_frame, text='Data Source', background=bg_color,
                        font=box_heading,fg='gray', labelanchor='nw', padx=5, pady=5,
                        borderwidth=3, border=4, width=250, height=170)
data_frame.grid_propagate(0)

rating_frame = LabelFrame(master=text_frame, text='Data Reliability', background=bg_color,
                          font=box_heading,fg='gray', labelanchor='nw', padx=5, pady=5,
                          borderwidth=3, border=4, width=200, height=150)
rating_frame.grid_propagate(0)

#position of two main frame
text_frame.grid(row=0, column=1)
img_frame.grid(row=0, column=0, padx=5)

#position of subframes
status_frame.grid(row=0, column=0, sticky='w', pady=3)
data_frame.grid(row=1, column=0, sticky='w', pady=3)
rating_frame.grid(row=2, column=0, sticky='w', pady=3)

#initial message
msg = Message(status_frame, width=360, text='Waiting for User Input . . .',
              background=bg_color, font=(font_face, 13),fg='gray')
msg.grid(row=0, column=0)

#options for selecting the source
source = StringVar(value='No Option Selected')
Radiobutton(data_frame, background=bg_color, text=' Source - A', font=(font_face, 13),
            variable=source, value='Source A selected !', command=fnc_show_source).grid(row=0, column=0)

Radiobutton(data_frame, background=bg_color, text=' Source - B', font=(font_face, 13),
            variable=source, value='Source B selected !', command=fnc_show_source).grid(row=1, column=0)

Radiobutton(data_frame, background=bg_color, text=' Source - C', font=(font_face, 13),
            variable=source, value='Source C selected !', command=fnc_show_source).grid(row=2, column=0)

Button(master=data_frame, text='Show Latest', font=(font_face, 11),
       command=fnc_show_latest).grid(row=3, column=0, padx=5)

Button(master=data_frame, text='Show Details', font=(font_face, 11),
       command=fnc_show_details).grid(row=3, column=1, padx=5)

#rating input
rate = IntVar()
rating = Scale(master=rating_frame, background=bg_color, from_=1, to=5,variable=rate,
               label='Rating', font=(font_face, 12), orient='horizontal', command=fnc_show_rating)

btn = Button(master=rating_frame, text='Save Rating', font=(font_face, 11), command=fnc_save_rating)
rating.pack()
btn.pack(padx=5, pady=10)

image = PhotoImage(file='./AIRobot.png') #image location here

img_lbl = Label(master=img_frame, image=image, bg='#bbeeff')
img_lbl.grid(row=0, column=0)


menubar = Menu()
main_window.config(menu=menubar)

mymenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Menu', menu=mymenu)
mymenu.add_command(label='Option 1')
mymenu.add_separator()
mymenu.add_command(label='Option 2')

# Start the event loop to detect user inputs
main_window.mainloop()
