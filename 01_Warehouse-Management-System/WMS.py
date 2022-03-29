import datetime
import random



            
def RandomSize():
    num = random.randint(0,7)
    return(str(num))
    
def RandomWeight():
    num = random.randint(1200,1250)
    return num
            
def Empty(tote_list):
    # iterate through every tote in tote_list
    for empty in tote_list:
        # if the item in the list is an int then it is empty
        if type(empty) == int:
            return empty   

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

class Order():
    count = 0
    
    def __init__(self, variety):
        self.variety = variety
        

class ReceiveOrder(Order):
    
    count = 0
    # An order must contain a varitey and the amount of pounds in the order
    def __init__(self, variety, pounds):
        super().__init__(variety) 
        self.pounds = pounds
        ReceiveOrder.count += 1
        self.order_currentDT = datetime.datetime.now()
        self.order_date = self.order_currentDT.month, self.order_currentDT.day, self.order_currentDT.year
        self.order_time = self.order_currentDT.hour, self.order_currentDT.minute
        
    # This function runs the order and creates totes    
    def execute(self):
        self.remaining = self.pounds
        while self.remaining >= 1250:
            # Find an empty tote
            self.i = Empty(tote)
            # Create a tote if class Tote
            tote[self.i] = Tote(self.variety, RandomSize(), RandomWeight())
            # Find a locaiton in Cold Storage A that is empty
            self.j = a.get_location()
            # Place a tote in a Cold Storage location
            a.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
            # Set tote location 
            tote[self.i].location = (a.name.capitalize(), self.j[0], self.j[1], self.j[2])
            # Once the order's remaining product is less than 12oo create last tote
            self.remaining -= tote[self.i].tote_weight
        self.i = Empty(tote)
        tote[self.i] = Tote(self.variety, RandomSize(), self.remaining)
            
            
        # Find a locaiton in Cold Storage A that is empty
        self.j = a.get_location()
        # Place a tote in a Cold Storage location
        a.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
        # Set tote location 
        tote[self.i].location = (a.name.capitalize(), self.j[0], self.j[1], self.j[2])
        
    def __repr__(self):
        return 'Variety : ' +str(self.variety).capitalize() + '\n' \
                + 'Pounds : ' + str(self.pounds) + "\n" \
                + 'Date: ' + str(self.order_currentDT.strftime("%m/%d/%Y")) + "\n" \
                + 'Time: ' + str(self.order_currentDT.strftime("%H:%M:%S"))
                
class WashOrder(Order):
    count = 0
    
    # An order must contain a varitey and the amount of pounds in the order
    def __init__(self, variety, size, totes):
        super().__init__(variety) 
        self.size = size
        self.totes = totes
        WashOrder.count += 1
        self.pick_list = []
        
    # This function runs the order and creates totes    
    def execute(self):
        self.tote_count = 0
        self.remaining = self.totes
        while self.remaining > 0:
            # Find an empty tote
            tote = a.get_tote(self.variety, self.size)
            if type(tote) == Tote:
                self.pick_list.append(tote)
                self.remaining -= 1
                self.tote_count += 1
            else:
                print("There are no remaining totes which match your criteria.\n", 
                      self.tote_count, "totes where removed from inventory.\n")
                break
        for tote in self.pick_list:
                        print(tote)
                        print() 
        
        
    def __repr__(self):
        return 'Variety : ' +str(self.variety).capitalize() + '\n' \
                + 'Pounds : ' + str(self.pounds) + "\n" \
                + 'Date: ' + str(self.order_currentDT.strftime("%m/%d/%Y")) + "\n" \
                + 'Time: ' + str(self.order_currentDT.strftime("%H:%M:%S"))

