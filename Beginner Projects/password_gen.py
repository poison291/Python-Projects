import random
import string


passLength = int(input("Enter The Password Length\n"))

print("Generated Password: ", end="")
for i in range ((passLength+1) // 2):
    random_alpha = random.choice(string.ascii_letters)
    print(random_alpha, end="")
    number = random.randint(1,9)
    print(number, end="")

print()