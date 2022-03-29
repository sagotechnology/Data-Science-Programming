def score_word(word, rack):
    '''This function uses the scores dictionary to produce a word score \
    based on the letters in the word.  A word and the rack is passed in \ 
    the rack is made into a list and the letters of the word are compared to \
    the list.  If a letter in the word matches the letter in the list the \
    letter is added to the score and removed from the list to avoid duplicate \
    scoring of the same letter'''
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    score = 0
    word_list = [letter for letter in rack]
    for letter in word:
        if letter in word_list:
            score += scores[letter]
            word_list.remove(letter)
    return score
