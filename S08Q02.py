number = int(input("Enter a number:"))

if number < 10:
    number =  number + 7
    number = number % 10
    print(number)

if 9 < number < 99:
    number = number**5
    new_number = str(number)
    new_number = new_number[-2:]
    print(new_number)

if 99 < number < 1000:
    new_number = int(input("Enter another number")) 
    number = number + new_number
    new_number_1 = str(number)
    new_number_1 = new_number_1[-3:]
    print(new_number_1)
    
    


                     
                 
