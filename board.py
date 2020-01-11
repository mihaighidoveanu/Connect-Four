class Board():
    #fixed dimensions of the Connect4 Board
    HEIGHT = 6
    WIDTH = 7
    PLAYER_0_WINS = 1
    PLAYER_1_WINS = 2
    IS_DRAW = -1

    def __init__(self, board = None, numMoves = 0, lastMove = None):

        if board is None:
            self.board = [[] for x in range(self.WIDTH)]
        else:
            self.board = [list(col) for col in board]
        self.numMoves = numMoves
        self.lastMove = lastMove

    def copy(self):
        return Board(self.board, self.numMoves, self.lastMove)

    # First player inserts a 1, and second player a 0
    def makeMove(self, column):
        column = column - 1
        self.numMoves += 1
        piece = self.numMoves % 2
        self.lastMove = (piece, column + 1)
        self.board[column].append(piece)

    # A child is of the form (move_to_make_child, child_board)
    def children(self):
        children = []
        for i in range(Board.WIDTH):
            # print(len(self.board[i]))
            if len(self.board[i]) < Board.HEIGHT:
                child = self.copy()
                # columns are numbered from 1 to 7
                i = i + 1
                child.makeMove(i)
                children.append((i, child))
        return children

    # Returns:
    #   False if the game did not end
    #   -1 if the game is a draw
    #   0 if player 0 wins
    #   1 if player 1 wins
    def end(self):
        for i in range(0,self.WIDTH):
            for j in range(0,self.HEIGHT):
                try:
                    if self.board[i][j]  == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j]  == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j]  + 1
                except IndexError:
                    pass

                try:
                    if not j + 3 > Board.HEIGHT and self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j - 3 < 0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

        if self.isFull():
            return Board.IS_DRAW
        return False

    def isFull(self):
        return self.numMoves == 42

    # X's are 1's and 0's are 0s
    def __str__(self):
        s = '\n'
        border = '+' + '---+' * Board.WIDTH
        s += border + '\n'
        for rowNum in range(Board.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(Board.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            s += row + '\n'
            s += border + '\n'
        return s


if __name__ == '__main__':
    board = Board()
    board.makeMove(1)
    board.makeMove(2)
    board.makeMove(2)
    board.makeMove(3)
    board.makeMove(1)
    board.makeMove(3)
    board.makeMove(3)
    board.makeMove(4)
    board.makeMove(4)
    board.makeMove(4)
    board.makeMove(4)
    board.makeMove(4)
    board.makeMove(5)
    print(board.end())
    print(board)
    print(board.numMoves)
    print(board.lastMove)


