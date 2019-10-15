#multplicaton of user desired number by defining function


def mul(num1,num2):
    for i in num2:
        print(num1,"x",i,"=",num1*i)

num1 = int(input("Enter the number for which multiplication table is required:"))

values = range(1,11)

mul(num1,values)

