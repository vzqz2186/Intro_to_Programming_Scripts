------------------------------------------------------------------------------80
"""
    Program: ASCII Code No. 1
     Author: Daniel Vazquez
       Date: 1/23/2017

  Objective: Write a program that accepts single-character user input from the
             keyboard and prints that user input and the numeric ASCII code for
             that character.
"""

print('This unit will convert a letter to its correspondant ASCII Code.')
myChr = str(input('Pleasy type a letter: '))
print('You typed ' + myChr)
print('The ASCII Code is: ' , ord(myChr))
