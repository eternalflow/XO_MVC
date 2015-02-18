from os import system


class Field:
    def __init__(self):
        self.cells = [[0,0,0],[0,0,0],[0,0,0]]

    def get(self, xy):
        x, y = xy
        if 0 <= x < 3 and 0 <= y < 3:
            return self.cells[x][y]

    def set(self, xy, val):  # xy is tuple of coordinates which will be filled with val
        x, y = xy
        if (self.cells[x][y] == 0) and 1 <= val <= 2:
            self.cells[x][y] = val

    def getrow(self, n):  # returns specified row
        if 0 <= n < 3:
            return [self.cells[n][i] for i in range(3)]
        else:
            return None

    def getcol(self, n):  # returns specified column
        if 0 <= n < 3:
            return [self.cells[i][n] for i in range(3)]
        else:
            return None

    def getdiag(self, n):  # returns main diagonal for n=0 and other for n=1
        if n == 0:
            return [self.cells[i][i] for i in range(3)]
        elif n == 1:
            return [self.cells[i][2-i] for i in range(3)]
        else:
            return None

    def checkwin(self):
        for i in range(3):  # checking cols and rows
            row = self.getrow(i)
            if row[0] == row[1] == row[2]:
                return row[0]
            col = self.getcol(i)
            if col[0] == col[1] == col[2]:
                return col[0]

        for i in range(2):  # checking diagonals
            diag = self.getdiag(i)
            if diag[0] == diag[1] == diag[2]:
                return diag[0]

        count = 0  # counting x-es and o-s
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] != 0:
                    count += 1
        if count == 9:  # draw
            return 3
        else:  # in the middle of game
            return 0


class Game:
    def __init__(self):
        # key2xy is dictionary, shows how to interpret input symbols in coordinates
        self.key2xy = {
            "q": (0, 0), "w": (0, 1), "e": (0, 2),
            "a": (1, 0), "s": (1, 1), "d": (1, 2),
            "z": (2, 0), "x": (2, 1), "c": (2, 2),
        }
        self.field = Field()  # init game field
        self.view = IO()      # the view
        self.player = 1       # x goes first

    def move(self, key):
        if not key in self.key2xy:
            return False
        else:
            if self.field.get(self.key2xy[key]) != 0:
                return False
            else:
                self.field.set(self.key2xy[key], self.player)
                self.player = 3 - self.player
                return True

    def start(self):
        status = self.field.checkwin()
        while status == 0:  # nobody won, no draw
            message = ""
            self.view.render(self.field)
            turn = self.view.get_turn(self.player)
            while not self.move(turn):
                turn = self.view.get_turn(self.player, error=True)
            status = self.field.checkwin()

        self.view.render(self.field)
        self.view.the_end(status)
        self.view.wait_and_close()


class IO:
    num2sym = {
        0: "_",
        1: "X",
        2: "O",
    }

    def decode_row(self, row):
        output = ""
        for i in row:
            output += self.num2sym[i] + " "
        return output

    def render(self, field):
        system("clear") # Linux
        for i in range(3):
            print(self.decode_row(field.getrow(i)))

    def get_turn(self, who, error=False):
        if error:
            print("Incorrect input!")
        if who == 1:
            print("X goes:")
        else:
            print("O goes:")
        return input()

    def the_end(self, status):
        if status == 1:
            message = "X wins"
        elif status == 2:
            message = "O wins"
        else:
            message = "Draw"
        print(message)

    def wait_and_close(self):
        input()

game = Game()
game.start()