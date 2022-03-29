
import sys

#from keep_score module import score_word function
#from keep_score import score_word

def score_word(word, rack):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    score = 0
    for letter in word:
        if letter in rack:
            score += scores[letter]
    return score


#define scrabble function
def scrabble(user_input):
    
    if len(user_input) < 2:
        raise Exception("User input must be contain more than two characters\
but less than 7. Please increase characers entered.")
    elif len(user_input) > 7:
        raise Exception("User input must be contain more than two characters\
but less than 7. Please decrease characers entered.")
    elif user_input.count('*') > 1 or user_input.count('?') > 1:
            raise Exception("User input can only contain two wildcards \
one '*' and/or one '?'.")
    elif any(letter not in '?*ABCDEFGHIJKLMNOPQRSTUVWXYZ' for letter in user_input.upper()):
        raise Exception("User input must be a letter or wildcard( * or ?).")
    else:
        rack = user_input.upper()
        
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
        
    '''This portion of the code finds the words in data that can be played given
    the letter is in the rack'''    
    match = []
    for word in data:
        temp = []
        for letter in rack:
            temp.extend(letter)
            count = 0
        for letter in word:
            if letter in temp:
                temp.remove(letter)
                count += 1
            elif '*' in temp:
                temp.remove('*')
                count += 1
            elif '?' in temp:
                temp.remove('?')
                count += 1
            else:
                break
        if count == len(word):
            match.append(word.lower())     
            
    '''Call function score_words from module keep_score. Put all the scores in
    array word_scores.'''        
    word_scores = []
    for word in match:
        word_score = score_word(word.lower(), rack.lower())  
        word_scores.append(word_score)
        
    '''Create a blank list scrabble. If the length of word_scores is equal to 
    the length of match place the first item in both list into a tuple.  Append 
    the tuble to scrabble. Loop through word_scores and match placing all items 
    in scrabble.'''
    scrabble = []    
    if len(word_scores) == len(match):
        for i in range(len(word_scores)):
            t = (word_scores[i], match[i])
            scrabble.append(t)
    scrabble.sort()
    
    '''While the scrabble list is not empty, iterate through the list to find the 
    highest score in alphbet order.'''   
    count = 0
    while scrabble != []:
        #Set largest to -1 to avoid an error when score is 0
        largest = -1
        for i in range(len(scrabble)):
            if scrabble[i][0] > largest:
                largest = scrabble[i][0]
                position = i
        print('(' + str(scrabble[position][0]) + ', ' + scrabble[position][1] + ')')        
        scrabble.pop(position)
        count += 1
    print("Total number of words:", count)
    print()
    
# try and except for scrabble function    
try:        
    #user_input = sys.argv[1]
    scrabble(sys.argv[1])
except Exception as e:
    print(e)