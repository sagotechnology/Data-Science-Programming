row = x = int(input("Enter an integer: "))
while row >= 1:
    print(" ")
    column = x
    while column >= 0:
        if column % 2 == 0:
            print("__", end = "")
        else:
            print("$$",  end = "")
        column -= 1
    row -= 1