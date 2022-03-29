class MarblesBoard():
    
    def __init__(self, marbles = (0)):
        self.marble_positions = list(marbles)
        
    def __repr__(self):
        return " ".join(str(m) for m in self.marble_positions)
    
    def switch(self):
        self.marble_positions = self.marble_positions[1:2] + self.marble_positions[0:1] + self.marble_positions[2:]
        
    def rotate(self):
        self.marble_positions = self.marble_positions[1:] + self.marble_positions[0:1]
        
    def answer(self):
        return (self.marble_positions == sorted(self.marble_positions))

class Solver():
    
    def __init__(self, solver_input):
        self.positions = solver_input
    
    def solve(self):
        step = 0
        
        while not self.positions.answer():
            print(self.positions)
            if (self.positions.marble_positions[0] > self.positions.marble_positions[1] and self.positions.marble_positions[1] != 0):
                self.positions.switch()
            else:
                self.positions.rotate()
            step += 1
            
        print(self.positions)
        print("total steps:", step)