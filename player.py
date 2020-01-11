import math

from board import Board

class Player:

    def __init__(self, depth, is_player1):

        self.is_player1 = is_player1
        self.depth = depth

    def heuristic(self, board):
        heur = 0
        state = board.board
        for i in range(0, Board.WIDTH):
            for j in range(0, Board.HEIGHT):
                # check horizontal streaks
                try:
                    score = 0
                    # add player_1  streak scores to heur
                    if state[i][j] == state[i + 1][j]:
                        score = 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j]:
                        score = 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j]:
                        score = 10000

                    # player1 streak scores are added (he is max)
                    # player0 streak scores are substracted (he is min)
                    player = state[i][j]
                    if player == 1:
                        heur += score
                    else:
                        heur -= score

                except IndexError:
                    pass

                # check vertical streaks
                try:
                    score = 0
                    if state[i][j] == state[i][j + 1]:
                        score = 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2]:
                        score = 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3]:
                        score = 10000

                    player = state[i][j]
                    if player == 1:
                        heur += score
                    else:
                        heur -= score

                except IndexError:
                    pass

                # check primary diagonal streaks
                try:
                    score = 0
                    if state[i][j] == state[i + 1][j + 1] == 1:
                        score = 10
                    if state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                        score = 100
                    if state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 1:
                        score = 10000

                    player = state[i][j]
                    if player == 1:
                        heur += score
                    else:
                        heur -= score
                except IndexError:
                    pass

                # check secondary diagonal streaks
                try:
                    score = 0
                    if state[i][j] == state[i+1][j - 1] == 1:
                        score = 10
                    if state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 1:
                        score = 100
                    if state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 1:
                        score = 10000

                    player = state[i][j]
                    if player == 1:
                        heur += score
                    else:
                        heur -= score

                except IndexError:
                    pass
        return heur

class PlayerMM(Player):

    # runs minmax to find the optimal move
    def bestmove(self, board):
        score, move = self.minimax(board, self.depth, self.is_player1)
        return move

    # minimax algorithm
    def minimax(self, board, depth, is_player1):
        if board.end() == Board.IS_DRAW:
            return -math.inf if is_player1 else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1

        if is_player1:
            best_score = -math.inf
            is_better = lambda x: x > best_score
        else:
            best_score = math.inf
            is_better = lambda x: x < best_score

        best_move = -1

        children = board.children()
        for child in children:
            move, childboard = child
            # print('Move, ', move)
            temp, _ = self.minimax(childboard, depth - 1, not is_player1)
            if is_better(temp):
                best_score = temp
                best_move = move
        return best_score, best_move

class PlayerAB(Player):

    def bestmove(self, board):
        score, move = self.alphabeta(board, self.depth, self.is_player1, -math.inf, math.inf)
        return move

    def alphabeta(self, board, depth, is_player1, alpha, beta):
        if board.end() == Board.IS_DRAW:
            return -math.inf if is_player1 else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1

        if is_player1:
            best_score = -math.inf
            is_better = lambda x: x > best_score
        else:
            best_score = math.inf
            is_better = lambda x: x < best_score

        best_move = -1

        children = board.children()
        for child in children:
            move, childboard = child
            temp, _ = self.alphabeta(childboard, depth - 1, not is_player1, alpha, beta)
            if is_better(temp):
                best_score = temp
                best_move = move
            if is_player1:
                alpha = max(alpha, temp)
            else:
                beta = min(beta, temp)
            if alpha >= beta:
                break
        return best_score, best_move


class ManualPlayer(Player):
    def __init__(self):
        super().__init__(depth = None, is_player1 = None)

    def bestmove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " " + (str(c + 1) if len(board.board[c]) < 6 else ' ') + "  "
        print(opts)

        col = input("Place an " + ('X' if self.is_player1 else '0') + " in column: ")
        col = int(col) - 1
        return col

