class MarblesBoard():
    """Class of a board of a sequence of marbles"""
    
    def __init__(self, marbles):
        self.board = list(marbles)
        
    def switch(self):
        self.board.insert(0, self.board.pop(1))
        
    def rotate(self):
        self.board.append(self.board.pop(0))
        
    def is_solved(self):
        return (self.board == sorted(self.board))

    def __repr__(self):
        return " ".join(str(x) for x in self.board)
        
class Solver():
    """A class to solve a MarblesBoard object"""
    
    def __init__(self, boards):
        self.mboard = boards
        print(self.mboard)
    
    def solve(self):
        steps = 0
        
        while not self.mboard.is_solved():
            print(self.mboard)
            if (self.mboard.board[0] > self.mboard.board[1] and self.mboard.board[1] != 0):
                self.mboard.switch()
            else:
                self.mboard.rotate()
            steps += 1
        
        print(self.mboard)
        print("total steps:", steps)