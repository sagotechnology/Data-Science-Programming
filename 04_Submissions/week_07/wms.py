import datetime
import random
import interface


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


class Order():
    count = 0
    
    def __init__(self, variety):
        self.variety = variety
        

class ReceiveOrder(Order):
    """This class is for receiving line orders.  The required attributes are
    variety, pounds, and storage destination.  Once an order is created it
    should be executed.  This will create bins with random sizes and weights
    between 1200 to 1250lbs.  The bins will then be placed in the first 
    available stroage location"""    
    
    count = 0
    # An order must contain a varitey and the amount of pounds in the order
    def __init__(self, variety, pounds, storage):
        super().__init__(variety) 
        self.pounds = pounds
        self.storage = storage
        ReceiveOrder.count += 1
        self.order_currentDT = datetime.datetime.now()
        self.order_date = self.order_currentDT.month, self.order_currentDT.day, self.order_currentDT.year
        self.order_time = self.order_currentDT.hour, self.order_currentDT.minute
        
    # This function runs the order and creates totes    
    def execute_a(self):
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
        
    # This function runs the order and creates totes    
    def execute_b(self):
        self.remaining = self.pounds
        while self.remaining >= 1250:
            self.i = Empty(tote)
            tote[self.i] = Tote(self.variety, RandomSize(), RandomWeight())
            self.j = b.get_location()
            b.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
            tote[self.i].location = (b.name.capitalize(), self.j[0], self.j[1], self.j[2])
            self.remaining -= tote[self.i].tote_weight
        self.i = Empty(tote)
        tote[self.i] = Tote(self.variety, RandomSize(), self.remaining)            
        self.j = b.get_location()
        b.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
        tote[self.i].location = (b.name.capitalize(), self.j[0], self.j[1], self.j[2])
        
    # This function runs the order and creates totes    
    def execute_c(self):
        self.remaining = self.pounds
        while self.remaining >= 1250:
            self.i = Empty(tote)
            tote[self.i] = Tote(self.variety, RandomSize(), RandomWeight())
            self.j = c.get_location()
            c.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
            tote[self.i].location = (c.name.capitalize(), self.j[0], self.j[1], self.j[2])
            self.remaining -= tote[self.i].tote_weight
        self.i = Empty(tote)
        tote[self.i] = Tote(self.variety, RandomSize(), self.remaining)            
        self.j = c.get_location()
        c.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
        tote[self.i].location = (c.name.capitalize(), self.j[0], self.j[1], self.j[2])
        
    # This function runs the order and creates totes    
    def execute_d(self):
        self.remaining = self.pounds
        while self.remaining >= 1250:
            self.i = Empty(tote)
            tote[self.i] = Tote(self.variety, RandomSize(), RandomWeight())
            self.j = d.get_location()
            d.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
            tote[self.i].location = (d.name.capitalize(), self.j[0], self.j[1], self.j[2])
            self.remaining -= tote[self.i].tote_weight
        self.i = Empty(tote)
        tote[self.i] = Tote(self.variety, RandomSize(), self.remaining)            
        self.j = d.get_location()
        d.location[self.j[0]][self.j[1]][self.j[2]] = tote[self.i]
        tote[self.i].location = (d.name.capitalize(), self.j[0], self.j[1], self.j[2])
        
    def __repr__(self):
        return 'Variety: ' +str(self.variety).capitalize() + '\n' \
                + 'Pounds: ' + str(self.pounds) + "\n" \
                + 'Storage: ' + str(self.storage.capitalize()) + "\n" \
                + 'Date: ' + str(self.order_currentDT.strftime("%m/%d/%Y")) + "\n" \
                + 'Time: ' + str(self.order_currentDT.strftime("%H:%M:%S"))
                
class WashOrder(Order):
    """This class is for wash line orders.  Wash line orders need a variety,
    product size, and number of totes.  Once the order is created and executed
    totes are removed from inventory following a first in first out (FIFO) method"""
    
    count = 0
    
    # An order must contain a varitey and the amount of pounds in the order
    def __init__(self, variety, size, totes):
        super().__init__(variety) 
        self.size = size
        self.totes = totes
        WashOrder.count += 1
        wash_history = []
        wash_history.append(wash_order[WashOrder.count])
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
    """This class is for Tote.  Every Tote has a variety, size, weight, location,
    time stamp, and ID.  I call this class from the receiving order class
    to create the bumber of bins necessary to complete the order."""
    
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
    
    # etter for tote id
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
        
    # tote represent
    def __repr__(self):
        return 'tote ID: ' + str(self.__tote_id) + '\n' \
                + 'Variety: ' + self.tote_variety.capitalize() + '\n' \
                + 'Size: ' + self.tote_size + '\n' \
                + 'Weight: ' + str(self.tote_weight) + 'lbs' + '\n' \
                + 'Location: ' + str(self.tote_location) + '\n' \
                + 'Date: ' + str(self.tote_currentDT.strftime("%m/%d/%Y")) + "\n" \
                + 'Time: ' + str(self.tote_currentDT.strftime("%H:%M:%S"))
                
