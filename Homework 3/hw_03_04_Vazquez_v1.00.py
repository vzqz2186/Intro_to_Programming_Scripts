------------------------------------------------------------------------------80
"""
    Program: Encryption No. 2
     Author: Daniel Vazquez
       Date: 1/29/2017

  Objective: Given user input of a line of plaintext, e.g., "I see 
             leprechaunts!" write a programthat outputs the text using a Caesar
             cypher. The program should work with all printable characters.
"""

print("Encryption time!")
while True:
    SecretMessage = (input("Type the secret message or enter to quit: "))
    if SecretMessage == "":
        break
    Distance = int(input("Type the distance: "))
    if Distance == 0:
        print("There's no encryption, genius.")
        break
    Encryption = ""
    for ch in SecretMessage:
        OldLetter = ord(ch)
        NewLetter = OldLetter + Distance
        if NewLetter > ord('z'):
            NewLetter = ord('a') + Distance - \
                          (ord('z') - OldLetter + 1)
        Encryption += chr(NewLetter)
    print(Encryption)
    Continue = input("Type yes to encrypt another message or enter to quit. ")
    if Continue == "":
        break
