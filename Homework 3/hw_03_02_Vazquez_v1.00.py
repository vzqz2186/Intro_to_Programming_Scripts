------------------------------------------------------------------------------80
"""
    Program:
     Author: Daniel Vazquez
       Date: 1/31/2017

  Objective: Write a program that displays the running average of N random
             numbers r such that 0 ≤ r ≤ 1 to 6 decimal places, where N is input
             by the user.
"""
"""
v1.00
from random import random

#RN = Random Number
#RN2 = Random Number 2
L = range(0,1000000)
count = 1
RN2 = 0
for i in L:
    number = float(input("please type a number: "))
    RN = (number) / 1000000
    count1 = count + 1
    RN2 += RN
    average = (RN2/count1)
    print("You typed", int(number))
    print("The average is", format(average, ".8g"))
"""

#v2.00
import random
print(format(random.random(), ".6g"))
"""
My logic to this problem is to ask the user for a number and then get that input
divided by a million, like discussed in class, and then divide that number by
the amount of times the user has input something. That way the program gets an
average to print to the user.
"""
