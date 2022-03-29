word = input('Enter a word: ').lower()
last_letter = 'a'

for letter in word:
    if letter in 'aeiou':
        print(letter, 'is a vowel')
        if letter < last_letter:
            print('The vowels in', word, 'are not in alphabetical order')
            break
        last_letter = letter
else:
    print('The vowels in', word, 'are in alphabetical order')