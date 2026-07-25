---
title: 2D Grids for Games
order: 2
---

# Chapter 22: 2D Grids for Games

Tetris board is a **grid**: rows and columns. In Python: a **list of lists** — each inner list is one row.

## Build Empty Board

```python
WIDTH = 10
HEIGHT = 20

def make_empty_board():
    board = []
    for _ in range(HEIGHT):
        row = ["."] * WIDTH
        board.append(row)
    return board

board = make_empty_board()
```

Or compact (common idiom):

```python
board = [["."] * WIDTH for _ in range(HEIGHT)]
```

## Read and Write a Cell

```python
row = 5
col = 3
board[row][col] = "#"

cell = board[row][col]
```

**row** = vertical (y), **col** = horizontal (x).

## Draw Board

```python
def draw_board(board):
    print("\n" * 2)
    for row in board:
        print("".join(row))

draw_board(board)
```

## Place a Small Shape

O-piece 2×2 at column 4, row 0:

```python
board[0][4] = "#"
board[0][5] = "#"
board[1][4] = "#"
board[1][5] = "#"
```

## Coordinates Mental Model

```
col 0  1  2  3  4 ...
row 0  .  .  .  .  #
row 1  .  .  .  .  #
...
```

Falling piece tracks `piece_row`, `piece_col` plus **shape offsets**.

## Copying Rows (Later)

When locking pieces, copy cell values — do not alias wrong lists.

```python
new_row = row[:]  # shallow copy of one row
```

## Try It Yourself

1. Create 10×6 empty board.
2. Draw a horizontal line of `#` on bottom row.
3. Draw board with `draw_board`.

Save as `board.py` in `my_tetris`.

## Summary

- **2D board** = list of row lists.
- Access **`board[row][col]`**.
- **`draw_board`** loops rows and joins characters.
- This is the **heart** of text Tetris.

**Next:** [Dictionaries](03-dictionaries.html)
