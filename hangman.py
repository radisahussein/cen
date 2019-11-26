import random
import sys

listSelectedWord = []
listCensoredWord = []
censoredWord = ""
chances = 5

def start():
    startGame = str(input("Start game? (y/n) : "))
    if startGame == "y":
        hangman()
    else:
        print("Aww Alright")
        sys.exit(1)

def hangman():
    global chances

    censoredWord = ""
    wordlist = ["elephant"]
    selectedWord = wordlist[random.randint(0,len(wordlist)-1)]
    listSelectedWord = list(selectedWord)
    listCensoredWord = []
    for i in listSelectedWord:
        listCensoredWord.append("*")

    censoredWord = censoredWord.join(listCensoredWord)
    print("-----------------------------")
    print("Word to guess: ")
    print(censoredWord)

#game
    while True:
        if chances > 0:
            if listCensoredWord == listSelectedWord:
                print("-----------------------------")
                print("you got it!")
                selection = input("Would you like to try again? (y/n) : ")
                if selection == "y":
                    hangman()
                else:
                    sys.exit(1)
                print("-----------------------------")
                break
            else:
                print("-----------------------------")
                guess = str(input("Guess a letter: "))
                if len(guess) == 1:
                    if guess.lower() in listCensoredWord:
                        print("-----------------------------")
                        print("You already guessed that!")
                        continue
                    else:
                        if guess.lower() in selectedWord:
                            print("-----------------------------")
                            print("Correct!")
                            positions = [n for n,x in enumerate(selectedWord) if x==guess.lower()]
                            for i in positions:
                                listCensoredWord[i] = guess.lower()
                            censoredWord = ""
                            for ele in listCensoredWord:
                                censoredWord += ele
                            print(censoredWord)

                        else:
                            print("-----------------------------")
                            print("incorrect!")
                            chances -= 1
                            print(chances,"chances left")
                else:
                    print("-----------------------------")
                    print("Please enter only 1 character!")
                    continue
        else:
            print("-----------------------------")
            print("Aww You lost :(")
            selection = input("Would you like to try again? (y/n) : ")
            if selection == "y":
                start()
            else:
                sys.exit(1)
start()
