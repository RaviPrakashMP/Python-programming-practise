#Take 2 numbers from the user.Print which number is a 2 digit number
#and which number is a 3 digit number.
#If it is neither, then print the number as it is

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

def perform_check(num1,num2):
    if 9 < num1 < 99:
        print("The entered number is a two digit number")

    elif 99 < num1 < 999:
        print("The entered number is a three digit number")

    else:
        0 < num1 < 10 and 1000 < num1
    print(num1)

    if 9 < num1 < 99:
        print("The entered number is a two digit number")

    elif 99 < num1 < 999:
        print("The entered number is a three digit number")

    else:
        0 < num2 < 10 and 1000 < num2
    print(num2)


perform_check(num1,num2)


    

    
    
