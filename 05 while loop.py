number=0
while number != 12:
    number = number + 2
    print ("the number is", number)

answer="N"
while answer != "Y":
    print("are we there yet?")
    answer = input ("Please respond Y or N")
print("Yay! We are there!")


username = ""
while not username:
    username = input("Please enter your username: ")

import sys

answerOK = False
while answerOK == False:

    answer = input("Exit? y or n ").upper()
    if answer == "Y":
         answerOK = True

exit(sys)
