_x = "x"
_o = "o"
_  = "_"

class Field:
    cells = []

    class Cell:
        def __init__(self):
            self.content = _

        def __repr__(self): #returns nice view of cell
            return self.content

        def fill(self, symbol): # fills the cell with symbol
            if self.content == _:
                self.content = symbol

    def __init__(self):
        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(self.Cell())

    def __repr__(self): # returns nice view of game field
        return "%s %s %s\n%s %s %s\n%s %s %s" % tuple(self.cells[i][j] for i in range(3) for j in range(3))

    def X(self, xy): # xy is tuple of coordinates which will be filled with X
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            self.cells[x][y].fill(_x)
            return self.O
        else:
            return None

    def O(self, xy): # xy is tuple of coordinates which will be filled with O
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            self.cells[x][y].fill(_o)
            return self.X
        else:
            return None

    def getrow(self, n): # returns specified row
        if 0 <= n < 3:
            return self.cells[n]
        else:
            return None

    def getcol(self, n): #returns specified column
        if 0 <= n < 3:
            return list(self.cells[i][n] for i in range(3))
        else:
            return None

    def getdiag(self, n): #returns main diagonal for n=0 and other for n=1
        if n == 0:
            return list(self.cells[i][i] for i in range(3))
        elif n == 1:
            return list(self.cells[i][2-i] for i in range(3))
        else:
            return None

class Game:
    def __init__(self, keys):
        # key2xy is dictionary, shows how to interpret input symbols in coordinates
        self.key2xy = {
            "q": (0, 0), "w": (0, 1), "e": (0, 2),
            "a": (1, 0), "s": (1, 1), "d": (1, 2),
            "z": (2, 0), "x": (2, 1), "c": (2, 2),
        }
        self.f = Field()        # init game field
        self.view = IO()        # the view
        self.player = self.f.X  # pointer to function to call on the next turn
        self.status = "_"       # "_" for game that is not ended, "x" or "o" for that who won, and None for draw

    def move(self, key):
        if key in self.key2xy:
            # call the function specified in self.player (f.X or f.O)
            # as far as we can remember, f.X returns f.O and vice versa
            # so we can reassign player like this
            self.player = self.player(self.key2xy[key])

    def checkwin(self):
        for i in range(3): # checking cols and rows
            row = self.f.getrow(i)
            if row[0] == row[1] == row[2]:
                return row[0]
            col = self.f.getcol(i)
            if col[0] == col[1] == col[2]:
                return col[0]

        for i in range(2): # checking diagonals
            diag = self.f.getdiag(i)
            if diag[0] == diag[1] == diag[2]:
                return diag[0]

        count = 0 #counting x-es and o-s
        for i in range(3):
            for j in range(3):
                if self.f.cells[i][j] != "_"
                    count += 1

        if count == 9: # draw
            return None
        else: # in the middle of game
            return "_"

    def start(self):


class IO:

    def render(self, field):
        print(field)

    def get_turn(self):
        return input()

game = Game()
print(game.f)
a=input()
game.move(a)
print(game.f)
a=input()
game.move(a)
print(game.f.getdiag(1))
