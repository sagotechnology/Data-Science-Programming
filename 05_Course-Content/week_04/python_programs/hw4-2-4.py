x = float(input("Enter a number to find the square root: "))
epsilon = 0.0000000001
num_guesses = 0
guess = 0.0
step = 1
for i in range(11):
    if guess**2 > x:
        guess -= step
        print(guess)
        step /= 10
    while guess**2 < x:
        guess += step
        num_guesses += 1
print(guess)
print('The square root of', x,'is',str(guess)[:12])







"""while ans != 3.16:#float('{:,.2f}'.format(3.1622776601):
    if ans <= 3.16:
        ans += epsilon
    else:#float('{:,.2f}'.format(3.1622776601):
        ans -= epsilon
        epsilon /= 10
    num_guesses += 1
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)"""