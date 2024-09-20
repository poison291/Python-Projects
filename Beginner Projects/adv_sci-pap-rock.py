import random

name = input("What is your name?\n")
print(f"Good Luck! {name}\n")

print("Welcome to Scissors paper Rock game!")
print("The Rules are simple wanna hear?")

askRule = input("Type (Y/N)\n").lower()

if (askRule == "y"):
    print("So If u choose Rock and Bot choose paper! Bot will win\nIf u choose Scissors and Bot choose stone! Bot will win\nIf u choose paper and Bot choose scissors Bot will win!\nAnd Their Vice-versa")


# Declaring The value 

scissors = -1
paper = 0
rock = 1

StringDict = {
    1: "Rock",
    0: "Paper",
    -1: "Scissors"
}

print("Enter Your choice!\n\nRock - 1\nPaper - 0\nScissors - -1\n")
userChoice = int(input(""))


print(f"So u chose {StringDict[userChoice]}\n")

# Declaring Bot choice 

botChoice = random.randint(-1, 1) # i.e -1, 0, 1

# Adding Game Logic

if (userChoice == botChoice):
    print("Its a draw!")
    print(f"Bot choice - {StringDict[botChoice]}")
    print(f"{name} choice - {StringDict[userChoice]}")

else:
    if(userChoice == -1 and botChoice == 0):
        print("Bot won\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")

    elif(userChoice == -1 and botChoice == 1):
        print("Bot Won!\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")

    elif(userChoice == 0 and botChoice == -1):
        print("Bot Won!\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")
        
    elif(userChoice == 0 and botChoice == 1):
        print("You Won!\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")
        
    elif(userChoice == 1 and botChoice == -1):
        print("You Won!\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")
        
    elif(userChoice == 1 and botChoice == 0):
        print("Bot Won!\n")
        print(f"Bot choice - {StringDict[botChoice]}")
        print(f"{name} choice - {StringDict[userChoice]}")

    else:
        print("Something went wrong!")


print("\nThanks for Playing")
