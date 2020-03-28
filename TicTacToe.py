class TicTacToe:
    """
    A tictactoe game against optimal play using Minimax
    """
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.maxdepth = 9

    def print_board(self):
        """
        Print each board interleaved with | and _
        """
        for row in range(len(self.board)):
            print(str(self.board[row][0]) + '|' + str(self.board[row][1]) +'|' + str(self.board[row][2]))
            if row != len(self.board)-1:
                print('_ _ _')
            print()

    def check_for_winner(self) -> int:
        if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X' or \
            self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X' or \
            self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X' or \
            self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X' or \
            self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X' or \
            self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X' or \
            self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X' or \
            self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X': return -5000 #Player wins

        if self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O' or \
            self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O' or \
            self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O' or \
            self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O' or \
            self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O' or \
            self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O' or \
            self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O' or \
            self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O': return 5000 #Ai

        #If no winner, check if open move available else draw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return -1
        #Draw
        return 0

    def play_again(self):
        while True:
            try:
                res = str(input('Play again? Y/N: '))
                if res == 'N':
                    exit()
                elif res == 'Y':
                    print('Game On!')
                    main()
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid input Y/N: ')

    def check_game_over(self):
        self.print_board()
        score = self.check_for_winner()
        if score == -5000:
            print('Player Wins!')
            self.play_again()
        elif score == 5000:
            print('Computer Wins!')
            self.play_again()
        elif score == 0:
            print('Draw!')
            self.play_again()

    def player_move(self):
        while True:
            try:
                row = int(input('Enter row move: '))
                col = int(input('Enter col move: '))

                if not 0 <= row < 3 or not 0 <= col < 3:
                    raise ValueError

                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    print(f'Player moves on position: {row}, {col}')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Invalid move! Please enter valid move:')

    def comp_move(self):
        best, depth, score, row, col = float('-inf'), 0, float('-inf'), 0, 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O' #make move
                    score = self._min((depth+1))
                    if score > best:
                        row, col, best = i, j, score
                    self.board[i][j] = ' ' #undo move

        print('Computer moves: {}, {}'.format(row, col))
        self.board[row][col] = 'O'

    def _min(self, depth: int) -> int:
        """
        Minimax value: of a player is the smallest value that the other players
        can force the player to receive, knowing the player's actions;
        equivalently, it is the largest value the player can be sure to get
        when they know the actions of the other player
        """
        best, score = float('inf'), 0

        #Check if game over
        if self.check_for_winner() != -1:
            return self.check_for_winner()

        if depth == self.maxdepth:
            return

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X' #make move
                    score = self._max((depth+1))
                    if score < best:
                        best = score
                    self.board[i][j] = ' ' #undo move
        return best


    def _max(self, depth: int) -> int:
        best, score = float('-inf'), 0

        #Check if game over
        if self.check_for_winner() != -1:
            return self.check_for_winner()

        if depth == self.maxdepth:
            return

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O' #make move
                    score = self._min((depth+1))
                    if score > best:
                        best = score
                    self.board[i][j] = ' ' #undo move
        return best

def main():
    game = TicTacToe()
    game.print_board()
    while True:
        game.player_move()
        game.check_game_over()
        game.comp_move()
        game.check_game_over()

if __name__ == "__main__":
    main()
