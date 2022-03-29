#[(x**2 + y**2)**0.5 for x in range(1,26) for y in range(1,26) if ((x**2 + y**2)**00.5) in range(1,26)]
word = 'Welcomed'#input()
word_list = [word[0:i] + word[i+1:] for i in range(len(word))]

'''word_list = []
            
for i in range(len(word)):
    print(i)
    word_list.append(word[0:i] + word[i+1:])'''      
print(word_list)