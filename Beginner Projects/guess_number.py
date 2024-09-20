import random


number = random.randint(1, 100)

# print(number)
attempt = 1

guess = int(input("Enter your Guess\n"))

while guess != number:
    if (guess > number):
        print("Your Guess is too High!")
    else:
        print("Your Guess is too Low!")
    guess = int(input("Enter your Guess"))
    attempt +=1
    
print(f"Well done You guess the number {number} in {attempt} attempt")

