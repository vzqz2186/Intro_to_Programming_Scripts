------------------------------------------------------------------------------80
"""
     Program: CONTACT
      Author: Daniel Vazquez
        Date: 3/17/2017

   Objective: Create a text-based game. 

#Algorithm added 03/20/2017 (v1.06.03)
1) The player has to get the survivor from the initial room to the escape pods
   by telling him what to do.

    1.1) WASD will be used to to navigate through the game.
    1.2) Q quits the game.
    1.3) Enter advances the game.

3) The game uses riddles and problems as obstacles for the player to solve in
   order for the game to progress.

    2.1) Problems range from regular riddles, anagrams, basic decryption,
         finding a key in a room, etc.

4) Player names his/her character.

5) Survivor is only known as C since that is the only thing the player hears
   from his name.

"""
#acceptable_caracters list and all its alikes were idea of Dr. Nichols
acceptable_characters = ['w', 'a', 's', 'd', 'q', 'y', 'n', "", 'W', 'A', 'S',\
                         'D', 'Q', 'Y', 'N']

def advance():                              #Defines A to continue and an exit.
    print(end = '\n')
    advance = input("Press (Enter) to continue or (q) to Exit. ")
    if advance == "":
        print(end = '\n')
        pass
    if advance == "q":
        quit()

def bye():                                  #Terminate the program when the end
    print(end = '\n')                       #is reached
    while True:
        bye = input("Press (q) to Exit.")
        if bye == "q":
            exit()
        if bye != 'q':
            pass

#Added v2.10.05
def storyL():
    storyL = open("Story(Left).txt", 'r+')      #story time
    dialogueL = storyL.readlines()
    print(dialogueL[0][0:31], name, dialogueL[0][42:77])
    print(dialogueL[1])
    advance()
    print(dialogueL[3])
    advance()
    print(dialogueL[5])
    print(dialogueL[6])
    advance()
    print(dialogueL[8])
    advance()
    print(dialogueL[10])
    print(dialogueL[11])
    print(dialogueL[12])
    print(dialogueL[13])
    print(dialogueL[14])
    print(dialogueL[15])
    advance()
    print(dialogueL[17])
    print(dialogueL[18])
    advance()
    print(dialogueL[20])
    print(dialogueL[21])
    print(dialogueL[22])
    print(dialogueL[23])
    print(dialogueL[24])
    advance()
    print(dialogueL[26])
    advance()
    print(dialogueL[28])
    print(dialogueL[29][0:10], name, dialogueL[29][21:35])
    advance()
    print(dialogueL[31])
    print(dialogueL[32])
    advance()
    print(dialogueL[34])
    print(dialogueL[35])
    advance()
    storyL.close
    
print("CONTACT", '\n')
start = ['y', 'q']
while True:
    Start = input("Press (y) to start a New Game or (q) to quit. ")
    if Start == 'y':
        print(end = '\n')
        break                               #Start Titles
    elif Start == 'q':
        exit()
    elif Start not in start:
        print("The game said 'Press (ENTER) or (q)'. Try again.")

#short introduction to the game
#Added v2.08.04
backstory = ['y', 'n']
while True:
    synopsis = input("(y) to read the synonpis. (n) to jump straight into the game. ")
    if synopsis == 'y':
        quickie = open("Synopsis.txt", 'r')
        intro = quickie.readlines()
        print('\n')
        print(intro[0])
        print(intro[1])
        print(intro[2])
        print(intro[3])
        print(intro[4])
        print(intro[5])
        print(intro[6])
        print(intro[7])
        print(intro[8])
        print('\n')
        break
    if synopsis == 'n':
        break
    if synopsis not in backstory:
        print("(Y) or (N). Try again.")

#Names player's character.
while True:
    name = input(str("Choose a name no longer than 10 characters: "))
    Name = list(name)
    chr_count = sum(1 for i in Name)
    if chr_count > 10:
        print("Name too large.")
    if chr_count <= 10:
        print("Welcome, Officer", name + ".")
        break

advance()

