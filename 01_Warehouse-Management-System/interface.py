# loop user input until correct size is entered
def input_size():
    size  = input("Please enter product size: ")         
    while check_size(size) == 1:
        print("\n" + size, "is an invalid size.\n")
        size = input("Please enter product size: ")
    return size

# check for correct size
def check_size(size):
    if size not in ['0', '1', '2', '3', '4', '5', '6', '7']:
        return 1
    else:
        return 0
    
# loop user input until correct storage is entered    
def input_storage():
    storage  = input("Please enter storage destination: ")      
    while check_storage(storage) == 1:
        print("\n" + storage, "is an invalid storage location.\n")
        storage = input("Please enter storage destination: ")
    return storage

# check for correct storage
def check_storage(storage):
    if storage not in ['a', 'b', 'c', 'd']:
        return 1
    else:
        return 0    
  
# loop user input until correct variety is entered      
def input_variety():
    # Input order variety
    variety = input("Please enter product variety: ")
    while check_variety(variety) == 1:
        print("\n" + variety, "is an invalid variety.\n")
        variety = input("Please enter product variety: ")
    return variety

# check for correct variety
def check_variety(variety):
    if variety not in ['purple', 'red', 'yellow', 'orgyellow']:
        return 1
    else:
        return 0

# loop user input until correct weight is entered
def input_weight():
    weight = input("Please enter product quantity in lbs: ")
    while check_int(weight) == 1:
        print("\n" + weight,"is not a valid weight.\n")
        weight = input("Please enter product quantity in lbs: ")
    return int(weight)

# loop user input until correct number of totes is entered
def input_tote():
    tote = input("Please enter number of totes: ")
    while check_int(tote) == 1:
        print("\n" + tote,"is not a valid for tote quantity.\n")
        tote = input("Please enter number of totes: ")
    return int(tote)

# check that user input is an integer
def check_int(num):
    try:
        user_input = int(num)
        if type(user_input) == int:
            return 0
    except ValueError:
        return 1   

# help menu at the beginning of the program 
def help_menu():
    print("\nWelcome to SamCo's Warehouse Management System.\n"
      "This program simulates a warehouse management system.  The primary user\n" 
      "interaction deals with executing Receiving Line orders to create and place\n" 
      "totes into the inventory/Cold Storage, as well as executing Wash Line orders\n" 
      "to remove totes from the Cold Storage.  Other functionality is built into the\n" 
      "system but is self-explanatory.  Please explore the program and have fun!\n")