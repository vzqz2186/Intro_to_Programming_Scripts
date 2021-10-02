------------------------------------------------------------------------------80
"""
    Program: 
     Author: Daniel Vazquez
       Date: 2/1/2017

  Objective: Write a generic user input function that takes the prompt as the
             argument and returns the user input as a string. Implement this
             function in the running average homework. Allow the user to input
             one or more characters to exit the program.
"""

#hw_04_01_Vazquez_v1.00.py

sum = 0
count = 1
while True:
    x = input('Type a number or type Q, E, or X to quit: ')
    if x == "q" or "Q" or "E" or "e" or "X" or "x":
        break
    number = int(x)
    average = count + 1
    sum += number
    print('the sum is ', sum)
    print('the average is ', (sum / average))