#Story time
story = open("Story.txt", 'r+')
dialogue = story.readlines()
print(dialogue[0])
print(dialogue[1])
print(dialogue[2])
advance()
print(dialogue[4][0:18], name, dialogue[4][30:74])
print(dialogue[5])
advance()
print(dialogue[7])
print(dialogue[8])
print(dialogue[9])
advance()
print(dialogue[11])
print(dialogue[12])
advance()
print(dialogue[14])
print(dialogue[15])
print(dialogue[16])
print(dialogue[17])
advance()
print(dialogue[19])
advance()
print(dialogue[21])
print(dialogue[22])
advance()
print(dialogue[24])
advance()
print(dialogue[26])
print(dialogue[27])
print(dialogue[28])
advance()
print(dialogue[30])
print(dialogue[31])
story.close()
advance()

#Get "access" to map and cameras. Minigames 1 and 2.
A1Map = "diagram"
print("Solve the anagram to access the map: ragamid.")
while True:
    guess = input("- ")
    if guess == "diagram":
        print("Access granted.", "\n")
        break
    else:
        print("Access denied.")

A1Cameras = "security"
print("solve the anagram to access the cameras: icurtesy.") 
while True:
    guess = input("- ")
    if guess == A1Cameras:
        print("Access granted.")
        print("ERROR 208: NO SIGNAL")
        break
    else:
        print("Access denied.")

advance()

print(dialogue[35])
print(dialogue[36])
advance()
print(dialogue[38])
advance()
print(dialogue[40])
advance()

#Level 1
print("Help the sirvivor get out of the room.")
print("Use WASD to guide him where to look.")
while True:
    GO = 0
    direction = input("- ")
    if direction == "w":       #Look in front
        print("C: Here's the door. There's a note with the #4 taped next to the lock.")

        while True:            #Interact with the door
            try1 = input("(Y) to input password. (N) to return. ")
            if try1 == "n":
                break
            if try1 == "y":
                password_room = input("Type password: ")
                if password_room == "OpenSesame":
                    print("Password accepted.")
                    GO = 1
                    break
                else:
                    print("Incorrect password.")

    elif direction == "a":     #Look left
        print("C: The beds are right here. Besides blankets, there's nothing here.")
    elif direction == "s":     #Look back (during initial position)
        print("C: There's a locker here. Gun inside. No ammo though.")
    elif direction == "d":     #Look right
        print("C: A desk.")

        while True:            #Investigate the desk
            look = input("-- ")
            if look == "s":    #Go back to main position
                break
            if look == "w":
                print("C: The top drawer only has food wraps in it.")
            if look == "a":
                print("C: There's a paper with something written on it. StirWiweqi.")
            if look == "d":
                print("C: One man, one woman, three children... There used to be a family here.")
            if look == "q":
                quit()

    elif direction == "q":
        quit()
    if GO == 1:
        break
#End Level 1

advance()

#Desicion time
story = open("Story.txt", 'r')
dialogue = story.readlines()
print(dialogue[44])
story.close()

"""

"""

