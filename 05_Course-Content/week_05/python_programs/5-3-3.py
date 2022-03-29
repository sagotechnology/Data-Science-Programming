def best(operation, names):
    length = 0
    best_name = ''
    for name in names:
        print(name)
        if operation(name) > length:
            length = operation(name)
            best_name = name
    return best_name
   
names = ["Ben", "April", "Zaber", "Alexis", "McJagger", "J.J.", "Madonna", "AaAa"]

print(best(lambda name : name.count('a') + name.count('A'), names,), "has the most A's.") 
'''
a = [name.count('a') + name.count('A') for name in names]
'''