class ColdStorage():
    """This class is for Cold Storages.  Cold stoages need a defined number of 
    aisle, columns, and rows.  Once totes are created using a receiving 
    order they are placed into inventory."""
    
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
                    "4 - Receiving Order History\n"
                    "h - Help Menu\n"
                    "q - Quit\n"
                    "\n""Please enter a command: "
                    )
        
        # Create an order
        if cmd == '1':
            while cmd != 'b':
                cmd = input("1 - Create Receiving Line Order\n"
                            "2 - Create Wash Line Order\n"
                            "b - Back\n"
                            "\n""Please enter a command: ")
                # Receiving Line Order
                if cmd == '1':
                
                    # Input order variety
                    order_variety = interface.input_variety()
                    # Input order wieght
                    order_weight = interface.input_weight()
                    order_storage = interface.input_storage()
                    order_num = ReceiveOrder.count
                    order[order_num] = ReceiveOrder(order_variety, order_weight, order_storage)
                    print("Product:", order_variety.capitalize(),"\n"
                          "Quantity:", order_weight, "\n"
                          "Storage:", order_storage.capitalize()
                          )
                    # Create the order, yes or no?
                    cmd = input("Execute order? y = yes, n no: ")
                    if cmd == 'y' and order_storage == 'a':
                        order[order_num].execute_a()
                        order_history.append(order[order_num])
                        print("\n""Order sent to Cold Storage A.")
                    elif cmd == 'y' and order_storage == 'b':
                        order[order_num].execute_b()
                        order_history.append(order[order_num])
                        print("\n""Order sent to Cold Storage B.")
                    elif cmd == 'y' and order_storage == 'c':
                        order[order_num].execute_c()
                        order_history.append(order[order_num])
                        print("\n""Order sent to Cold Storage C.")
                    elif cmd == 'y' and order_storage == 'd':
                        order[order_num].execute_d()
                        order_history.append(order[order_num])
                        print("\n""Order sent to Cold Storage D.")
                        
                    else:
                        print("\n""Order aborted.")
                        
                # Wash Line Order   
                elif cmd == '2':
                
                    order_variety = interface.input_variety()
                    order_size = interface.input_size()
                    order_totes = interface.input_tote()
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
            b.display()
            c.display()
            d.display()
            
        # Find
        elif cmd == '3':
            cmd = ''
            cmd = input("1 - Find by variety.\n"
                        "2 - Find by size.\n"
                        "3 - Find by variety and size\n"
                        "4 - Find by location.\n"
                        "\n""Please enter a command: ")
            
            # Find by variety
            if cmd == '1':
                find_variety = interface.input_variety()
                print()
                a.display_variety(find_variety)
                
            #Find by size    
            elif cmd == '2':
                find_size = interface.input_size()
                print()
                a.display_size(find_size)
            
            # Find by variety and size
            elif cmd == '3':
                find_variety = interface.input_variety()
                find_size = interface.input_size()
                print()
                a.display_variety_size(find_variety, find_size)
            
            # Find by location
            elif cmd == '4':
                find_aisle = interface.input_aisle()
                find_column = interface.input_column()
                find_row = interface.input_row()
                print()
                print(a.location[find_aisle][find_column][find_row])
                
            else:
                print("'"+ cmd + "'", 'is an invalid entry.')
        
        # View order history
        elif cmd == "4":
            for past_order in order_history:
                print(past_order)
                print()
    
        # Quit program
        elif cmd == 'q':
            print("Program terminated")
        
        # Help menu
        elif cmd == "h":
            interface.help_menu()
        
        else:
            print("'"+ cmd + "'", 'is an invalid entry.')

tote = [i for i in range(1000000)]
order = [i for i in range(1000)]
order_history = []
wash_order = [i for i in range(1000)]
a = ColdStorage('a',5,5,5)  
b = ColdStorage('b',5,5,5)
c = ColdStorage('c',5,5,5)
d = ColdStorage('d',5,5,5)    

operator_interface()


























