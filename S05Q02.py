

num = []

one_digit = []

two_digit = []

three_digit = []

while True:
    num1 = int(input("Enter a value:"))
    num.append(num1)
    
    if num1 == 0:
        break

for num1 in num:
    if num1 < 10 :
        one_digit.append(num1)
        
    elif num1 > 9 and num1 < 100:
        two_digit.append(num1)
       

    elif num1 > 99 and num1 < 1000:
        three_digit.append(num1)
        

print("The number of single_digit are",len(one_digit))
print("The number of two_digit are",len(two_digit))
print("The number of three_digit are",len(three_digit))
print("The maximum number among entered numbers are",max(num))
print("The minimum number among entered numbers are",min(num))
