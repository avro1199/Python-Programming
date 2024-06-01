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
from sqlite3 import *
from random import randint
from os.path import isfile

# Open the database, if it exists
db_file = 'movie_actors.db'
if isfile(db_file):
    connection = connect(database = db_file)
    actors_db = connection.cursor()
else:
    raise Exception('Cannot find database file: ' + db_file)

# Select and print the question of interest
num_movies = randint(1, 62)
print('How many actors have starred in', num_movies,
      ('movies?' if num_movies != 1 else 'movie?'))

# Put your code here
# pass
command = f'SELECT * FROM actors WHERE "number_of_movies" = {num_movies}'
# command = 'SELECT * FROM actors WHERE "number_of_movies" = ' + str(num_movies)

message = connection.execute(command)

message_lst = list(message)

# print(message_lst)
for actor in message_lst:
    print(actor)
print(len(message_lst))

# Release the database
actors_db.close()
connection.close()
