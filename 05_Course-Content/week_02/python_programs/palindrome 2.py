name = input("Enter your name: ")
#
i = 0
eman = ''
while i < len(name):
    j = len(name) - 1 - i
    if i == 0:
        eman = name[j].upper()
        print(name[j].upper())
    else:
        eman = eman + name[j].lower()
        print(name[j].lower())
    i += 1
if name.lower() == eman.lower():
    print('\nPalindrome!')
    