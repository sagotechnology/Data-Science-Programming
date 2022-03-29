try:
    x = float(input("Enter a number: "))
    print("The reciprocal of your number is", 1/x)
except ValueError:
    print("You did not enter a valid number.")
    
except ZeroDivisionError:
    print("Zero does not have a reciprocal")
except:
    print("something else went wrong.")



'''
flag = 0
while flag == 0:   
    try:
        x = float(input("Enter a number: "))
        print("The reciprocal of your number is", 1/x)
        flag = 1
    except ValueError:
        print("You did not enter a valid number.")
    except ZeroDivisionError:
        print("Zero does not have a reciprocal")
        flag = 1
    except:
        print("something else went wrong.")
'''