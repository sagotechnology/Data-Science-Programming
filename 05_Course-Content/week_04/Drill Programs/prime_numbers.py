x = int(input('Eneter a number: '))
prime = True

for i in range(2,x):
    if x % i == 0:
        prime = False
        print(x, 'is not a prime number. It is divisable by', i)
if prime == True:
     print(x, 'is prime')
else:
    print(x, 'is not prime')