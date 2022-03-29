import random

class Marble:
    """Class of a single Marble """
    def __init__(self, char):
        if len(char) > 1:
            print("Invalid Marble Name")
            return
        self.name = char
        self.pos = [0, 0]
           
class GaltonBox:
    """Class of a box to drop the marbles in"""
    
    def __init__(self, row):
        self.size = row
        self.marble_list = []
    
    def insert_marble(self, marble):
        self.marble_list.append(marble)
        
    def time_step(self):
        # Update the marble each time step until that marble reaches the bottom of the box
        for marble in self.marble_list:
            if marble.pos[0] != self.size - 1:
                marble.pos[0] += 1
                marble.pos[1] += random.randint(0, 1) 
            
    def __repr__(self):
        output = ""
        box = []
        
        # Create the box with all -s
        for row in range(1, self.size + 1):
            box.append(list('-' * row))
        
        # Now put the replace the -s with the marbles at those positions
        for marble in self.marble_list:
            box[marble.pos[0]][marble.pos[1]] = marble.name
            
        # Make the output string
        for rows in box:
            output += ''.join(rows)
            output += "\n"
        return output