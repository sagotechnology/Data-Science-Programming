def grt_five(item):
    if type(item) == int or type(item) == float:
        return item > 5
    if item is None:
        return 1
    else:
        return item

def compute(value):
 
    if type(value) == int or type(value) == float:
        return value ** 2
    elif type(value) == str:
        return value[::-1]
    else:
        return None


'''def compute(value):
    try:
        if type(value) == int or type(value) == float:
            return value ** 2
        if type(value) == str:
            return value[::-1]
        else:
            print("Please enter an integer, float, or string.")
    except NameError:
        print('Help')'''
        

'''try:
    if type(value) == int or type(value) == float:
        print(value ** 2)
    if type(value) == str:
        print(value[::-1])
    else:
        print("Please enter an integer, float, or string.")
except (ValueError, NameError):
    print("Oops!  That was no valid number.  Try again...")'''