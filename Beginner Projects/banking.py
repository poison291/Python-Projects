userBalance = 0 # lets this is user balance


# Main Menu
def menu():
    print("Welcome to Poison Bank\n")
    print("1- To Check Balance")
    print("2- To Deposite Money")
    print("3- To Withdraw Money")
    print("4 - To exit\n")
    

#Check balance
def balance():
    print(f"Your Current balance is {userBalance}\n")

# Deposite Section
def deposite(amount):
    global userBalance
    userBalance = userBalance + amount
    print(f"Succesfuly! Rs.{amount} deposited")
    print(f"Your Current balance is {userBalance}\n")


# Withdraw section
def withDraw(amount):
    global userBalance
    if userBalance > amount:
        userBalance = userBalance - amount
        print(f"Succesfuly! Rs.{amount} Withdrawn")
        print(f"Your Current balance is {userBalance}\n")
    else:
        print(f"You have Rs.{userBalance}! You cant withdraw\n")


while True:
    menu()
    choice = input("Enter The Task You want to perform\n")
    if (choice == "1"):
        balance()
    elif(choice == "2"):
        Todepo = int(input("Enter The amount to deposite\n"))
        deposite(Todepo)
        
    elif(choice == "3"):
        Towith = int(input("Enter The amount to Withdraw\n"))
        withDraw(Towith)
        
    elif(choice == "4"):
        print("GoodBye!")
        break
        
    else:
        print("Invalid! choice Please choose from 1 to 4\n")