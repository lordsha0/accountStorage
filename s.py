#! /usr/bin/python3

import os


userChoiceIsValid = False

while(not(userChoiceIsValid)):
    print("Do you want to add, fetch or update?")
    userChoice = input()
    
    if(userChoice == 'a' or userChoice == "add" or userChoice == 'f' or userChoice == "fetch" or userChoice == 'u' or userChoice == "update"):
        userChoiceIsValid = True
    else:
        print("Please choose a valid option")

if(userChoiceIsValid):