#story divides (v1.07.03)
while True:
    divide = input("Choose left (a) or right (d): ")
    print(end = '\n')
    choices = ['a', 'd']

    if divide not in choices:
        print("Officer ", name,", WHERE?!", '\n')

    if divide == 'd':                               #survivor goes right
        print("C: Going right.")
        #v2.12.05
        advance()
        print("C: I have encountered another locked door. ")
        advance()
        print("Use WASD to help him find a way to unlock the door.")
        key = 0

        #Level 2.1
        while True:
            direction = input("- ")
            if direction == "w":
                print("C: Door. It looks like it works with a seires of 3 numbers. Seems like the first")
                print("   is 4. We have to find the others.")
                guess = input ("(w) to fill in the combination. (s) to go back. ")
                if guess == 'w':                        #entering passcode
                    
                    while True:
                        Guess = input("Type passcode: ")
                        if Guess == "476":
                            print("Access granted.", '\n')    #right passcode
                            key = 1
                            break
                        if Guess!= "476":
                            print("Access denied.")     #wrong passcode
                            break
                if guess == 's':
                    pass
            if direction == "a":
                print("C: Another dorm.")

                while True:                             #room 1 in level 2.1
                    explore_room = input("-- ")
                    if explore_room == 'w':
                        print("C: Lucky bastard, this guy had a TV in his dorm.")
                    if explore_room == 'a':
                        print("C: There is a notepad here on the floor with a math problem on the screen.")
                        Try = input("(y) to solve the problem. (n) to go back. ")
                        if Try == 'n':
                            pass
                        if Try == 'y':
                            print("A bat and a ball cost 1.10 in total. How much did the ball cost? ")
                            priceAnswers = ['0.05', '.05']

                            while True:                 #unlocking notepad1
                                riddle = input("Type answer: ")
                                if riddle in priceAnswers:
                                    print("Passcode Pt.2: 7")   #achieved
                                    break
                                if riddle not in priceAnswers:  #failed
                                    print("WRONG")
                                
                    if explore_room == 's':             #going back to main place
                        print("C: Going back to the corridor.")
                        break

                    if explore_room == 'd':
                        print("C: There is a bed with a lamp here. It looks like power has already run")
                        print("   out here.")
            if direction == 's': 
                print("C: Sir, we can't go back. The power is running out.")
            if direction == 'd':                        #room 2 in level 2.1 
                print("C: Maintenance Room.")

                while True:
                    explore_room = input("-- ")
                    if explore_room == 'w':
                        print("C: The janitor didn't order all his mops and stuff. Makes my OCD go")
                        print("   crazy!")
                    if explore_room == 'a':
                        print("C: Oh man... here's... what's left of the janitor. He has his")
                        print("   notepad on his hand.")
                        Try = input("(y) to solve the problem. (n) to go back. ")
                        if Try == 'n':
                            pass
                        if Try == 'y':
                            print("Which word in the dictionary is spelled incorrectly.")

                            while True:                 #unlocking notepad2
                                riddle = input("Type Answer: ")
                                if riddle == "incorrectly": #bam
                                    print("Passcode Pt.3: 6")
                                    break
                                if riddle != "incorrectly": #damn
                                    print("WRONG")

                    if explore_room == 's':             #going back to main place
                        print("C: Going back to the corridor.")
                        break
                    if explore_room == 'd':
                        print("C: A picture of the janitor and his family... his name was Rick. Damn")
                        print("   these monsters...")

            if direction == "q":                        #quits program
                quit()
            if key == 1:                                #closes level 2.1
                break

        storyL()
        break

