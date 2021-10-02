------------------------------------------------------------------------------80
"""
       Name: Program - Read and Write
     Author: Daniel Vazquez
       Date: 2/20/2017

  Objective: Write a program that prompts the user for the names of two text
             files. Read the contents of the first file and WRITE that to the
             second file.

             - Use "first_file.txt" with at least 10 lines of something.
             - Use "second-file_###.txt" where '###' goes from 000 to 999 and
               back to 000 depending on the times the program is run.

             Send the program and the first_file.txt
"""

#program creates second file
#hardcode the first and second file name

import os
count = 0
print("This one will read a file and then rewrite its content in another file.")
while True:
    file1 = input("Name of the first file or X to quit: ")   #names 1st file
    if file1 == "x":
        break
    file2 = "second_file.txt"
    f1 = open(file1, 'r')                          #pulls up the first file
    if os.path.isfile(file2):                      #if 2nd file exists...
        count += 1
        FILE2 = file2[:11] + "(" + str(count) + ")" + file2[-4:]
                                                   #creates 2nd file and
                                                   #adds number version
        F2 = open(str(FILE2), 'w')
        for line in f1:                            #copies the content of file1
            F2.write(line)                         #to file2
        F2.close()
    if os.path.isfile(file2) is False:             #if 2nd file doesn't exist...
        f2 = open(file2, 'w')                      #creates the second file
        for line in f1:
            f2.write(line)
        f2.close()

    print("Done. Check the location folder.")
    sigues = input("Press Y to do it again or X to quit. ")
    if sigues == "y":
        continue
    if sigues == "x":
        break
    
"""
os.path.isfile() came from:
https://docs.python.org/3.6/library/os.path.html

for line in f1:
    f2.write(line)
was based in 'Methods of File Objects' from:
https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
"""
