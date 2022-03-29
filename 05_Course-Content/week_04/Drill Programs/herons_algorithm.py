x = float(input('Enter a number: '))

epsilon = 0.00001
num_guesses = 0
ans = 1

while abs(x/ans - ans) > epsilon:
    ans = ((x/ans + ans)/2)
    num_guesses += 1
print(ans, 'is close to the square root of x')
print(num_guesses)