#Added v2.08.04
    if divide == 'a':                               #survivor goes left
        print("C: Going left.")
        advance()
        print("C: We have a problem. I've reached a door and it's locked.")
        advance()
        print("Use WASD to guide him where to look to find the key.")
        key = 0
        turnon = ['w', 's']
        #Level 2.2
        while True:
            direction = input("- ")
            if direction == 'w':                    #interact with door
                print("C: Here's the door.")
                key1 = input("Press (w) to enter key or (s) to go back and find it. ")
                if key1 == 's':
                    pass
                elif key1 == 'w':
                    if key == 0:
                        print("Access denied.")     #no key, no entrance     
                        print("C: Officer", name, ", without a key we cannot open the door.")
                        pass
                    elif key == 1:                  #yes key, yes entrance
                        print("Access granted.", '\n')
                        break
                elif key1 not in turnon:
                    print("C: Wah? You are goong to have to repeat that.")
            elif direction == 'd':
                print("C: I can see the pods from this window.")
            elif direction == 's':
                print("C: Lights are fading out. The ship's running out of power. We have to hurry.")
            elif direction == 'a':
                print("C: There's a screen turned off right here.")
                TurnOn = input("(w) to turn on the screen. (s) to return. ")
                if TurnOn == 'w':
                    print("C: There's a riddle on the screen.")
                    print("The more you take, the more you leave behind. What am I?")
                    while True:                     #solve the riddle
                        riddler = input("Type answer: (Hint: it's plural) ")
                        if riddler == "footsteps":      #succeeded at riddling
                            print("Access granted.")
                            print("C: the screen lifted up. There was a key inside. I'll take it.")
                            key = 1
                            break
                        else:                       #failed at riddling
                            print("Access denied.")
                            break
                if TurnOn == 's':
                    pass
                if TurnOn not in turnon:
                    pass
            elif direction == 'q':
                quit()
        #End of Level 2.2

        advance()
    
        storyL()
        storyL = open("Story(Left).txt", 'r')      #story time
        dialogueL = storyL.readlines()
        print(dialogueL[37])
        advance()
        print(dialogueL[39])
        advance()
        storyL.close
    
        #Level 3
        #v2.11.05
        print('\n')
        print("Look around for the button.")
        key = 0
        bHinge = 0
        bCup = 0
        bCover = 0
        stalls = [1,2,3,4,5,6,7]
        while True:
            direction = input("- ")
            if direction == 'w':
               print("C: The door is here.")
               while True:
                   button = input("(w) to insert the button. (s) to go back. ")
                   if button == 'w':
                       #All pssibilities for having certain pieces.
                       if bHinge == 0 and bCup == 0 and bCover == 0:
                           print("C: Officer", name, ", there is nothing to press...")
                           break
                       if bHinge == 0 and bCup == 0 and bCover == 1:
                           print("C: We just have the cover of the button. No mechanism.")
                           break
                       if bHinge == 1 and bCup == 0 and bCover == 0:
                           print("C: We only have the hinge. We need more parts.")
                           break
                       if bHinge == 0 and bCup == 1 and bCover == 0:
                           print("C: We just have the cup. No hinge or cover.")
                           break
                       if bHinge == 1 and bCup == 0 and bCover == 1:
                           print("C: We have the cover and the hinge. We are missing the cup.")
                           break
                       if bHinge == 1 and bCup == 1 and bCover == 0:
                           print("C: Hinge and cup but no cover.")
                           break
                       if bHinge == 0 and bCup == 1 and bCover == 1:
                           print("We have everything but the hinge.")
                           break
                       if bHinge == 1 and bCup == 1 and bCover == 1:
                           print("C: The button is assembled. I'm through.", '\n')
                           key = 1
                           break
                   if button == 's':
                       break
            elif direction == 'a':
                print("C: This is the bathroom. You're lucky you can't smell this.")
                while True:
                    search = input("(w) to search the stalls. (s) to go back. ")
                    if search == 'w':
                        print(stalls)
                        while True:             #search bathroom for parts
                            stall = input("Type the number of the stall to search it. (S) to go back. ")
                            if stall == '1':
                                print("C: This stall is empty.")
                            if stall == '2':
                                print("C: Somebody didn't flush this one...")
                            if stall == '3':
                                print("C: Oh... there's a dead man here... holding the cover of the button?")
                                print("Cover aqquired.")
                                bCover = 1
                                break
                            if stall == '4':
                                print("C: This toilet is destroyed... I guess somebody took a big one here.")
                            if stall == '5':
                                print("C: OH MY GOD! THIS ONE IS CLEAN. There's nothing here though.")
                            if stall == '6':
                                print("C: This toilet is a mess... nasty...")
                            if stall == '7':
                                print("Oh my God... there's a part INSIDE this toilet... Well, all for surviving.")
                                print("Cup aqquired.")
                                bCup = 1
                                break
                            if stall == 's':
                                break
                    if search == 's':
                        print("C: I'm back at the corridor.")
                        break
                    if search != 's' or 'w':
                        pass
            elif direction == 's':
                print("C: I have the feeling that I'm not the only one here...")
            elif direction == 'd':                  #locker riddle
                print("C: A locker. It seems that there is something inside but it's locked.")
                Try = input("(w) to solve the problem to open the locker. (s) to go back. ")
                if Try == 's':
                    print("C: I'm back at the corridor.")
                    pass
                if Try == 'w':
                    print("C: Riddle.")
                    print("It has fingers and a thumb, but are not living. What is it?")
                    print("All lowercase.")
                    while True:
                        guess = input("Type answer: A(n) ")
                        if guess == "glove":        #succeeded at riddling
                            print("Access granted.")
                            print("C: Here is the hinge. This comes with me.")
                            bHinge = 1
                            print("C: I'm back at the corridor.")
                            break
                        if guess != "glove":        #failed at riddling
                            print("Access denied.")       
            if direction == 'q':
                quit()
            if key == 1:
                break
        break
