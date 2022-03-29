def is_consonant(letter):
    letter = letter.lower()
    if letter in 'aeiou':
        return True

def to_piglatin(word): 
    word = word.lower()
    word_list = word.split(' ')
    item = 0
    while item < len(word_list):
        for letter in word_list[item]:
            if not is_consonant(letter):
                word_list[item] = word_list[item][1:] + word_list[item][0]
            else:
                break
    item += 1        
    return word_list[0].capitalize() + 'ay'