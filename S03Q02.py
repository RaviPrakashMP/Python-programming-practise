num = int(input("Enter a number:"))

def perform_check(num):
    if 0 < num < 10:
        num = num + 7
        num = num % 10
        print(num)

    elif 9 < num < 99:
        num = num**5
        num = num % 10
        print(num)

    elif 99 < num < 999:
        num1 = int(input("Enter another number:"))
        num = num + num1
        num = num % 10
        print(num)

perform_check(num)