class Tote():
    count = 0
    
    # Initialize tote with attributes: ID, variety, size, and weight
    def __init__(self, in_variety, in_size, in_weight = 0, in_location = 'yard'):
        varieties = ['purple', 'red','yellow']
        sizes = ['0', '1', '2', '3', '4', '5', '6', '7']
        Tote.count += 1
        self.__tote_id = Tote.count
        if in_variety not in varieties:
            raise Exception("Invalid variety.")
        self.tote_variety = in_variety
        if in_size not in sizes:
            raise Exception("Invalid size.")
        self.tote_size = in_size
        self.tote_weight = in_weight
        self.tote_location = in_location
        self.tote_currentDT = datetime.datetime.now()
        self.tote_date = self.tote_currentDT.month, self.tote_currentDT.day, self.tote_currentDT.year
        self.tote_time = self.tote_currentDT.hour, self.tote_currentDT.minute
        
    @classmethod
    def tote_total(cls):
        return cls.count
    
    # Create getter for tote id
    @property
    def id_num(self):
        return self.__tote_id    
    
    # tote variery getter and setter  
    @property
    def variety(self):
        return self.tote_variety
    @variety.setter
    def variety(self, in_variety):
        varieties = ['purple', 'red','yellow']
        if in_variety not in varieties:
            raise Exception("Invalid variety.")
        self.tote_variety = in_variety
        
    # tote size getter and setter
    @property
    def size(self):
        return self.tote_size
    @size.setter
    def size(self, in_size):
        sizes = ['9', '0', '1', '2', '3', '4', '5', '6']
        if in_size not in sizes:
            raise Exception("Invalid size.")
        self.tote_size = in_size
        
    # tote weight getter and setter
    @property
    def weight(self):
        return self.tote_weight
    @weight.setter
    def weight(self, in_weight):
        self.tote_weight = in_weight
        
    #tote location getter and setter
    @property
    def location(self):
        return self.tote_location
    @location.setter
    def location(self, in_location):
        self.tote_location = in_location
    def __repr__(self):
        return 'tote ID: ' + str(self.__tote_id) + '\n' \
                + 'Variety: ' + self.tote_variety.capitalize() + '\n' \
                + 'Size: ' + self.tote_size + '\n' \
                + 'Weight: ' + str(self.tote_weight) + 'lbs' + '\n' \
                + 'Location: ' + str(self.tote_location) + '\n' \
                + 'Date: ' + str(self.tote_currentDT.strftime("%m/%d/%Y")) + "\n" \
                + 'Time: ' + str(self.tote_currentDT.strftime("%H:%M:%S"))
                
class ColdStorage():
    
    def __init__(self, name, num_aisles = 0, num_columns = 0, num_rows = 0):
        self.location = []
        self.name = name
        for self.a in range(num_aisles):
            self.location.append([])
            for self.c in range(num_columns):
                self.location[self.a].append([])
                for self.r in range(num_rows):
                    self.location[self.a][self.c].append(0)
    
    def get_location(self):
        for self.a in range(len(self.location)):
            for self.c in range(len(self.location[self.a])):
                for self.r in range(len(self.location[self.a][self.c])):
                    if type(self.location[self.a][self.c][self.r]) != Tote:
                        return self.a, self.c, self.r  
    
    def display(self):
        for self.a in range(len(self.location)):
            for self.c in range(len(self.location[self.a])):
                for self.r in range(len(self.location[self.a][self.c])):
                    if type(self.location[self.a][self.c][self.r]) == Tote:
                        print(self.location[self.a][self.c][self.r])
                        print()
                        
    def display_size(self, size):
        self.size = size
        for self.a in range(len(self.location)):
            for self.c in range(len(self.location[self.a])):
                for self.r in range(len(self.location[self.a][self.c])):
                    if type(self.location[self.a][self.c][self.r]) == Tote and \
                        self.location[self.a][self.c][self.r].tote_size == str(self.size):
                        print(self.location[self.a][self.c][self.r])
                        print()
    
    def display_variety(self, variety):
        self.variety = str(variety)
        if self.variety in ['purple', 'red', 'yellow']:
            for self.a in range(len(self.location)):
                for self.c in range(len(self.location[self.a])):
                    for self.r in range(len(self.location[self.a][self.c])):
                        if type(self.location[self.a][self.c][self.r]) == Tote and \
                            self.location[self.a][self.c][self.r].tote_variety == str(self.variety):
                            print(self.location[self.a][self.c][self.r])
                            print()
        else:
            print(self.variety.capitalize(), "is not a valid variety." )
            
    def display_variety_size(self, variety, size):
        self.variety = str(variety)
        self.size = size
        if self.variety in ['purple', 'red', 'yellow']:
            for self.a in range(len(self.location)):
                for self.c in range(len(self.location[self.a])):
                    for self.r in range(len(self.location[self.a][self.c])):
                        if type(self.location[self.a][self.c][self.r]) == Tote and \
                            self.location[self.a][self.c][self.r].tote_variety == str(self.variety) \
                            and self.location[self.a][self.c][self.r].tote_size == str(self.size):
                            print(self.location[self.a][self.c][self.r])
                            print()
        else:
            print(self.variety.capitalize(), "is not a valid variety." )
            
    def get_tote(self, variety, size):
        self.variety = variety
        self.size = size
        self.first_tote = 0
        self.fifo_tote = 0
        self.tote_aisle = 0
        self.tote_column = 0
        self.tote_row = 0
        for self.a in range(len(self.location)):
            for self.c in range(len(self.location[self.a])):
                for self.r in range(len(self.location[self.a][self.c])):
                    if type(self.location[self.a][self.c][self.r]) == Tote and \
                        self.location[self.a][self.c][self.r].tote_variety == str(self.variety) and \
                        self.location[self.a][self.c][self.r].tote_size == str(self.size):
                        self.first_tote = self.location[self.a][self.c][self.r]
                        self.tote_aisle = self.a
                        self.tote_column = self.c
                        self.tote_row = self.r
                        break
                else:
                    continue
                break
            else:
                continue
            break

    
        for self.a in range(len(self.location)):
            for self.c in range(len(self.location[self.a])):
                for self.r in range(len(self.location[self.a][self.c])):
                    if type(self.location[self.a][self.c][self.r]) == Tote and \
                        self.location[self.a][self.c][self.r].tote_variety == str(self.variety) and \
                        self.location[self.a][self.c][self.r].tote_size == str(self.size) and \
                        self.location[self.a][self.c][self.r].tote_time < self.first_tote.tote_time:
                        self.fifo_tote = self.location[self.a][self.c][self.r]
                        self.tote_aisle = self.a
                        self.tote_column = self.c
                        self.tote_row = self.r
                    else:
                        self.fifo_tote = self.first_tote
        self.location[self.tote_aisle][self.tote_column][self.tote_row] = 0
        return self.fifo_tote
    


