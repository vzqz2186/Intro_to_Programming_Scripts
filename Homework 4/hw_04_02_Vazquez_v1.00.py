------------------------------------------------------------------------------80
"""
    Program: Decrypt
     Author: Daniel Vazquez
       Date: 2/1/2017

  Objective: Decrypt->
                  aUxbt!csjmmjh-!boe!uif!tmjuiz!upwft
                  Eje!hzsf!boe!hjncmf!jo!uif!xbcf;
                  Bmm!njntz!xfsf!uif!cpsphpwft-
                  Boe!uif!npnf!sbuit!pvuhsbcf/
"""

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
        NewLetter = OldLetter - Distance
        if NewLetter < ord('a'):
            NewLetter = ord('z') - \
                          (Distance - (ord('a') - OldLetter + 1))
        Encryption += chr(NewLetter)
    print(Encryption)
    Continue = input("Type yes to encrypt another message or enter to quit. ")
    if Continue == "":
        quit()

"""
I based the last encryption homework and the example of the slides to confirm
the message. I figured it out by hand using the ASCII chart in the slides.The
key is literally 1. The reason I used the program is because I couldn't find
sense of the message when I got it by hand and wanted to make sure I wasn't
wrong. Not until I found out that it is a poem by Lewis Carrol that I
understood. The message is:

            'Twas brillig and the slithy toves
            Did gyre and gimble in the wabe:
            All mimsy were the borogoves,
            And the mome raths outgrabe.
"""
