#Password Generator by Radisa Hussein Rachmadi

import random
import sys
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9","!","@","?","#","$","%","&","*"]
passwordList = []

def settings():
    length = int(input("Length of Password: "))
    numberSymbols = str(input("Include Numbers & Symbols? (y/n): "))
    if numberSymbols == 'y':
        for i in range(len(numbers)):
            combine = letters.append(numbers[i])
        for i in range(length):
            choice = random.randint(0,len(letters) - 1)
            generate = letters[choice]
            passwordList.append(generate)
    else:
        for i in range(length):
            choice = random.randint(0,len(letters) - 1)
            generate = letters[choice]
            passwordList.append(generate)

    convert(passwordList)

def convert(s):
    passwordString = ""
    for i in s:
        passwordString += i
    print("Generated Password: ",passwordString)


settings()

