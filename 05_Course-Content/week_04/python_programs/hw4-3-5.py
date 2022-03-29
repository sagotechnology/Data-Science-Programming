word = 'Booted'

word_list = [word[0:i] + letter + word[i+1:] for i in range(len(word)) if word[i] in 'aeiou' for letter in 'aeiou' if letter != word[i]]


'''for i in range(len(word)):
    if word[i] in 'aeiou':
        for letter in 'aeiou':
            if letter != word[i]:
                word_list.append(word[0:i] + letter + word[i+1:])''' 

'''for letter in word:
    print(letter)
    if letter in 'aeiou':
        for vowel in 'aeiou':
            if vowel not in letter:
                print(vowel)'''

"""for i in word:
    if i in 'aeiou':
        print()
        print(i+'-', end = '')
        for vowel in 'aeiou':
            print(vowel, end = '')"""
            