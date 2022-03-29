x = int(input('Enter a number: '))

for i in range(2,x):
    print('Now checking possible divsor', i)
    if x % i == 0:
        print(x, 'is not a prime number')
        break
else:
    print(x, 'is a prime number')
    
