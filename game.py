from board import Board
from player import PlayerMM, PlayerAB, ManualPlayer

class Game:

    def __init__(self, player1, player0):
        self.board = Board()
        self.player1 = player1
        self.player0 = player0

    def play(self):

        is_player1 = True

        while(True):

            # take turns
            if is_player1:
                move = self.player1.bestmove(self.board)
            else:
                move = self.player0.bestmove(self.board)

            player = "Player " + ('1' if is_player1 else '0')
            print(f'{player} moved at {move}')

            #make the move
            self.board.makeMove(move)
            print(self.board)
            print(self.board.numMoves)
            print(self.board.lastMove)

            # check if game ended
            did_end = self.board.end()
            if did_end == Board.IS_DRAW:
                print("It is a draw!")
                break
            elif did_end == Board.PLAYER_1_WINS:
                print("Player 1 wins!")
                break
            elif did_end == Board.PLAYER_0_WINS:
                print("Player 0 wins!")
                break
            else:
                is_player1 = not is_player1



if __name__ == "__main__":
    game = Game(PlayerMM(4, True), PlayerMM(4, False))
    game.play()
