# library imports
import sys
import json
import os
from cryptography.fernet import Fernet

# file saves
saveFile = "passwords.json"
keyFile = "key.key"

# load encryption key / gen new one if it doesnt exist
def loadKey():
    if os.path.exists(keyFile):
        with open(keyFile, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(keyFile, "wb") as f:
        f.write(key)
    return key

# create cipher obj using key
cipher = Fernet(loadKey())

# load passwords from json and decrypt
def loadPasswords():
    if os.path.exists(saveFile):
        with open(saveFile, "r") as file:
            encrypted_data = json.load(file)
        return {site: cipher.decrypt(pw.encode()).decode() for site, pw in encrypted_data.items()}
    return {}

pwDict = loadPasswords()

# encrypt all passwords and save to json file
def savePasswords():
    encrypted_data = {site: cipher.encrypt(pw.encode()).decode() for site, pw in pwDict.items()}
    with open(saveFile, "w") as file:
        json.dump(encrypted_data, file, indent=4)

# menu loop
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

# insert new password/site combo
def createPasswords():
    website = input("Enter website where its stored: ")
    password = input("Enter the password for the website: ")
    addToDictionary(website, password)
    savePasswords()
    print("\nSuccessfully added information.")

# push entries into pwDict
def addToDictionary(ws, pw):
    pwDict[ws] = pw

# remove a password/site combo from pwDict
def removePasswords():
    print("Please type the website you wish to remove")
    removeTarget = input()
    if removeTarget in pwDict:
        del pwDict[removeTarget]
        savePasswords()
        print(f"\nSuccessfully removed {removeTarget}.")
    else:
        print(f"\n{removeTarget} was not found in the password bank.")

# show all passwords
def showAllPasswords():
    print(pwDict)

if __name__ == "__main__":
    mainMenu()  
