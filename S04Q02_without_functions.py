E = int(input("Enter the marks scored in English exam:"))
S = int(input("Enter the marks scored in Science exam:"))
M = int(input("Enter the marks scored in Mathematics exam:"))

percentage = ((E+S+M)/270)*100

if percentage > 90:
    print("The student has scored First Class")

elif 75 < percentage < 90:
    print("The student has scored second class")

elif 35 < percentage < 75:
    print("The student scored average")

else:
    print("The student is failed")
    
