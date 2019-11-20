# Guess the Number by Radisa Hussein Rachmadi
import random
import sys

#win variable for end of game
win = 0

#User plays game
start = input("Do you want to start the game? (y/n) : ")
zeo = 0
#Decision Loop
while True:
    if start == "y":
        print("Okay Good, lets start!")
        break
    elif start == "n":
        print("Aw alright then  :(")
        sys.exit(1)

    else:
        print("Hey that ain't an answer!")
        sys.exit(1)

#number range

numberRange = (int(input("Range of Number: ")))
print("Number Range : ", str(numberRange))
number = random.randint(0, numberRange)
tries = (int(input("How many tries? : ")))
print("Chances : ", tries)

#Game Start
print("--------------------")
print("Start Game")
print("Number Range: ", str(numberRange))
print("Chances left: ", str(tries))

#first while true for "tries"/"chances" counter
while True:
    if win == 1:
        break

    elif tries > 0:

        #second while true for too high too low counter
        while True:
            guess = int(input("Guess Number: "))
            if guess > number:
                print("Your guess is too high!")
                tries -= 1
                print("You have", tries, "chances left!")
                continue

            elif guess < number:
                print("Your guess is too low..")
                tries -= 1
                print("You have", tries, "chances left!")
                continue

            else:
                win = 1
                print("Correct! The number was", number)
                break

    else:
        print("Aww you have no more chances left, gg")
        break





