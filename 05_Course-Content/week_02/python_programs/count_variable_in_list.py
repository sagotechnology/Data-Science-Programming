name = input("Enter a name: ")
#
i = 0
while i < len(name):
    j = len(name) - 1 - i
    if i == 0:
        print(name[j].upper(), end = '')
    else:
        print(name[j].lower(), end = '')
    i += 1

    