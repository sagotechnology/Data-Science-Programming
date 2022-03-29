# Q4-2-4 Grading Tag:
x = float(input("Enter a number to find the square root: "))
epsilon = 0.0000000001
num_guesses = 0
guess = 0.0
step = 1
while step > epsilon:
    while (guess + step)**2 < x:
        guess += step
        num_guesses += 1   
    step /= 10
print('The square root of', x,'is','{:,.10f}'.format(guess))







"""while ans != 3.16:#float('{:,.2f}'.format(3.1622776601):
    if ans <= 3.16:
        ans += epsilon
    else:#float('{:,.2f}'.format(3.1622776601):
        ans -= epsilon
        epsilon /= 10
    num_guesses += 1
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)"""