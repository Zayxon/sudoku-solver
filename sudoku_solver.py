EMPTY = 0
class Sudoku():
    def __init__(self, board_9x9):
        self.board = board_9x9

    def solve(self):
        found = self.find_empty()
        if not found:
            return True
        else:
            r, c = found # coordinates of the empty field
        
        for new_num in range(1,10):
            if (    self.is_row_valid(r, c, new_num) and
                    self.is_col_valid(r, c, new_num) and
                    self.is_square_valid(r, c, new_num)  ):

                self.board[r][c] = new_num

                # recursion
                if self.solve():
                    return True

                # solve method (for the next empty field) had FALSE return value
                # => our number must be incorrect
                # => we set our field back to empty (in case previous number is also incorrect)
                # => we continue looking for a valid number
                self.board[r][c] = EMPTY

        # solve method was unsuccessful in finding valid number
        return False


    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == EMPTY:
                    return row, col

    def is_row_valid(self, row, col, number):
        for i in range(9):
            if number == self.board[row][i]:
                return False
        return True

    def is_col_valid(self, row, col, number):
        for i in range(9):
            if number == self.board[i][col]:
                return False
        return True

    def is_square_valid(self, row, col, number):
        # starts scouting from the top-left corner of the exact square
        row = (row // 3) * 3
        col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if number == self.board[row + i][col + j]:
                    return False
        return True

    def print_board(self):
        for r in range(9):
            if r % 3 == 0:
                print("-------------------------")
            for c in range(9):
                if (c % 3) == 0:
                    print("| ", end="")
                print(self.board[r][c], end=" ")
                if c == 8:
                    print("|", end="")
            print()
            if r == 8:
                print("-------------------------")
    
    def get_board(self):
        return self.board


if __name__ == "__main__":
    # example of given input
    board_example = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    s = Sudoku(board_example)
    s.print_board()
    print("  ---- AFTER SOLVE ----")
    s.solve()
    s.print_board()