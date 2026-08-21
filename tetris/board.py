from constants import BLOCK, EMPTY, HEIGHT, WIDTH


def make_board():
    """Return empty HEIGHT x WIDTH grid."""
    return [[EMPTY] * WIDTH for _ in range(HEIGHT)]


def draw_board(board, piece_cells=None, score=0, lines=0, piece_name=""):
    """
    Draw board. piece_cells: list of (row, col) for falling piece.
    """
    display = [row[:] for row in board]
    if piece_cells:
        for r, c in piece_cells:
            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                display[r][c] = BLOCK

    print("\n" * 2)
    print("=" * (WIDTH + 2))
    header = f" Score: {score}   Lines: {lines}"
    if piece_name:
        header += f"   Piece: {piece_name}"
    print(header)
    print("+" + "-" * WIDTH + "+")
    for row in display:
        print("|" + "".join(row) + "|")
    print("+" + "-" * WIDTH + "+")
    print(" a:left  d:right  s:down  w:rotate  h:hard drop  q:quit")


def is_cell_free(board, row, col):
    if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH:
        return False
    return board[row][col] == EMPTY


def fill_row(board, row_index):
    """Set one entire row to blocks — useful for testing line clear."""
    board[row_index] = [BLOCK] * WIDTH


def is_row_full(row):
    return EMPTY not in row


if __name__ == "__main__":
    b = make_board()
    draw_board(b)
    cells = [(0, 4), (0, 5), (1, 4), (1, 5)]
    draw_board(b, cells, piece_name="O")