#End of Level 3

advance()

#both paths lead to the same room
#v2.13.05
storyR = open("the_room.txt", 'r+')             #story time
dialogueR = storyR.readlines()
print(dialogueR[0][0:11], name, dialogueR[0][21:77])
print(dialogueR[1])
advance()
print(dialogueR[3])
advance()
print(dialogueR[5])
print(dialogueR[6])
print(dialogueR[7])
advance()
print(dialogueR[9])
advance()
print(dialogueR[11])
advance()
print(dialogueR[13])
advance()
print(dialogueR[15])
advance()
print(dialogueR[17])
print(dialogueR[18])
advance()
print(dialogueR[20])
advance()
print(dialogueR[22])
print(dialogueR[23])
advance()
print(dialogueR[25])
storyR.close
advance()

#Level 4
print("C: Oh God... It went out of the room, I gotta get out of here quickly!")
advance()
print("Help the survivor get safely to the other side of the room. (q) to quit.")
Sec1 = 0
Sec2 = 0
GO1 = 0
GO2 = 0

while True:
    direction = input("- ")
    if direction == 'w':
        print("C: The door is right here. It needs two keys to open.")
        Open = input("(w) to disable security system. (s) to go back. ")
        if Open == 'w':
            if Sec1 == 0 and Sec2 == 0:
                print("C: Sir, we don't have any of the keys.")
            else:

                while True:                         #try to open door
                    pec1 = input("(y) to use Key 1. (n) to bo back. ")
                    if pec1 != 'y' or 'n':
                        pass
                    if pec1 == 'n':
                        break
                    if pec1 == 'y':
                        if Sec1 == 1:
                            print("Access granted.")
                            GO1 = 1
                            break
                        if Sec1 == 0:
                            print("Access denied.")
                            break

                while True:
                    pec2 = input("(y) to use key 2. (n) to go back. ")
                    if pec2 != 'y' or 'n':
                        pass
                    if pec2 == 'n':
                        break
                    if pec2 == 'y':
                        if Sec2 == 1:
                            print("Access granted.")
                            GO2 = 1
                            break
                        if Sec2 == 0:
                            print("Access denied.")
                            break
                #if you have both keys, u good. If not, ur not.
                        
        if Open == 's':
            pass
    if direction == 'a':
        print("C: Control room.")

        while True:
            search = input("-- ")
            if search == 's':
                print("C: Going back to the main room.")
                break
            if search == 'w':
                print("C: This is the machinery room.")

                while True:
                    look = input("--- ")
                    if look  == 'w':
                        print("C: They turned the engines off. They are figuring out how our technology works!")
                    if look == 's':
                        print("C: Going back to the control room.")
                        break
                    if look == 'a':
                        print("C: They destroyed the electric console. That's why the ship's running out of")
                        print("   power!")
                    if look == 'd':
                        print("C: why do these people had a locker room here...")

                        while True:
                            creep = input("(w) to check lockers. (s) to go back. ")
                            if creep != 'w' or 's':
                                pass
                            if creep == 'w':
                                lockers = ['1','2','3','4','5','s']

                                while True:
                                    locker = input("Type a number between 1 and 5 to search the lockers. (S) to go back. ")
                                    if locker not in lockers:
                                        print("C: That does not exist, Officer ", name,".")
                                    if locker == '1':
                                        print("C: Empty.")
                                    if locker == '2':
                                        print("C: There's a lab coat with stuff in it's pocket. One of the keys was in it.")
                                        print("Key 1 aquired.")
                                        Sec1 = 1
                                        break
                                    if locker == '3':
                                        print("C: Empty.")
                                    if locker == '4':
                                        print("C: Some tools and lab coats but nothing important here.")
                                    if locker == '5':
                                        print("C: Just a bunch of clothes here.")
                                    if locker == 's':
                                        print("C: Going back to the machinery room.")
                                        break

                            if creep == 's':
                                break

            if search == 'a':
                print("C: This is the console room.")

                while True:
                    look = input("--- ")
                    if look == 'w':
                        print("C: Here is the console from where the temperatures of the ship are monitored.")
                    if look == 'a':
                        print("C: A dead man... I used to know him. His name was Jeff...")
                        nasty = input("(w) to search Jeff. (s) to leave Jeff alone. ")
                        if nasty != 'w' or 's':
                            pass
                        if nasty == 'w':
                            print("C: Jeff might have saved my life. He had a key.")
                            print("Key 2 aquired.")
                            Sec2 = 1
                        if nasty == 's':
                            pass
                    if look == 's':
                        print("C: Going back to the control room.")
                        break
                    if look == 'd':
                        print("C: Some destroyed datapads on the floor. Nothing useful.")

            if search == 'd':
                print("C: The communications room is here.")

                while True:
                    look = input("--- ")
                    if look == 'w':
                        print("C: The FTL Vid Comm... completely wrecked...")
                    if look == 'a':
                        print("C: All the wires for the FTL Vid Comm are cut.")
                    if look == 's':
                        print("C: Going back to the control room.")
                        break
                    if look == 'd':
                        print("C: A soldier died here protecting this room. He will be remembered...")
                    
    if direction == 's':
        print("C: There is no turning back, Officer", name, ", it is now or never.")
    if direction == 'd':
        print("C: I don't think I want to go there, that's where the creature went.")
    if direction == 'q':
        quit()
    if GO1 == 1 and GO2 == 1:
        break
