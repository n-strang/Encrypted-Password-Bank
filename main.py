import sys

def mainMenu():
    print("Welcome to the password bank, select from following options: ")
    print("\n1) Add website + password \n2) Remove website + password")
    print("3) Search for password by website name (requires PIN)")
    choice = int(input())
    if(choice == 1):
        createPasswordObject()
    elif(choice == 2):
        removePasswordObject()
    elif (choice == 3):
        searchPasswordObject()
    else:
        print("Please choose options again.")
        sys.exit()

def createPasswordObject():
    website = input("Enter website where its stored: ")
    password = input("Enter the password for the website: ")
    addToDictionary(website, password)

def removePasswordObject():
    print("option2")
    
def searchPasswordObject():
    print("option3")

def addToDictionary(ws, pw):
    pwDict ={}
    pwDict[ws] = pw
    print(pwDict)

class banked_pw:
    def __init__(self, website, pw):
        self.website = website
        self.pw = pw
        
if __name__ == "__main__":
    mainMenu()
    