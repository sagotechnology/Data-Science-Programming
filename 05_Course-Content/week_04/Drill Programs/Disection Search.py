x = float(input('Enter a number: '))
epsilon = 0.00000000001
num_guess = 0
low = 0
high = x
ans = (high + low) / 2

while high - low >= 2 * epsilon:
    print('low =', low, 'high = ', high)
    num_guess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(ans,'is close to the square root of', x)
print('The number of guesses was', num_guess)