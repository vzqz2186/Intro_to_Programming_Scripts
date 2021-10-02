------------------------------------------------------------------------------80
"""
    Program: Quadratic Formula
     Author: Daniel Vazquez
       Date: 1/30/2017

  Objective: Given user input of real numbers a, b, and c, write a program that
             computes the two roots of a quadratic equation using the quadratic
             formula. Results may be complex.
"""

import math

print("This unit will compute the roots for a quadratic formula.")
A = float(input("a = "))
B = float(input("b = "))
C = float(input("c = "))
j = -1**0.5
Root1 = ((-B) + (((B*B) - (4*A*C)) ** 0.5)) / (2 * A)
Root2 = ((-B) - (((B*B) - (4*A*C)) ** 0.5)) / (2 * A)
print("The first root is", format(Root1, ".6g"))
print("the first root is", format(Root2, ".6g"))
