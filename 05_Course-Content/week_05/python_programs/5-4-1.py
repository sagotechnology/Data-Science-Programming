def Fibonacci(n):
    if n <= 1:
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))
'''
number = int(input('Enter a number: ')) #user enters a number
fibonacci = [1] #add 1 to the fibonacci list
if number > 0: #check if interger is greater than zero
    fibonacci.append(1) #add anotheer 1 to the fibonaci list    
    while fibonacci[-1] + fibonacci[-2] <= number: #while last two items sum is less than or equl to number
        fibonacci.append(fibonacci[-2] + fibonacci[-1]) #qppend list with last and second variable
    i = 0
    j = len(fibonacci) #find the length of the fibonact series 
    print('')
    while i < j:
        print(fibonacci[i], end = ' ') #print the item, add a space
        i += 1
'''