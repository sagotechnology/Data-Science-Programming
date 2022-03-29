data = input("Enter words separated by spaces: ")
words = data.split()

guess = ""
for word in words:
    if len(word) > len(guess):
        guess = word
        
print("The longest word is", guess)
    
