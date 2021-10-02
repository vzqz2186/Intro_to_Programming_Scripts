------------------------------------------------------------------------------80
"""
    Program: Sum of inputs and averages
     Author: Daniel Vazquez
       Date: 1/23/2017

  Objective: Write a program that allows the user to specify the number of
             iterations used in 'this' approximation and that displays the
             resulting value.
"""
#approximation: PI/4 = 1 - 1/3 + 1/5 - 1/7 + ...
#The great Skylar Youngblood helped me and some other people with this program.

goal = (int(input("Enter the number to reach: ")))
def frange(start, stop, step):
    i = start
    while i < stop:
           yield i
           i += step

for i in frange(0, goal, 0.1):
#http://pythoncentral.io/pythons-range-function-explained/
#The website where the code comes from.
    print(i)
print(goal)
