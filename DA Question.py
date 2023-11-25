#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 - PYTHON
The objective of the project is to calculate the duration of how long a person lived based on his Age. The duration should be calculated in different time units like Months, Weeks, Days, Hours, Minutes, Seconds
The input to the application is an Age of a person and the output is expected to calculate the duration of time he lived in different time units as selected by the user
# In[1]:


class AgeCalculator:
    def __init__(self, age):
        self.age = age

    def calculate_duration(self):
        # Constants for conversion
        days_in_year = 365.25
        hours_in_day = 24
        minutes_in_hour = 60
        seconds_in_minute = 60

        # Calculate durations
        years = self.age
        months = years * 12
        weeks = years * 52.1775  # Average number of weeks in a year
        days = years * days_in_year
        hours = days * hours_in_day
        minutes = hours * minutes_in_hour
        seconds = minutes * seconds_in_minute

        # Return the calculated durations
        return {
            'Years': years,
            'Months': months,
            'Weeks': weeks,
            'Days': days,
            'Hours': hours,
            'Minutes': minutes,
            'Seconds': seconds
        }

def main():
    # Get age from user input
    age = int(input("Enter the age of the person: "))

    # Create an instance of the AgeCalculator class
    age_calculator = AgeCalculator(age)

    # Calculate the duration
    duration = age_calculator.calculate_duration()

    # Display the results
    print(f"\nDuration of {age} years in different time units:")
    for unit, value in duration.items():
        print(f"{unit}: {value:.2f}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()


# # Assignment 3 - SQL Assignment - 2
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

The data file for this application is mbox.txt

# In[2]:


import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()


# In[ ]:




