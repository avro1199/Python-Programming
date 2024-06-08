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
from random import choice, randint
from os.path import isfile

# Connect to the database
db_file = 'customers.db'
if isfile(db_file):
    db_connection = connect(database = db_file)
    db_cursor = db_connection.cursor()
else:
    raise Exception('Cannot find database file: ' + db_file)

# Select and print the question of interest
last_names = ['Almeida', 'Barnett', 'Bernard', 'Brooks', 'Brown',
              'Chase', 'Cunningham', 'Dubois', 'Fernandes', 'Francis',
              'Girard', 'Gonçalves', 'Gordon', 'Goyer', 'Gray',
              'Gruber', 'Gutiérrez', 'Hansen', 'Harris', 'Holý',
              'Hughes', 'Hämäläinen', 'Johansson', 'Jones', 'Kovács',
              'Köhler', 'Leacock', 'Lefebvre', 'Mancini', 'Martins',
              'Mercier', 'Miller', 'Mitchell', 'Murray', 'Muñoz',
              'Nielsen', "O'Reilly", 'Pareek', 'Peeters', 'Peterson',
              'Philips', 'Ralston', 'Ramos', 'Rocha', 'Rojas',
              'Sampaio', 'Schneider', 'Schröder', 'Silk', 'Smith',
              'Srivastava', 'Stevens', 'Sullivan', 'Taylor', 'Tremblay',
              'Van der Berg', 'Wichterlová', 'Wójcik', 'Zimmermann']
last_name = choice(last_names)
print(f"\nWhat is the email address for the customer with last name '{last_name}'?")

#--------------------------------------------------------------------#

# Put your code here
command = f"SELECT Email from customers WHERE LastName = '{last_name}'"
email = db_connection.execute(command).fetchone()[0]
print(f"Customer {last_name}'s email address is {email}")

#--------------------------------------------------------------------#

# Release the database
db_cursor.close()
db_connection.close()
