from Board import Board
from ValidEntry import ValidEntry

check_valid = ValidEntry()

new_board = Board()


def solve(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if check_valid.valid_val(board, y, x, n):
                        board[y][x] = n
                        solve(board)
                        board[y][x] = 0
                return
    new_board.print_board(board)


b = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
     [6, 8, 0, 0, 7, 0, 0, 9, 0],
     [1, 9, 0, 0, 0, 4, 5, 0, 0],
     [8, 2, 0, 1, 0, 0, 0, 4, 0],
     [0, 0, 4, 6, 0, 2, 9, 0, 0],
     [0, 5, 0, 0, 0, 3, 0, 2, 8],
     [0, 0, 9, 3, 0, 0, 0, 7, 4],
     [0, 4, 0, 0, 5, 0, 0, 3, 6],
     [7, 0, 3, 0, 1, 8, 0, 0, 0]]

b2 = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
      [0, 0, 9, 0, 0, 0, 0, 4, 0],
      [7, 0, 2, 1, 0, 0, 9, 6, 0],
      [2, 0, 0, 0, 0, 0, 0, 9, 0],
      [0, 6, 0, 0, 0, 0, 0, 7, 0],
      [0, 7, 0, 0, 0, 6, 0, 0, 5],
      [0, 2, 7, 0, 0, 8, 4, 0, 6],
      [0, 3, 0, 0, 0, 0, 5, 0, 0],
      [5, 0, 0, 0, 6, 2, 0, 0, 8]]

b3 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 3, 6, 0, 0, 0, 0, 0],
      [0, 7, 0, 0, 9, 0, 2, 0, 0],
      [0, 5, 0, 0, 0, 7, 0, 0, 0],
      [0, 0, 0, 0, 4, 5, 7, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 3, 0],
      [0, 0, 1, 0, 0, 0, 0, 6, 8],
      [0, 0, 8, 5, 0, 0, 0, 1, 0],
      [0, 9, 0, 0, 0, 0, 4, 0, 0]]

      

solve(b3)
