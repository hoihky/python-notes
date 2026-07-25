---
title: Building the Board
order: 2
---

# Chapter 28: Building the Board

Create **`constants.py`** and **`board.py`** — foundation of the game.

## constants.py

```python
WIDTH = 10
HEIGHT = 20

EMPTY = "."
BLOCK = "#"
```

## board.py

```python
from constants import WIDTH, HEIGHT, EMPTY, BLOCK

def make_board():
    """Return empty HEIGHT x WIDTH grid."""
    return [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def draw_board(board, piece_cells=None, piece_char=BLOCK):
    """
    Draw board. piece_cells: list of (row, col) for falling piece.
  """
    display = [row[:] for row in board]  # copy
    if piece_cells:
        for r, c in piece_cells:
            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                display[r][c] = piece_char
    print("\n" * 2)
    for row in display:
        print("".join(row))

def is_cell_free(board, row, col):
    if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH:
        return False
    return board[row][col] == EMPTY
```

## Test It

```python
# at bottom of board.py
if __name__ == "__main__":
    b = make_board()
    draw_board(b)
    # fake piece cells
    cells = [(0, 4), (0, 5), (1, 4), (1, 5)]
    draw_board(b, cells)
```

Run:

```bash
python3 board.py
```

You should see empty grid, then O-shape on top.

## Why Copy for Display?

We must not permanently draw falling piece onto `board` until lock — overlay on **copy** for drawing only.

## Try It Yourself

Add a function `def fill_row(board, row_index):` setting one row to all `#`. Test drawing.

## Summary

- **`constants.py`** centralizes sizes and symbols.
- **`make_board`**, **`draw_board`**, **`is_cell_free`** are core.
- Falling piece drawn via **overlay** on copy.
- Next: **shape definitions**.

**Next:** [Tetromino Shapes](03-tetromino-shapes.html)
