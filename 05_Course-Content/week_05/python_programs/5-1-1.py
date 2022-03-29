def sum_digits(x):
    digit_list = [i for i in str(abs(x))]
    sum_x = 0 
    for num in digit_list: 
        if num in '0123456789':
            sum_x += int(num)
    return sum_x

def diff_sum_digits(x):
    diff_x = abs(x) - sum_digits(x)
    return diff_x

def wraps_diff_sum_digits(x):
    wrap = diff_sum_digits(x)
    while wrap >= 10:
        wrap = diff_sum_digits(wrap)
    return wrap
    
    
'''num = input('Enter an integer: ')
for i in num:
    print(i)'''