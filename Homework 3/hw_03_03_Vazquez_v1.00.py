------------------------------------------------------------------------------80
"""
    Program: Encryption No. 1
     Author: Daniel Vazquez
       Date: 1/29/2017

  Objective: Given user input of a line of plaintext, e.g., "I see imaginary
             numbers!" write a programthat outputs the text reversed. The
             program should work with all printable characters.
"""
print("Let's reverse whatever you want to reverse.")
while True:
    message = str(input("Type the message or enter to quit: "))
    if message == "":
        break
    print("You typed:", message)
    print("The new message is: ", message [::-1])

    