def operator_interface():
    
    
    # Main Screen
    cmd = ''
    while cmd != 'q':  
        cmd = input("1 - Create Order\n"
                    "2 - Display Cold Storage\n"
                    "3 - Find\n"
                    "h - Help Menu\n"
                    "q - quit\n"
                    "\n""Please enter a command: "
                    )
        
        # Create an order
        if cmd == '1':
            while cmd != 'b':
                cmd = input("1 - Create Receiving Line Order\n"
                            "2 - Create Wash Line Order\n"
                            "b - Back\n"
                            "\n""Please enter a command: ")
                if cmd == '1':
                
                    # Input order variety
                    order_variety = input_variety()
                        
                    # Input order wieght
                    order_weight = input_weight()
                    
                    # Create the order, yes or no?
                    order_num = ReceiveOrder.count
                    order[order_num] = ReceiveOrder(order_variety, order_weight)
                    print("Product:", order_variety.capitalize(),"\n"
                          "Quantity:", order_weight)
                    cmd = input("Execute order? y = yes, n no: ")
                    if cmd == 'y':
                        order[order_num].execute()
                        print("\n""Order executed.")
                    else:
                        print("\n""Order aborted.")
                        
                elif cmd == '2':
                
                    order_variety = input_variety()
                    order_size = input_size()
                    order_totes = input_tote()
                    order_num = WashOrder.count
                    wash_order[order_num] = WashOrder(order_variety, order_size, order_totes)
                    print("Product:", order_variety.capitalize(),"\n"
                          "Size:", order_size, "\n"
                          "Quantity:", order_totes)
                    cmd = input("Execute order? y = yes, n no: ")
                    if cmd == 'y':
                        wash_order[order_num].execute()
                        print("\n""Order executed.")
                    else:
                        print("\n""Order aborted.")
                    
                    
                
        # Display Cold Storage
        elif cmd == '2':
            a.display()
            
        # Find
        elif cmd == '3':
            cmd = ''
            cmd = input("1 - Find by variety.\n"
                        "2 - Find by size.\n"
                        "3 - Find by variety and size\n"
                        "4 - Find by location.\n"
                        "\n""Please enter a command: ")
            
            if cmd == '1':
                find_variety = input_variety()
                print()
                a.display_variety(find_variety)
                
            elif cmd == '2':
                find_size = input_size()
                print()
                a.display_size(find_size)
                
            elif cmd == '3':
                find_variety = input_variety()
                find_size = input_size()
                print()
                a.display_variety_size(find_variety, find_size)
                
            elif cmd == '4':
                find_aisle = input_aisle()
                find_column = input_column()
                find_row = input_row()
                print()
                print(a.location[find_aisle][find_column][find_row])
                
            else:
                print("'"+ cmd + "'", 'is an invalid entry.')
                
            
    
        elif cmd == 'q':
            print("Program terminated")
            
        elif cmd == "h":
            print("\nWelcome to SamCo's Warehouse Management System.\n"
                  "This program simulates a warehouse management system.  The primary user\n" 
                  "interaction deals with executing Receiving Line orders to create and place\n" 
                  "totes into the inventory/Cold Storage, as well as executing Wash Line orders\n" 
                  "to remove totes from the Cold Storage.  Other functionality is built into the\n" 
                  "system but is self-explanatory.  Please explore the program and have fun!\n")
        
        else:
            print("'"+ cmd + "'", 'is an invalid entry.')

tote = [i for i in range(1000000)]
order = [i for i in range(1000)]
wash_order = [i for i in range(1000)]
a = ColdStorage('a',5,5,5)  
b = ColdStorage('b',5,5,5)
c = ColdStorage('c',5,5,5)
d = ColdStorage('d',5,5,5)    

operator_interface()


























