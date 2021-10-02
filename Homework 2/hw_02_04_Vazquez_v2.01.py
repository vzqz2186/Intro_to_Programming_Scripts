------------------------------------------------------------------------------80
"""
    Program: Sum of inputs and averages
     Author: Daniel Vazquez
       Date: 1/23/2017

  Objective: Write a program that accepts user input of single integer,
             computing the sum and average after each step.
"""

"""
v1.00
#Y = str(input('Type a number: '))

while True:
    #X = amount of numbers that are going to be used.
    input('Type a number: ')
    #print('The sum is ' + sum + '.')
    #sum = 0.0
    #mean = (sum) / X
This got too convoluted and confusing. Decided to start again.
"""

#v2.00
#X = number to be used.
sum = 0
count = 1
while True:
    X = input('Enter a number or enter to quit: ')
    if X == "":
        break
    number = int(X)
    average = count + 1
    sum += number
    print('the sum is ', sum)
    print('the average is ', (sum / average))
