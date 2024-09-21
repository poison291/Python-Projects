num1 = int(input("Enter Your Number!\n"))

print("Enter The Operation(+, -, *, /)")
operation = input("")

num2 = int(input("Enter Your Number!\n"))




if (operation == "+"):
    print(f"The Sum of {num1} and {num2} is {num1 + num2}")

elif(operation == "-"):
    print(f"The Difference of {num1} and {num2} is {num1 - num2}")
    
elif(operation == "*"):
    print(f"The Product of {num1} and {num2} is {num1 * num2}")
    
elif(operation == "/"):
    if(num2 == 0):
        print("Please Enter Valid Divisible | 0 cant be divided")
    else:
        print(f"The Division of {num1} and {num2} is {num1 / num2}")

else:
    print("Invalid Operations")