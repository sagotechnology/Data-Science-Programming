def len_score(name):
    return len(name)

def best(operation, names):
    length = 0
    best_name = ''
    for name in names:
        if operation(name) > length:
            length = operation(name)
            best_name = name
    return best_name
   
names = ["Ben", "April", "Zaber", "Alexis", "McJagger", "J.J.", "Madonna"]

print(best(len_score, names)) 