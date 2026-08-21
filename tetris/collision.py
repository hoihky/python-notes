from constants import EMPTY, HEIGHT, WIDTH


def can_place(board, cells):
    for row, col in cells:
        if col < 0 or col >= WIDTH or row >= HEIGHT:
            return False
        if row < 0:
            continue
        if board[row][col] != EMPTY:
            return False
    return True
