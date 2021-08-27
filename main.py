class Board:

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x = 0
        self.y = 0
        self.board = [["_" for s in range(r)] for d in range(c)]
        self.boardtour = [["_" for s in range(r)] for d in range(c)]
        self.moves = 1
        self.counter = 1

    def moveknight(self, x, y):
        self.x = x
        self.y = y
        self.board[x][y] = "X"

    def possible(self, xx, yy):
        if xx >= self.r or xx < 0:
            return False
        if yy >= self.c or yy < 0:
            return False
        if 'X' == self.board[xx][yy]:
            return False
        return True

    def nrofviablemoves(self, x, y):
        possibilites = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x + 1, y - 2),
                        (x - 1, y + 2), (x - 1, y - 2)]
        counter = 0
        for k in range(len(possibilites)):
            xx = possibilites[k][0]
            yy = possibilites[k][1]
            if self.possible(xx, yy):
                counter += 1
        return counter

    def printingviablemoves(self):
        x = self.x
        y = self.y
        possibilites = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x + 1, y - 2),
                        (x - 1, y + 2), (x - 1, y - 2)]
        for k in range(len(possibilites)):
            xx = possibilites[k][0]
            yy = possibilites[k][1]
            if self.possible(xx, yy):
                self.board[xx][yy] = self.nrofviablemoves(xx, yy)

    def clearing(self):
        for x in range(self.r):
            for y in range(self.c):
                try:
                    int(self.board[x][y])
                    self.board[x][y] = "_"
                except:
                    continue

    def printing(self, board):
        for x in range(self.r - 1, -1, -1):
            for y in range(self.c):
                print(board[x][y], end=' ')
            print("\n")
        print("\n")

    def warnsdorf(self):
        self.printingviablemoves()
        moves = 1000
        score = []
        for x in range(self.r):
            for y in range(self.c):
                try:
                    if int(self.board[x][y]) <= moves:
                        if int(self.board[x][y]) < moves:
                            moves = int(self.board[x][y])
                            score = []

                        score.append([x, y])
                except:
                    continue
        return score

    def putinboard(self, x, y, char):
        self.board[x][y] = char

    def whatnextmove(self, viablemoves):

        self.clearing()
        nextmove = 100
        movetochoose = 0
        for x, e in reversed(list(enumerate(viablemoves))):
            self.moveknight(viablemoves[x][0], viablemoves[x][1])
            for z in range(self.r):
                for y in range(z):
                    if type(self.board[z][y]) is int and self.board[z][y] < nextmove:  # checking what move will be the best based on nr of possibilites after certain move
                        nextmove = self.board[z][y]
                        movetochoose = x
            self.putinboard(viablemoves[x][0], viablemoves[x][1], "_")
            self.clearing()
        return movetochoose

    def fastcheck(self):
        if self.r != self.c:
            print("there is no solution, the board must be square")
            raise SystemExit(0)

    def solution(self):
        if self.counter == 1:
            self.fastcheck()

        self.printboardtour()

        viablemoves = self.warnsdorf()

        if self.counter == self.r * self.c:
            return "there is a solution"
        elif len(viablemoves) == 0:
            return "there is no solution"
        else:
            self.bestknightmove(viablemoves)
            return self.solution()

    def bestknightmove(self, viablemoves):
        movetochoose = self.whatnextmove(viablemoves)
        x, y = viablemoves[movetochoose][0], viablemoves[movetochoose][1]
        self.moveknight(x, y)
        self.clearing()
        self.counter += 1
        self.boardtour[x][y] = self.counter

    def printboardtour(self):
        if self.counter < 10:
            self.boardtour[self.x][self.y] = " " + str(self.counter)
        else:
            self.boardtour[self.x][self.y] = self.counter
        self.printing(self.boardtour)


def main():
    size = input("Input board size: ")
    size = size.split()
    board2 = Board(int(size[0]), int(size[1]))
    startposition = input("Input starting position: ")
    startposition = startposition.split()
    board2.moveknight(int(startposition[0]), int(startposition[1]))
    print(board2.solution())


if __name__ == "__main__":
    main()
