'''
def is_consonant(letter):
    letter = letter.lower()
    if letter in 'aeiou':
        return True

def to_piglatin(word): 
    word = word.lower()
    word_list = word.split(' ')
    for word in word_list:
        for letter in word:
            if not is_consonant(letter):
                word = word[1:] + word[0]
            else:
                print(word.capitalize() + 'ay')
'''
def is_consonant(letter):
    if letter in 'aeiou':
        return True

def to_piglatin(word): 
    word = word.lower()
    word_list = word.split(' ')
    for letter in word_list[0]:
        if not is_consonant(letter):
            word_list[0] = word_list[0][1:] + word_list[0][0]
        else:
            return word_list[0].capitalize() + 'ay'