#End of Level 4

print('\n')
advance()
#2.14.05                                    #ending
storyE = open("Ending.txt", 'r+')
dialogueE = storyE.readlines()
print(dialogueE[0])
print(dialogueE[1])
advance()
print(dialogueE[3])
advance()
print(dialogueE[5])
print(dialogueE[6])
advance()
print(dialogueE[8])
advance()
print(dialogueE[10])
advance()
print(dialogueE[12])
print(dialogueE[13])
advance()
print(dialogueE[15])
print(dialogueE[16])
advance()
print("CONTACT")
storyE.close
bye()

"""
03/17/2017 (v1.06)
>>> First part of the story if finished.
>>> To do:
  >> Continue into the next decision on the story: which way to go.
    > Going right will have a different outcome than going left.
  >> Figure out a way to change the U that signals the player's dialogue to
     the first letter of the player's chosen name.

03/20/2017 (v1.06.03)
>>> Added algorithm to the file.
>>> Established rules and mechanics of the game.
>>> Added the "diary" to record the progress and changes done to the game.
>>> Changed 'r+' to just 'r' when opening story.txt to add the player's name
    when it is mentioned.

3/22/2017 (v1.07.03)
>>> Divided the story into two.

03/23/2017 (v2.08.04)
>>> Added another door to clear to the left.
>>> Did some changes to the format of the instructions.
>>> Added Synopsis.txt to the game.
>>> To do:
  >> Add an event that happens when you decide to go right
  >> Continue the story after clearing the door to the left.
  >> Organize the script into different .txt files depending on the situation
     chosen by the user.

03/27/2017 (v2.08.05)
>>> Checking for user input was improved.

04/16/2017 (v2.09.05)
>>> It turned out that user input check "improvement" actually messed up the
    code a bit, so it was restored to the previous version.

04/16/2017 (v2.10.05)
>>> Added more story and started to work in another level.

04/16/2017 (v2.11.05)
>>> Level 3 is finished.

04/17/2017 (v2.12.05)
>>> Added all the situation if the player goes left.
>>> Added user input check that actually works.

04/17/2017 (v2.13.05)
>>> Added the part of the story that connects both paths into the last level.
>>> Started working on the last level.

04/18/2017 (v2.14.05)
>>> Level 4 is finished.
>>> Last dialogue file is created and implemented.
>>> Both endings are added.
>>> Game is complete.
>>> Fixed the synopsis reading bug.
>>> Improved the bye() function.
"""
