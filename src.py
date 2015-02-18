from os import system

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
                return True
            else:
                return False

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
            if self.cells[x][y].fill(_x):
                return self.O
            else:
                return self.X
        else:
            return None

    def O(self, xy): # xy is tuple of coordinates which will be filled with O
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            if self.cells[x][y].fill(_o):
                return self.X
            else:
                return self.O
        else:
            return None

    def getrow(self, n): # returns specified row
        if 0 <= n < 3:
            return [self.cells[n][i].content for i in range(3)]
        else:
            return None

    def getcol(self, n): #returns specified column
        if 0 <= n < 3:
            return [self.cells[i][n].content for i in range(3)]
        else:
            return None

    def getdiag(self, n): #returns main diagonal for n=0 and other for n=1
        if n == 0:
            return [self.cells[i][i].content for i in range(3)]
        elif n == 1:
            return [self.cells[i][2-i].content for i in range(3)]
        else:
            return None

class Game:
    def __init__(self):
        # key2xy is dictionary, shows how to interpret input symbols in coordinates
        self.key2xy = {
            "q": (0, 0), "w": (0, 1), "e": (0, 2),
            "a": (1, 0), "s": (1, 1), "d": (1, 2),
            "z": (2, 0), "x": (2, 1), "c": (2, 2),
        }
        self.field = Field()        # init game field
        self.view = IO()            # the view
        self.player = self.field.X  # pointer to function to call on the next turn
        self.status = "_"           # "_" for game that is not ended, "x" or "o" for that who won, and None for draw
        self.x = True               # True if Player x must move

    def move(self, key):
        if not key in self.key2xy:
            return False
        # call the function specified in self.player (f.X or f.O)
        # as far as we can remember, f.X returns f.O and vice versa
        # so we can reassign player like this
        else:
            self.player = self.player(self.key2xy[key])
            self.x = self.player == self.field.X
            return True

    def checkwin(self):
        for i in range(3): # checking cols and rows
            row = self.field.getrow(i)
            if row[0] == row[1] == row[2]:
                return row[0]
            col = self.field.getcol(i)
            if col[0] == col[1] == col[2]:
                return col[0]

        for i in range(2): # checking diagonals
            diag = self.field.getdiag(i)
            if diag[0] == diag[1] == diag[2]:
                return diag[0]

        count = 0 #counting x-es and o-s
        for i in range(3):
            for j in range(3):
                if self.field.cells[i][j].content != "_":
                    count += 1

        if count == 9: # draw
            return None
        else: # in the middle of game
            return "_"

    def start(self):
        message = ""
        while self.status == "_":
            self.view.render(self.field)
            if self.x:
                message = "X goes:"
            else:
                message = "O goes:"
            turn = self.view.get_turn(message)
            while not self.move(turn):
                turn = self.view.get_turn("Incorrect input. Try again:")
            self.status = self.checkwin()

        self.view.render(self.field)
        self.view.show_message("Game over.")
        if self.status is None:
           message = "Draw."
        else:
           message = self.status + " wins"
        self.view.show_message(message)
        self.view.wait_and_close()

class IO:

    def render(self, field):
        system("clear") # Linux
        print(field, "\n\n")

    def get_turn(self, message):
        print(message)
        return input()

    def show_message(self, message):
        print(message)

    def wait_and_close(self):
        input()

game = Game()
game.start()
