------------------------------------------------------------------------------80
"""
    Program: Date and Time
    Aurthor: Daniel Vazquez
       Date: 1/30/2017

  Objective:Write a programthat prints date and time of program in three
            different formats.
"""

from time import strftime

print("This time will give you the time in three different formats.")
S1 = strftime("%A %B %d, %Y. %I:%M %p")
S2 = strftime("%a %m/%d/%y. %H:%M")
S3 = strftime("%d-%m-%y. %I:%M %p")
print(S1)
print(S2)
print(S3)
