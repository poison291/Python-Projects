import string
word = input("Enter the word!\n").lower()
reverse_word = word[::-1]


# print(reverse_word)

def palindrome(word, reverse):
    if(word == reverse_word):
        print("True")
    else:
        print("False")

palindrome(word, reverse_word)
