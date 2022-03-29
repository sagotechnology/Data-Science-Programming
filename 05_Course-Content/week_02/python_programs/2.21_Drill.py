x = int(input("Enter an integer: "))
if x % 2 == 0:
    print("$$")
else:
    print(x)
print(" ")
while x >= 0:
    print("T-minus")
    print(x)
    x -= 1
print("Blast off!")