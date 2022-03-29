import sys

#from keep_score module import score_word function
from keep_score import score_word

#define scrabble function
def scrabble(user_input):
    
    if len(user_input) < 2:
        raise Exception("User input must contain more than two characters \
but less than seven. Please increase the amount of characters entered.")
    elif len(user_input) > 7:
        raise Exception("User input must contain more than two characters \
but less than seven. Please decrease the amount of characters entered.")
    elif user_input.count('*') > 1 or user_input.count('?') > 1:
            raise Exception("User input can only contain two wildcards \
one '*' and/or one '?'.")
    elif any(letter not in '?*ABCDEFGHIJKLMNOPQRSTUVWXYZ' for letter in user_input.upper()):
        raise Exception("User input must be a letter or wildcard( * or ?).")
    else:
        rack = user_input.upper()
        
    #Import words from  sowpods.txt
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
        
    #Find words that can be made from rack
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
            
    #Score words
    '''Call function score_words from module keep_score. Put all the scores in
    array word_scores.'''        
    word_scores = []
    for word in match:
        word_score = score_word(word.lower(), rack.lower())  
        word_scores.append(word_score)
     
    #Create list consisting of score and word tuples.
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
    
    #Find and print the results by highest score and alphabetical order.
    '''While the scrabble list is not empty, iterate through the list to find the 
    highest score in alphbet order.'''   
    total_words = 0
    while scrabble != []:
        #Set largest to -1 to avoid an error when score is 0
        largest = -1
        for i in range(len(scrabble)):
            if scrabble[i][0] > largest:
                largest = scrabble[i][0]
                position = i
        print('(' + str(scrabble[position][0]) + ', ' + scrabble[position][1] + ')')        
        scrabble.pop(position)
        total_words += 1
    print("Total number of words:", total_words)
    
# try and except for scrabble function    
try:        
    scrabble(sys.argv[1])
except Exception as e:
    print(e)