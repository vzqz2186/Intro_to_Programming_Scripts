------------------------------------------------------------------------------80
"""
    Program: The Triangle
     Author: Daniel Vazquez
       Date: 1/22/2017

  Objective: Write a program that accepts the three sides of a triangle as
             inputs so it can tell if it is an equilateral triangle.
"""
#The program will tell the type of triangle depending on the user's input.

print('This unit will tell you which type of triangle are you talking about.')
A = float(input('Lenght of the A side of the triangle: '))
B = float(input('Lenght of the B side of the triangle: '))      
C = float(input('Lenght of the C side of the trinagle: '))
    

if A == B == C:
    print('This is an equilateral triangle.')
elif A != B == C:
    print('This is an isosceles triangle.')
elif A == B != C:
    print('This is an isosceles triangle.')
elif B != A == C:
    print('This is an isosceles triangle.')
elif A != B != C:
    print('This is a scalene triangle.')
