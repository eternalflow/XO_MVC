_x = "x"
_o = "o"
_  = "_"

class Field:
    cells = []

    class Cell:
        def __init__(self):
            self.content = _

        def __repr__(self):
            return self.content

        def fill(self, symbol):
            if self.content == _:
                self.content = symbol

    def __init__(self):
        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(self.Cell())

    def __repr__(self):
        return "%s %s %s\n%s %s %s\n%s %s %s" % tuple(self.cells[i][j] for i in range(3) for j in range(3))

    def X(self, xy):
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            self.cells[x][y].fill(_x)
            return self.O

    def O(self, xy):
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            self.cells[x][y].fill(_o)
            return self.X

    def getrow(self, n):
        if 0 <= n < 3:
            return self.cells[n]
        else:
            return None

    def getcol(self, n):
        if 0 <= n < 3:
            return list(self.cells[i][n] for i in range(3))
        else:
            return None

    def getdiag(self, n):
        if n == 0:
            return list(self.cells[i][i] for i in range(3))
        elif n == 1:
            return list(self.cells[i][2-i] for i in range(3))
        else:
            return None

class Game:
    key2xy = {
        "q":(0,0), "w":(0,1), "e":(0,2),
        "a":(1,0), "s":(1,1), "d":(1,2),
        "z":(2,0), "x":(2,1), "c":(2,2),
    }

    f = Field()
    player = f.X # The next turn

    def move(self, key):
        if key in self.key2xy:
            self.player = self.player(self.key2xy[key]) # Put the symbol on the field

    def checkwin(self):
        pass

class IO:
    pass

game = Game()
print(game.f)
a=input()
game.move(a)
print(game.f)
a=input()
game.move(a)
print(game.f.getdiag(1))
