row = x = int(input("Enter an integer: "))
while row >= 1:
    print(" ")
    columns = x
    while columns >= 0:
        print(columns, end = " ")
        columns -= 1
    row -= 1