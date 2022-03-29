def input_size():
    size  = input("Please enter product size: ")         
    while check_size(size) == 1:
        print("\n" + size, "is an invalid size.\n")
        size = input("Please enter product size: ")
    return size

def check_size(size):
    if size not in ['0', '1', '2', '3', '4', '5', '6', '7']:
        return 1
    else:
        return 0
    
def input_storage():
    storage  = input("Please enter storage destination: ")      
    while check_storage(storage) == 1:
        print("\n" + storage, "is an invalid storage location.\n")
        storage = input("Please enter storage destination: ")
    return storage

def check_storage(storage):
    if storage not in ['a', 'b', 'c', 'd']:
        return 1
    else:
        return 0    
        
def input_variety():
    # Input order variety
    variety = input("Please enter product variety: ")
    while check_variety(variety) == 1:
        print("\n" + variety, "is an invalid variety.\n")
        variety = input("Please enter product variety: ")
    return variety

def check_variety(variety):
    if variety not in ['purple', 'red', 'yellow', 'orgyellow']:
        return 1
    else:
        return 0

def input_weight():
    weight = input("Please enter product quantity in lbs: ")
    while check_int(weight) == 1:
        print("\n" + weight,"is not a valid weight.\n")
        weight = input("Please enter product quantity in lbs: ")
    return int(weight)

def input_tote():
    tote = input("Please enter number of totes: ")
    while check_int(tote) == 1:
        print("\n" + tote,"is not a valid for tote quantity.\n")
        tote = input("Please enter number of totes: ")
    return int(tote)

def check_int(num):
    try:
        user_input = int(num)
        if type(user_input) == int:
            return 0
    except ValueError:
        return 1     

def input_aisle():
    aisle = input("Please enter aisle: ")
    while check_aisle(aisle) == 1:
        print("\n" + aisle,"is not a valid aisle.\n")
        aisle = input("Please enter aisle: ")
    return int(aisle)    
    
def check_aisle(num):
    try:
        user_input = int(num)
        if type(user_input) == int and user_input < len(a.location):
            return 0
        else:
            return 1
    except ValueError:
        return 1  
    
def input_column():
    column = input("Please enter column: ")
    while check_column(column) == 1:
        print("\n" + column,"is not a valid column.\n")
        column = input("Please enter column: ")
    return int(column)    
    
def check_column(num):
    try:
        user_input = int(num)
        if type(user_input) == int and user_input < len(a.location[0]):
            return 0
        else:
            return 1
    except ValueError:
        return 1     

def input_row():
    row = input("Please enter row: ")
    while check_row(row) == 1:
        print("\n" + row,"is not a valid row.\n")
        row = input("Please enter row: ")
    return int(row)    
    
def check_row(num):
    try:
        user_input = int(num)
        if type(user_input) == int and user_input < len(a.location[0][0]):
            return 0
        else:
            return 1
    except ValueError:
        return 1     
    
def help_menu():
    print("\nWelcome to SamCo's Warehouse Management System.\n"
      "This program simulates a warehouse management system.  The primary user\n" 
      "interaction deals with executing Receiving Line orders to create and place\n" 
      "totes into the inventory/Cold Storage, as well as executing Wash Line orders\n" 
      "to remove totes from the Cold Storage.  Other functionality is built into the\n" 
      "system but is self-explanatory.  Please explore the program and have fun!\n")