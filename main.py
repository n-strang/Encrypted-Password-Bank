import sys
import json
import os

saveFile = "passwords.json"

def loadPasswords():
    if os.path.exists(saveFile):
        with open(saveFile, "r") as file:
            return json.load(file)
    return {}

pwDict = loadPasswords()

def savePasswords():
    with open(saveFile, "w") as file:
        json.dump(pwDict, file, indent=4)

def mainMenu():
    choice = 2
    while(choice != 1):
        print("\nWelcome to the password bank, select from following options: ")
        print("\n1) exit program \n2) Add website + password ")
        print("3) Remove website + password \n4) Show all passwords")
        choice = int(input())
        if(choice == 2):
            createPasswords()
        elif(choice == 3):
            removePasswords()
        elif (choice == 4):
            showAllPasswords()

def createPasswords():
    website = input("Enter website where its stored: ")
    password = input("Enter the password for the website: ")
    addToDictionary(website, password)
    savePasswords()
    print("\nSuccessfully added information.")

def addToDictionary(ws, pw):
    pwDict[ws] = pw

def removePasswords():
    print("Please type the website you wish to remove")
    removeTarget = input()
    if removeTarget in pwDict:
        del pwDict[removeTarget]
        savePasswords()
        print(f"\nSuccessfully removed {removeTarget}.")
    else:
        print(f"\n{removeTarget} was not found in the password bank.")

def showAllPasswords():
    print(pwDict)

if __name__ == "__main__":
    mainMenu()  
