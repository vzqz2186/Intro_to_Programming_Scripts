------------------------------------------------------------------------------80
"""
    Program: Prime or Not Prime
     Author: Daniel Vazquez
       Date: 2/1/2017

  Objective: Write a program to check wether an integer input by user is prime.
             No internet is allowed in this one.
"""

#v3.00
import math
print("~This unit will know if an input number is a prime.")
while True:
    x = input("Type an integer or type Q to quit: ")
    if x == "q" or "Q":
        break
    else:
        a = int(x)
        if a == 2:
            print(x, "is prime.")
        if a == 9:
            print(x, "is not prime.")
        if a > 2:
            if a % 2 == 0:
                print(x, "is not prime.")
            if a % 2 != 0:
                prime = True
                for i in range(3, a, 2):
                    if a % i == 0:
                        prime = False
                if (prime):
                        print(x, "is prime.")

"""
Dr. Nichols email's algorithm:

enter n
if n==2 then prime
if n is even then not prime
isPrime = true
for i in range(3,n/2,2):
    if N%i==0:
        isPrime=false

if(isPrime) then print("prime")
"""

"""
classroom algorithm:
for i in range(3,n,2):
    if i is prime(i):
        if D/i ==integer:
            print("not prime")
        else:
            print("prime")
"""
