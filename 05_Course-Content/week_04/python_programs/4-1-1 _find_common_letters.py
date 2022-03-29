word_one = input('Enter one word: ').lower()
word_two = input('Enter another word: ').lower()
common_letters = ''
#iterate through first word
for letter_one in word_one:
#iterate through second word
    for letter_two in word_two:
#if letters are common add to common string
        if letter_one == letter_two and letter_one not in common_letters:
            common_letters += letter_one
#sort string in alphabetical order            
alphabet = 'abcdefghijklmnopqrstuvwxyz'
common_letters_order = ''
for letter in alphabet:
    for letter_common in common_letters:
        if letter == letter_common:
            common_letters_order += letter_common
            
if common_letters == '':
    print('\n\nNo common letters.')
else:
    print('\n\nLetters in common:', common_letters_order)