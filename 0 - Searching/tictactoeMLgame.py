#TicTacToe ML Minimax Algorithm
import math
import time
from tictactoeplayers import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = self.make_board() #Initialize with board and no winner yet
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self): #Print out the board in rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        
    @staticmethod
    # 0 | 1 | 2
    # 3 | 4 | 5
    # 6 | 7 | 8
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter): #Making a move on the board (number between 0 and 8)
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3 : (row_ind + 1) * 3] #Slice self.board for only that row
        if all([s == letter for s in row]):
            return True
        #check the column
        col_ind = square % 3 #Column based on remainders when divided by 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        #check the diagonal
        if square % 2 == 0: #all diagonal numbers are divisible by 2
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal_2]):
                return True
        return False
    
    def empty_squares(self): #Are any empty squares remaining
        return True if " " in self.board else False
    
    def num_empty_squares(self):
        return self.board.count(" ")
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)