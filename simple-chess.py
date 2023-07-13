class ChessGame:
    def __init__(self):
        self.board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

    def print_board(self):
        print("   ", end="")
        print("   ".join([chr(97 + i) for i in range(8)]))
        print("  ---------------------------------")
        for i in range(8):
            print(f"{8 - i} |", end="")
            for j in range(8):
                print(f" {self.board[i][j]} ", end="|")
            print(f" {8 - i}")
            print("  ---------------------------------")
        print("   ", end="")
        print("   ".join([chr(97 + i) for i in range(8)]))

    def move_piece(self, from_pos, to_pos):
        from_col, from_row = self.parse_position(from_pos)
        to_col, to_row = self.parse_position(to_pos)

        piece = self.board[from_row][from_col]
        self.board[from_row][from_col] = ' '
        self.board[to_row][to_col] = piece

    def parse_position(self, position):
        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        return col, row

    def play(self):
        self.print_board()

        while True:
            from_pos = input("Enter the position of the piece you want to move: ")
            to_pos = input("Enter the target position: ")

            self.move_piece(from_pos, to_pos)
            self.print_board()


# Start the game
chess_game = ChessGame()
