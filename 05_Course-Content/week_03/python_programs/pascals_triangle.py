### Q3-5 Grading Tag: Please put your entire solution in this cell. Don't edit this line.
row = int(input('Enter a row number: '))
pascal = []
#create the number of list specified by row, add '1' to all lists
for i in range(row):
    pascal.append([])
    pascal[i].append(1)
#exclude pascal[0] and pascal[1], every list there after add items 0+1, 1+2, ... ,n + (n+1)
    for j in range(1,i):
        pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
#append a 1 to the end of all pascal[i] except pascal[0]        
    if i != 0:
        pascal[i].append(1)
for i in range(row - 1):
    while len(pascal[i]) < row:
        pascal[i].append(0)
print()
#print row     
for i in range(row):
    print()    
    for j in range(row):
        print(pascal[i][j], end =' ')