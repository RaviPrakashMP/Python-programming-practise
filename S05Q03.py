#Take a number as input from the user.
#Print all the squares of numbers from 1 to any large number. 
#The numbers printed should be less than 
#The number given as input by the user
n = int(input("Enter a number:"))

for a in range(1,n):
    a = a**2

    if a < n:
        print(a)

    if a > n:
        break


        
   



