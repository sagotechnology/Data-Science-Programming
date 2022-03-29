def weighted_avg(grades, weights):
    item = 0 
    total = 0
    total_weights = 0
    if len(grades) != len(weights):
        raise Exception("The number of grades and weights are not equal.")
    while item < 4:
        total += (grades[item] * weights[item])/100
        total_weights += weights[item]
        if weights[item] > 100 or weights[item] < 0:
            raise Exception("Weight " + str(weights[item]) + " does not fall within \
the range of 0 to 100.")
        if grades[item] < 0:
            raise Exception ("Grade "+ str(grades[item]) + " is less than 0.")
        item += 1
    if total_weights != 100:
        raise Exception("Weights do not sum to 100.")    
    return total

grades1 = [88,99,100,70]
weights1 = [30, 30, 30, 5]

grades2 = [78, 75, 80, 99]
weights2 = [110, 10, -20, 0]

grades3 = [84, 80, 67, 97]
weights3 = [50, 25, 25]

grades4 = [100, 80, 90, -10]
weights4 = [20, 25, 25, 30]