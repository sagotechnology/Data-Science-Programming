name = input("Enter your name: ")
name_lower_case  = name.lower()
name_reverse = name_lower_case[::-1]
if name_reverse == name_lower_case:
    print(name,'\nPalindrome!')
else:
    print()