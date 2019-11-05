"""
Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter.
"""
file_name = input("Enter the file to be executed:")

with open(file_name) as FH:
     
for line in FH:

        words = line.split(".")

        if words[0] >= "A" and words[0] <= "Z":

            print(line)

        
            
