"""
Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter.
"""

with open("Dhoni.txt") as FH:

    text = FH.read()

    all_lines = text.split('\n')

    for line in all_lines:

        words = line.split(".")

        if words[0] >= "A" and words[0] <= "Z":

            print(line)

        
            
