x = int(input('Eneter a number: '))
prime = True

i = 2

while i < x and prime:
    if x % i == 0:
        prime = False
        print(x, 'is not a prime number. It is divisable by', i)
    i += 1    
print('kept looping until i is', i)  
if prime == True:
     print(x, 'is prime')
else:
    print(x, 'is not prime')