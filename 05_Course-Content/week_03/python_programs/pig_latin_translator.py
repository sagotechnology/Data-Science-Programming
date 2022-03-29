"""Write code that translates a name into (simplified) Pig Latin. 
(Please do not make this a 'real' Pig Latin translator.) 
Have your script ask the user for his or her name, which can comprise 
first, middle, and/or last parts. For each name part, move the first letter to 
the end of the part and append the letters "ay". Make sure that only the first 
letter of each word in your output is capitalized. You can use the split() 
method on the string to create a list of the name parts. Be sure that your 
script can handle one, two or three name parts separated by spaces. 
This will likely involve a loop.
Your script should re-create the following example exactly:
    
Enter your name: Paul Laskowski

Aulpay Askowskilay"""
# User enters their name.
name_input = input('Please enter your name: ')
print('\n')
# Create a list from user input, split the name between the spaces.
name_list = name_input.split(' ')
# Determine the number of items in the list.
i = 0
j = len(name_list)
while i < j:
    name_pig_latin = name_list[i][1].upper() + name_list[i][2:].lower() + \
    name_list[i][0].lower() + 'ay'
    print(name_pig_latin, end=' ')
    i += 1