a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
mean = int(input("""Please type
1 for the arithmetic mean
2 for the geometric mean
3 for the root-mean-square

enter selection: """))
#print('\n')
#
# arithmetic mean
if mean == 1:
    print('\n' + 'arithmetic mean = ', (a + b) / 2)
elif mean == 2:
    print('\n' + 'The geometric mean = ', (a * b) ** 0.5)
elif mean == 3:
    print('\n' + 'The root-mean-square = ', (((a ** 2) + (b ** 2)) / 2) ** 0.5)
else:
    print('\n' + "invalid entry")