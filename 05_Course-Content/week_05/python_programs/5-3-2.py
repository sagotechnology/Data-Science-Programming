def number_of_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in 'aeiou':
            count += 1
    return count        