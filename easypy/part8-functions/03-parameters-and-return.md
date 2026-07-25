---
title: Parameters and Return Values
order: 3
---

# Chapter 26: Parameters and Return Values

Functions become powerful when they **take** board state and **return** updated state or True/False answers.

## Returning Booleans

```python
def is_inside_board(col, row, width, height):
    if col < 0 or col >= width:
        return False
    if row < 0 or row >= height:
        return False
    return True

print(is_inside_board(9, 0, 10, 20))   # True
print(is_inside_board(10, 0, 10, 20))  # False
```

## Returning New Data vs Mutating

Lists can change **in place**:

```python
def fill_bottom_row(board):
    board[-1] = ["#"] * len(board[0])
```

Or return new board (less common for us):

```python
def copy_board(board):
    return [row[:] for row in board]
```

## Default Parameters

```python
def make_row(width=10, char="."):
    return [char] * width

make_row()
make_row(5, "#")
```

Defaults must come after non-default parameters.

## Early return

```python
def can_place(board, cells):
    for row, col in cells:
        if board[row][col] != ".":
            return False
    return True
```

Stop as soon as you know the answer.

## Tetris — Cells from Piece

Piece at anchor `(piece_row, piece_col)` with offsets:

```python
def get_piece_cells(piece_row, piece_col, shape_offsets):
    cells = []
    for dr, dc in shape_offsets:
        r = piece_row + dr
        c = piece_col + dc
        cells.append((r, c))
    return cells
```

## Main Program Structure

```python
def main():
    board = make_board()
    draw_board(board)

if __name__ == "__main__":
    main()
```

Running the file calls `main()` — standard Python pattern.

## Try It Yourself

Write `def count_filled(row):` returning how many `#` in a row list.

## Summary

- Functions **return** results: numbers, lists, booleans.
- **Default parameters** optional arguments.
- **`if __name__ == "__main__"`** entry point.
- Ready for **Tetris Part 9**.

**Next:** [How Tetris Works](../part9-tetris-foundations/01-game-design-overview.html)
