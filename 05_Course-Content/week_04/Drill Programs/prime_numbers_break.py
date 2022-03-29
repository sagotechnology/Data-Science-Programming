x = int(input('Enter a number: '))
prime = True

for i in range(2,x):
    print('Now checking possible divsor', i)
    if x % i == 0:
        prime = False
        break 
if prime == True:
     print(x, 'is prime')
else:
    print(x, 'is not prime')