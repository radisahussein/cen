#Rock Paper Scissors by Radisa Hussein Rachmadi

import random
import sys

def game():
    settings = int(input("Game best of? : "))
    playerWins = 0
    computerWins = 0
    choices = ["Rock", "Paper", "Scissors"]

    while True:
        if playerWins + computerWins < settings:
            print("--------------------------------------------")
            computerChoice = random.choice(choices)
            playerChoice = str(input("Rock, Paper, Scissors? : "))

            if playerChoice == computerChoice:
                print("You chose",playerChoice,"Computer Chose",computerChoice)
                print("Draw!")
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Rock" and computerChoice == "Paper":
                print("You chose Rock, Computer Chose Paper")
                print("You Lost!")
                computerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Rock" and computerChoice == "Scissors":
                print("You chose Rock, Computer Chose Scissors")
                print("You Won!")
                playerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Paper" and computerChoice == "Scissors":
                print("You chose Paper, Computer Chose Scissors")
                print("You Lost!")
                computerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Paper" and computerChoice == "Rock":
                print("You chose Paper, Computer Chose Rock")
                print("You Won!")
                playerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Scissors" and computerChoice == "Rock":
                print("You chose Scissors, Computer Chose Rock")
                print("You Lost!")
                computerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            elif playerChoice == "Scissors" and computerChoice == "Paper":
                print("You chose Scissors, Computer Chose Paper")
                print("You Won!")
                playerWins += 1
                print("You:", playerWins, "vs", "Computer:", computerWins)

            else:
                print("That ain't a choice! (Case-Sensitive btw)")
                continue

        else:
            print("-----------------------------------------------")
            print("Result: ")
            print("You:", playerWins, "vs", "Computer:", computerWins)
            if playerWins > computerWins:
                print("YOU WON THE GAME!")
            else:
                print("COMPUTER WON THE GAME!")
            print("End of Game")
            break


def startFunction():
    start = input("Start the game? (y/n) : ")
    if start == "y":
        game()

    elif start == "n":
        print("Aw alright bye!")
        sys.exit(1)

    else:
        print("That ain't an answer buddy!")
        sys.exit(1)

startFunction()




